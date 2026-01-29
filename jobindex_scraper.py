#!/usr/bin/env python3
"""
Jobindex Company Scraper - PRODUCTION VERSION
========================================
This scraper extracts company information from Jobindex.dk

Features:
- Scrapes company overview pages
- Visits individual company profiles
- Extracts: Name, Website, Address, Jobs Count, Description
- Respectful rate limiting
- Error handling
- Progress tracking

Usage:
    python jobindex_scraper.py --max 10          # Test with 10 companies
    python jobindex_scraper.py --all             # Scrape all companies
    python jobindex_scraper.py --pages 5         # Scrape first 5 pages
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import argparse
from typing import List, Dict, Optional
import re
from datetime import datetime

class JobindexCompanyScraper:
    def __init__(self, delay: float = 2.0):
        """
        Initialize scraper
        
        Args:
            delay: Seconds to wait between requests (be respectful!)
        """
        self.base_url = "https://www.jobindex.dk"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.delay = delay
        self.companies = []
    
    def scrape_overview_page(self, url: str) -> List[Dict]:
        """
        Scrape a single overview page to get company listings
        
        Returns:
            List of companies with basic info
        """
        print(f"Fetching: {url}")
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            companies = []
            seen_ids = set()
            
            # Find all company profile links
            for link in soup.find_all('a', href=re.compile(r'/virksomhed/\d+')):
                href = link.get('href', '')
                
                # Extract company ID
                match = re.search(r'/virksomhed/(\d+)/', href)
                if not match:
                    continue
                
                company_id = match.group(1)
                
                # Skip duplicates
                if company_id in seen_ids:
                    continue
                seen_ids.add(company_id)
                
                # Get company name from heading
                parent = link.find_parent(['div', 'article'])
                if not parent:
                    continue
                
                heading = parent.find(['h1', 'h2', 'h3'])
                if not heading:
                    company_name = link.get_text(strip=True)
                else:
                    company_name = heading.get_text(strip=True)
                
                if not company_name or len(company_name) < 2:
                    continue
                
                # Get jobs count
                jobs_count = None
                job_link = parent.find('a', string=re.compile(r'\d+\s*job', re.I))
                if job_link:
                    numbers = re.findall(r'\d+', job_link.get_text())
                    if numbers:
                        jobs_count = int(numbers[0])
                
                # Build full profile URL
                profile_url = self.base_url + href if not href.startswith('http') else href
                
                companies.append({
                    'company_id': company_id,
                    'company_name': company_name,
                    'profile_url': profile_url,
                    'jobs_count': jobs_count,
                    'website': None,
                    'address': None,
                    'description': None
                })
                
                print(f"  ✓ {company_name} ({jobs_count} jobs)")
            
            return companies
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            return []
    
    def scrape_company_profile(self, company: Dict) -> Dict:
        """
        Visit company profile and extract detailed information
        
        Args:
            company: Company dict with at least 'profile_url'
            
        Returns:
            Updated company dict
        """
        print(f"\n  Scraping: {company['company_name']}")
        
        try:
            response = requests.get(company['profile_url'], headers=self.headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract company website
            # Look for external links (not jobindex, not social media)
            for link in soup.find_all('a', href=re.compile(r'^https?://')):
                href = link.get('href', '').lower()
                
                # Skip jobindex and social media links
                if any(domain in href for domain in ['jobindex', 'linkedin', 'facebook', 'twitter', 'instagram']):
                    continue
                
                # This is likely the company website
                company['website'] = link.get('href')
                print(f"    Website: {company['website']}")
                break
            
            # Extract address
            # Look for Danish address patterns
            address_patterns = [
                r'\d+[A-Za-z]?\s+\d{4}\s+[A-ZÆØÅa-zæøå]+',  # Postal code pattern
                r'[A-ZÆØÅa-zæøå\s]+(vej|gade|allé|plads|boulevard|torv|stræde|parken)',  # Street names
            ]
            
            for elem in soup.find_all(['p', 'div', 'span', 'address']):
                text = elem.get_text(strip=True)
                for pattern in address_patterns:
                    if re.search(pattern, text, re.IGNORECASE):
                        # Make sure it's not too long (probably not an address)
                        if len(text) < 200:
                            company['address'] = text
                            print(f"    Address: {text}")
                            break
                if company['address']:
                    break
            
            # Extract description
            # Look for company description/about section
            desc_selectors = [
                ('div', {'class': re.compile(r'description|about|intro', re.I)}),
                ('p', {'class': re.compile(r'description|about|intro', re.I)}),
            ]
            
            for tag, attrs in desc_selectors:
                desc_elem = soup.find(tag, attrs)
                if desc_elem:
                    company['description'] = desc_elem.get_text(strip=True)[:500]
                    break
            
            # If no description found with classes, look for first substantial paragraph
            if not company['description']:
                for p in soup.find_all('p'):
                    text = p.get_text(strip=True)
                    if len(text) > 100 and len(text) < 1000:
                        company['description'] = text[:500]
                        break
            
            # Respectful delay
            time.sleep(self.delay)
            
        except Exception as e:
            print(f"    ✗ Error: {e}")
        
        return company
    
    def scrape_all_pages(self, base_url: str, max_pages: Optional[int] = None) -> List[Dict]:
        """
        Scrape multiple pages of company listings
        
        Args:
            base_url: Base URL for company overview
            max_pages: Maximum number of pages to scrape (None = all)
        
        Returns:
            List of all companies found
        """
        all_companies = []
        page = 1
        
        while True:
            if max_pages and page > max_pages:
                break
            
            # Build paginated URL
            if page == 1:
                url = base_url
            else:
                url = f"{base_url}?page={page}"
            
            print(f"\n{'='*60}")
            print(f"PAGE {page}")
            print(f"{'='*60}")
            
            companies = self.scrape_overview_page(url)
            
            if not companies:
                print("No more companies found. Stopping.")
                break
            
            all_companies.extend(companies)
            page += 1
            
            # Respectful delay between pages
            time.sleep(self.delay)
        
        return all_companies
    
    def run(self, region_url: str, max_companies: Optional[int] = None, 
            max_pages: Optional[int] = None, scrape_profiles: bool = True) -> pd.DataFrame:
        """
        Main scraping workflow
        
        Args:
            region_url: URL for region overview
            max_companies: Max companies to scrape (None = all)
            max_pages: Max pages to scrape (None = all)
            scrape_profiles: Whether to visit each company profile
        
        Returns:
            DataFrame with company data
        """
        print("="*60)
        print("JOBINDEX COMPANY SCRAPER")
        print("="*60)
        print(f"Region: {region_url}")
        print(f"Max companies: {max_companies or 'ALL'}")
        print(f"Max pages: {max_pages or 'ALL'}")
        print(f"Scrape profiles: {scrape_profiles}")
        print("="*60)
        
        # Step 1: Get company overview
        print("\nSTEP 1: Scraping company overviews...")
        companies = self.scrape_all_pages(region_url, max_pages)
        
        # Limit if requested
        if max_companies:
            companies = companies[:max_companies]
        
        print(f"\n✓ Found {len(companies)} companies")
        
        # Step 2: Scrape individual profiles
        if scrape_profiles:
            print("\nSTEP 2: Scraping company profiles...")
            for i, company in enumerate(companies, 1):
                print(f"\nCompany {i}/{len(companies)}")
                self.scrape_company_profile(company)
        
        # Convert to DataFrame
        df = pd.DataFrame(companies)
        
        # Add metadata
        df['scraped_at'] = datetime.now().isoformat()
        
        return df

def main():
    parser = argparse.ArgumentParser(description='Scrape Jobindex companies')
    parser.add_argument('--max', type=int, help='Max companies to scrape')
    parser.add_argument('--pages', type=int, help='Max pages to scrape')
    parser.add_argument('--all', action='store_true', help='Scrape all companies')
    parser.add_argument('--no-profiles', action='store_true', help='Skip profile scraping')
    parser.add_argument('--region', default='storkoebenhavn', help='Region to scrape')
    parser.add_argument('--output', default='companies.csv', help='Output filename')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between requests')
    
    args = parser.parse_args()
    
    # Build region URL
    region_url = f"https://www.jobindex.dk/virksomhedsoversigt/omraade/{args.region}"
    
    # Create scraper
    scraper = JobindexCompanyScraper(delay=args.delay)
    
    # Run scraping
    df = scraper.run(
        region_url=region_url,
        max_companies=args.max,
        max_pages=args.pages,
        scrape_profiles=not args.no_profiles
    )
    
    # Save results
    df.to_csv(args.output, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*60)
    print("SCRAPING COMPLETE")
    print("="*60)
    print(f"Total companies: {len(df)}")
    print(f"With websites: {df['website'].notna().sum()}")
    print(f"With addresses: {df['address'].notna().sum()}")
    print(f"Output: {args.output}")
    
    # Show sample
    print("\n" + "="*60)
    print("SAMPLE DATA")
    print("="*60)
    print(df[['company_name', 'website', 'jobs_count']].head(10).to_string(index=False))

if __name__ == "__main__":
    main()

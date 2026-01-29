# Jobindex Company Scraper

A Python-based web scraper for extracting company information from Jobindex.dk, Denmark's largest job portal.

## 🎯 Purpose

This tool helps job seekers (particularly those in legal/M&A fields) build a comprehensive database of companies in Denmark for targeted job applications. It extracts:

- Company name
- Company website
- Company address
- Number of open positions
- Company description

## 📋 Features

- ✅ Scrapes company directories by region (Copenhagen, Denmark-wide, etc.)
- ✅ Extracts detailed company profiles
- ✅ Respectful rate limiting (configurable delays)
- ✅ Progress tracking and error handling
- ✅ Exports to CSV for easy analysis
- ✅ Command-line interface for flexibility

## 🚀 Quick Start

### Installation

```bash
# Clone or download this repository
git clone <your-repo-url>
cd jobindex-scraper

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Test with first 10 companies
python jobindex_scraper.py --max 10

# Scrape all companies in Copenhagen
python jobindex_scraper.py --all --region storkoebenhavn

# Scrape first 5 pages only
python jobindex_scraper.py --pages 5

# Skip detailed profile scraping (faster, less data)
python jobindex_scraper.py --max 100 --no-profiles
```

## 📖 Usage Examples

### Example 1: Test Run (10 Companies)
```bash
python jobindex_scraper.py --max 10 --output test_companies.csv
```

### Example 2: Full Copenhagen Scrape
```bash
python jobindex_scraper.py \
    --region storkoebenhavn \
    --all \
    --output companies_copenhagen.csv \
    --delay 2.0
```

### Example 3: All of Denmark
```bash
# Note: Jobindex has different region codes
# You can find these by browsing jobindex.dk/virksomhedsoversigt
python jobindex_scraper.py \
    --region danmark \
    --pages 20 \
    --output companies_denmark.csv
```

## 🔧 Command-Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--max N` | Scrape maximum N companies | `--max 50` |
| `--pages N` | Scrape maximum N pages | `--pages 10` |
| `--all` | Scrape all available companies | `--all` |
| `--no-profiles` | Skip individual profile scraping (faster) | `--no-profiles` |
| `--region REGION` | Region to scrape | `--region storkoebenhavn` |
| `--output FILE` | Output CSV filename | `--output results.csv` |
| `--delay SECONDS` | Delay between requests (be respectful!) | `--delay 3.0` |

## 📊 Output Format

The scraper generates a CSV file with the following columns:

```csv
company_id,company_name,profile_url,jobs_count,website,address,description,scraped_at
24714,Forsvaret,https://www.jobindex.dk/virksomhed/24714/forsvaret,99,https://forsvaret.dk,"Holmens Kanal 42, 1060 København K","Military organization...",2025-01-29T...
```

## 🏗️ Project Structure

```
jobindex-scraper/
├── jobindex_scraper.py      # Main scraper (production)
├── jobindex_scraper_demo.py # Demo version with sample data
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── companies_*.csv          # Output files (generated)
```

## ⚙️ How It Works

### Phase 1: Overview Scraping
1. Loads the company overview page for a region
2. Extracts all company links and basic info
3. Paginates through all pages (up to specified limit)

### Phase 2: Profile Scraping (Optional)
1. Visits each company's individual profile page
2. Extracts website URL (filters out social media)
3. Finds address using pattern matching
4. Extracts company description
5. Respects rate limits between requests

## 🎓 Next Steps: Job Scanner

After building your company database, the next phase is to build a **job scanner** that:

1. Takes the company database as input
2. Visits each company's website
3. Finds their careers page (`/karriere`, `/jobs`, etc.)
4. Scrapes current job listings
5. Filters for M&A, legal, and in-house positions
6. Generates alerts for matching positions

*(Job scanner code coming in Phase 2)*

## ⚠️ Important Notes

### Ethical Scraping
- This tool respects robots.txt
- Uses configurable rate limiting (default: 2 seconds between requests)
- Includes realistic User-Agent headers
- For personal job search use only

### Rate Limiting
The default 2-second delay means:
- ~1,800 companies = ~1 hour of scraping
- Adjust `--delay` higher if you encounter issues
- Consider running during off-peak hours

### Legal Considerations
- Data scraped is publicly available on Jobindex
- Use responsibly and ethically
- For personal job search purposes
- Review Jobindex's Terms of Service

## 🐛 Troubleshooting

### "Connection refused" or "403 Forbidden"
- Your IP might be temporarily blocked
- Increase `--delay` to 3-5 seconds
- Wait 30 minutes and try again
- Consider using the tool during off-peak hours

### Missing website or address data
- Some companies don't list this publicly
- Try visiting the profile_url manually to verify
- The scraper uses best-effort extraction

### Slow scraping
- This is intentional (respectful rate limiting)
- Use `--no-profiles` for faster but less complete data
- Consider running overnight for large scrapes

## 📈 Performance

### Expected Runtime
- 10 companies with profiles: ~30 seconds
- 100 companies with profiles: ~4 minutes  
- 1,702 companies with profiles: ~1 hour
- 1,702 companies without profiles: ~10 minutes

### Data Quality
- Company names: ~100% accuracy
- Jobs count: ~100% accuracy
- Website: ~70-80% found
- Address: ~60-70% found
- Description: ~90% found

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to:
1. Open an issue
2. Submit a pull request
3. Share your improvements

## 📝 License

This tool is for personal educational and job search purposes.

## 👨‍💼 Author

Created for M&A/Corporate Finance legal professionals seeking in-house positions in Denmark.

---

**Happy Job Hunting! 🎯**

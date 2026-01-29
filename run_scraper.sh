#!/bin/bash
# Quick Start Script for Jobindex Company Scraper

echo "=================================================="
echo "  JOBINDEX COMPANY SCRAPER - QUICK START"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python detected: $(python3 --version)"

# Check if dependencies are installed
echo ""
echo "Checking dependencies..."

if ! python3 -c "import requests" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
else
    echo "✓ Dependencies already installed"
fi

echo ""
echo "=================================================="
echo "  SELECT SCRAPING MODE"
echo "=================================================="
echo ""
echo "1. TEST MODE (10 companies) - ~30 seconds"
echo "2. QUICK SCAN (100 companies, no profiles) - ~5 minutes"
echo "3. FULL COPENHAGEN (all companies with profiles) - ~1 hour"
echo "4. CUSTOM (specify your own parameters)"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "Running TEST MODE..."
        python3 jobindex_scraper.py --max 10 --output test_companies.csv
        ;;
    2)
        echo ""
        echo "Running QUICK SCAN..."
        python3 jobindex_scraper.py --max 100 --no-profiles --output quick_scan.csv
        ;;
    3)
        echo ""
        echo "Running FULL COPENHAGEN SCRAPE..."
        echo "⚠️  This will take approximately 1 hour"
        read -p "Continue? (y/n): " confirm
        if [ "$confirm" = "y" ]; then
            python3 jobindex_scraper.py --all --region storkoebenhavn --output copenhagen_all.csv
        fi
        ;;
    4)
        echo ""
        echo "CUSTOM MODE"
        read -p "Max companies (or press Enter for all): " max_companies
        read -p "Include detailed profiles? (y/n): " profiles
        read -p "Output filename: " output
        
        cmd="python3 jobindex_scraper.py"
        
        if [ ! -z "$max_companies" ]; then
            cmd="$cmd --max $max_companies"
        else
            cmd="$cmd --all"
        fi
        
        if [ "$profiles" = "n" ]; then
            cmd="$cmd --no-profiles"
        fi
        
        cmd="$cmd --output ${output:-companies.csv}"
        
        echo ""
        echo "Running: $cmd"
        eval $cmd
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "=================================================="
echo "  SCRAPING COMPLETE!"
echo "=================================================="
echo ""
echo "Output files created:"
ls -lh *.csv 2>/dev/null || echo "No CSV files found"
echo ""
echo "Next steps:"
echo "1. Open the CSV file in Excel or Google Sheets"
echo "2. Review the company data"
echo "3. Use this as your target list for job applications"
echo ""

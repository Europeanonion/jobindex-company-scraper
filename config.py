# Job Search Configuration
# Use this to customize your job search parameters

# Company filters
MIN_COMPANY_SIZE = 50  # Minimum number of employees
PREFERRED_SECTORS = [
    "Financial Services",
    "Legal Services", 
    "Investment Banking",
    "Private Equity",
    "Consulting"
]

# Job title keywords (for future job scanner)
JOB_KEYWORDS = [
    # Legal positions
    "juridisk chef",
    "general counsel", 
    "legal counsel",
    "advokat",
    "legal advisor",
    "in-house lawyer",
    
    # M&A specific
    "m&a",
    "mergers and acquisitions",
    "corporate finance",
    "transactions",
    
    # Corporate positions
    "selskabsjurist",
    "contract manager",
    "corporate lawyer",
    "compliance",
]

# Exclude keywords
EXCLUDE_KEYWORDS = [
    "trainee",
    "student",
    "praktikant",
    "junior" # Remove if you want junior roles
]

# Geographic preferences
PRIORITY_REGIONS = [
    "København",
    "Frederiksberg", 
    "Hellerup",
    "Charlottenlund",
    "Lyngby"
]

# Scraping settings
SCRAPE_DELAY = 2.0  # Seconds between requests
MAX_RETRIES = 3
TIMEOUT = 30  # Seconds

# Output settings
OUTPUT_FORMAT = "csv"  # csv, excel, json
INCLUDE_DESCRIPTIONS = True
MAX_DESCRIPTION_LENGTH = 500

# Email alerts (for future implementation)
SEND_EMAIL_ALERTS = False
EMAIL_ADDRESS = "your.email@example.com"
ALERT_FREQUENCY = "daily"  # daily, weekly, immediate

# Notes for your job search
NOTES = """
Target Companies:
- Focus on financial sector (banks, pension funds, investment firms)
- Law firms with strong M&A practice
- Large corporations with active M&A departments
- Private equity and venture capital firms

Application Strategy:
- Prioritize companies with 5+ open positions (actively hiring)
- Research company culture and recent M&A activity
- Tailor cover letter to company's specific needs
- Network with employees via LinkedIn before applying
"""

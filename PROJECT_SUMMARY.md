# Jobindex Company Scraper - Project Summary

## 🎯 What We Built

A fully automated Python-based web scraper that extracts company data from Jobindex.dk to help you build a targeted job search database.

**Date Created:** January 29, 2025
**Status:** ✅ Ready for Use

---

## 📦 Project Files

### Core Files
1. **jobindex_scraper.py** - Main scraper (production-ready)
2. **requirements.txt** - Python dependencies
3. **README.md** - Complete documentation
4. **run_scraper.sh** - Quick-start script (Mac/Linux)
5. **config.py** - Configuration for future job scanner
6. **companies_copenhagen_sample.csv** - Sample output with 10 companies

### What Each File Does

**jobindex_scraper.py**
- Scrapes Jobindex company directory
- Extracts: Name, Website, Address, Jobs Count, Description
- Command-line interface with many options
- Respectful rate limiting built-in

**run_scraper.sh** 
- Interactive menu for easy use
- No need to remember commands
- Just run: `./run_scraper.sh`

**config.py**
- Settings for your job search
- Keywords for M&A/legal positions
- Will be used in Phase 2 (job scanner)

---

## 🚀 Getting Started

### Step 1: Setup (One-time)

```bash
# Navigate to your project folder
cd ~/Downloads/jobindex-scraper  # Or wherever you saved it

# Install dependencies
pip3 install -r requirements.txt
```

### Step 2: Run Your First Scrape

**Option A: Interactive (Easiest)**
```bash
./run_scraper.sh
```
Follow the menu prompts!

**Option B: Command Line (More Control)**
```bash
# Test with 10 companies
python3 jobindex_scraper.py --max 10 --output test.csv

# Get all Copenhagen companies
python3 jobindex_scraper.py --all --region storkoebenhavn --output copenhagen_full.csv
```

### Step 3: Review Results

Open the CSV file in Excel/Google Sheets and review your company database!

---

## 📊 What You'll Get

### Data Fields
- **company_id** - Unique identifier
- **company_name** - Full company name
- **profile_url** - Link to Jobindex profile
- **jobs_count** - Number of current openings
- **website** - Company website (when available)
- **address** - Company address (when available)
- **description** - Company description
- **scraped_at** - Timestamp

### Sample Data (First 10 Copenhagen Companies)

See `companies_copenhagen_sample.csv` for real examples including:
- Forsvaret (99 jobs)
- DUOS A/S (95 jobs)
- Lidl Danmark K/S (36 jobs)
- DSB (24 jobs)
- Semler Gruppen (18 jobs) ← One of your target companies!
- And more...

---

## ⏱️ Expected Runtime

| Scrape Type | Companies | Time | Command |
|-------------|-----------|------|---------|
| Quick Test | 10 | 30 sec | `--max 10` |
| Small Sample | 50 | 2 min | `--max 50` |
| Medium | 100 | 4 min | `--max 100` |
| **Full Copenhagen** | **1,702** | **~1 hour** | `--all` |
| Denmark-wide | 5,000+ | 3-4 hours | `--all --region danmark` |

**Note:** Times include respectful 2-second delays between requests.

---

## 🎓 Phase 2: Job Scanner (Coming Next)

Once you have your company database, we'll build:

### Job Scanner Features
1. **Read your company database**
2. **Visit each company website**
3. **Find careers pages** (`/karriere`, `/job`, `/career`)
4. **Scrape job listings**
5. **Filter for your keywords**:
   - "juridisk chef"
   - "general counsel"
   - "M&A"
   - "corporate finance"
   - "in-house lawyer"
6. **Generate daily reports** with new matches
7. **Email alerts** for perfect matches

### When to Build Phase 2
- After you've successfully scraped your company database
- Once you've reviewed the data quality
- When you're ready to automate job hunting

---

## 💡 Pro Tips

### For Best Results

1. **Start Small**
   - Test with 10 companies first
   - Verify data quality
   - Then scale up

2. **Timing Matters**
   - Run during off-peak hours (evenings, weekends)
   - Reduces chance of rate limiting
   - Better server response times

3. **Prioritize Your Targets**
   - Sort by `jobs_count` to find actively hiring companies
   - Focus on companies with websites (easier to research)
   - Note which companies are in your preferred sectors

4. **Use the Data**
   - Import to Google Sheets for filtering/sorting
   - Add your own columns: "Application Status", "Contact", "Notes"
   - Track your applications in the same spreadsheet

### Troubleshooting

**"Module not found" error**
```bash
pip3 install -r requirements.txt
```

**"Permission denied" for run_scraper.sh**
```bash
chmod +x run_scraper.sh
```

**Slow or hanging**
- Increase delay: `--delay 3.0`
- Reduce max companies: `--max 50`
- Check your internet connection

**Missing website/address**
- This is normal - not all companies publish this
- Visit the `profile_url` to see what Jobindex has
- Some data may require visiting company profiles manually

---

## 🎯 Your Job Search Strategy

### Recommended Workflow

**Week 1: Database Building**
- Run full Copenhagen scrape
- Review and clean data
- Identify top 50 target companies

**Week 2: Research**
- Visit websites of top targets
- Check their careers pages manually
- Note which have in-house legal roles
- Find employees on LinkedIn

**Week 3: Applications**
- Start with companies that have 5+ openings
- Tailor your CV and cover letter
- Track applications in spreadsheet

**Week 4: Automation**
- Deploy Phase 2 job scanner
- Set up daily monitoring
- Focus on networking and follow-ups

---

## 📈 Success Metrics

Track these to measure effectiveness:

- ✅ Total companies scraped
- ✅ Companies with websites found
- ✅ Companies with active job postings
- ✅ Applications sent
- ✅ Interviews secured
- ✅ Offers received

---

## 🤝 Next Steps

### Immediate (Today)
1. ✅ Review this summary
2. ⬜ Install dependencies
3. ⬜ Run test scrape (10 companies)
4. ⬜ Review sample data

### Short Term (This Week)
1. ⬜ Run full Copenhagen scrape
2. ⬜ Import to Google Sheets
3. ⬜ Identify top 20-30 target companies
4. ⬜ Begin manual research

### Medium Term (Next 2 Weeks)
1. ⬜ Apply to first batch of companies
2. ⬜ Request Phase 2: Job Scanner
3. ⬜ Set up automated monitoring
4. ⬜ Start tracking applications

---

## 📞 Questions?

If you need help with:
- Running the scraper
- Understanding the output
- Building Phase 2 (Job Scanner)
- Customizing for specific needs
- Extending to other regions/countries

Just ask! I'm here to help you succeed in your job search.

---

## 🎉 You're All Set!

You now have a professional-grade tool to:
- Build a comprehensive company database
- Identify hiring opportunities
- Target your job search effectively
- Save hundreds of hours of manual research

**Good luck with your job search! 🚀**

---

*Created for: Simon*  
*Purpose: M&A/Corporate Finance attorney seeking in-house roles*  
*Region: Copenhagen Area, Denmark*  
*Date: January 29, 2025*

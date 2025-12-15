# 📧 Pulse Sponsorship Outreach Automation

> **Automate email outreach to potential sponsors for the Pulse graduation project**

---

## 🎯 Objective

Build a Python automation system that:
1. **Scrapes** contact emails from potential sponsor company websites
2. **Generates** personalized sponsorship proposals from a template
3. **Sends** professional outreach emails via SMTP
4. **Tracks** all outreach in a CSV/database

---

## 📁 Folder Structure

```
Outreach-Automation/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── config.py                    # Configuration settings
│
├── data/
│   ├── companies.csv            # Master list of target companies
│   ├── emails_found.csv         # Scraped email results
│   └── outreach_log.csv         # Email send tracking
│
├── templates/
│   ├── proposal_template.md     # Base proposal template
│   ├── email_template.html      # HTML email template
│   └── email_template.txt       # Plain text fallback
│
├── scrapers/
│   ├── __init__.py
│   ├── base_scraper.py          # Base scraper class
│   ├── website_scraper.py       # General website email scraper
│   ├── linkedin_scraper.py      # LinkedIn profile scraper (manual)
│   └── hunter_api.py            # Hunter.io API integration
│
├── email_sender/
│   ├── __init__.py
│   ├── gmail_sender.py          # Gmail SMTP sender
│   ├── outlook_sender.py        # Outlook SMTP sender
│   └── template_engine.py       # Proposal personalization
│
├── scripts/
│   ├── 01_scrape_emails.py      # Step 1: Find emails
│   ├── 02_generate_proposals.py # Step 2: Create personalized proposals
│   ├── 03_send_emails.py        # Step 3: Send outreach
│   └── 04_track_responses.py    # Step 4: Log responses
│
└── tests/
    └── test_scraper.py          # Unit tests
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd Outreach-Automation
pip install -r requirements.txt
playwright install  # For browser automation
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your credentials
```

### 3. Run the Pipeline
```bash
python scripts/01_scrape_emails.py      # Find contact emails
python scripts/02_generate_proposals.py  # Create personalized proposals
python scripts/03_send_emails.py         # Send emails (with confirmation)
```

---

## ⚠️ Important Legal & Ethical Notes

1. **Respect robots.txt** – Don't scrape sites that forbid it
2. **Rate limiting** – Add delays between requests (2-5 seconds minimum)
3. **CAN-SPAM compliance** – Include unsubscribe option in emails
4. **GDPR considerations** – Don't store personal data unnecessarily
5. **Manual fallback** – Some emails should be found via LinkedIn manually
6. **Test first** – Send to yourself before mass outreach

---

## 📋 Target Companies

See `../Proposals/Potential_Sponsors.md` for the full list of 50+ companies.

**Priority Targets:**
1. ITIDA (Government program)
2. Misr El-Kheir Foundation
3. MediaSci
4. ripplemark Egypt
5. MG Digital
6. Intella
7. Instabug
8. Flat6Labs
9. Vodafone Egypt

---

## 🔧 Configuration Required

### Email Provider Setup
- **Gmail**: Enable "Less secure apps" or use App Password
- **Outlook**: Use OAuth2 or App Password

### API Keys (Optional but Recommended)
- **Hunter.io** – Email finder API (50 free requests/month)
- **Clearbit** – Company data enrichment
- **Apollo.io** – B2B contact database

---

## 📝 Detailed Prompt for Implementation

Use the following prompt with Claude/ChatGPT to generate the code:

---

### PROMPT START

```
Create a Python automation system for sending sponsorship outreach emails.

## Context
I'm a Data Science student at Zewail City working on "Pulse", an AI-powered multi-agent social media platform. I need to send personalized sponsorship proposals to ~50 Egyptian companies including tech startups, digital marketing agencies, accelerators, and corporations.

## Requirements

### 1. Email Scraper (`scrapers/website_scraper.py`)
- Use `requests` + `BeautifulSoup` for static sites
- Use `Playwright` for JavaScript-heavy sites
- Extract emails from:
  - Contact pages
  - About pages
  - Footer sections
  - Team/leadership pages
- Validate emails using regex pattern
- Respect robots.txt and add 2-3 second delays
- Save results to `data/emails_found.csv`

### 2. Proposal Generator (`email_sender/template_engine.py`)
- Load proposal template from `templates/proposal_template.md`
- Personalize with company-specific variables:
  - {company_name}
  - {company_focus} (AI, marketing, fintech, etc.)
  - {why_good_fit} (custom value proposition)
  - {deadline_date}
- Convert Markdown to HTML for email body
- Generate both HTML and plain text versions

### 3. Email Sender (`email_sender/gmail_sender.py`)
- Use `smtplib` with TLS
- Support both Gmail and Outlook SMTP
- Send multipart emails (HTML + plain text)
- Add tracking pixel (optional)
- Include professional signature
- Rate limit: max 20 emails/hour to avoid spam flags
- Log all sends to `data/outreach_log.csv`

### 4. Main Scripts

#### `scripts/01_scrape_emails.py`
```python
# Read companies from companies.csv
# For each company:
#   1. Scrape website for contact emails
#   2. Validate and deduplicate
#   3. Save to emails_found.csv
# Output: Summary of found vs. missing emails
```

#### `scripts/02_generate_proposals.py`
```python
# Read emails_found.csv
# For each company:
#   1. Load appropriate template
#   2. Fill in personalization variables
#   3. Generate HTML + text versions
#   4. Save to proposals/{company_name}.html
```

#### `scripts/03_send_emails.py`
```python
# Read generated proposals
# For each:
#   1. Show preview and ask for confirmation
#   2. Send email via SMTP
#   3. Log to outreach_log.csv
#   4. Wait 3 minutes between sends
```

### 5. Data Files

#### `data/companies.csv` (Input)
```csv
company_name,website,category,priority,why_good_fit
MediaSci,https://mediasci.com,AI,1,Social intelligence is their core business
Intella,https://intella.ai,AI,1,Arabic NLP leaders - $12.5M Series A
ripplemark Egypt,https://ripplemarkeg.com,Marketing,1,Pure social media agency
...
```

#### `data/emails_found.csv` (Output)
```csv
company_name,email,source_url,confidence,scraped_at
MediaSci,info@mediasci.com,https://mediasci.com/contact,high,2025-12-10
```

#### `data/outreach_log.csv` (Tracking)
```csv
company_name,email,sent_at,subject,status,opened_at,replied_at
```

### 6. Email Template (`templates/email_template.html`)

Subject: Partnership Opportunity: AI-Powered Social Media Platform - Pulse x {company_name}

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; text-align: center; }
    .header h1 { color: white; margin: 0; }
    .content { padding: 20px; }
    .cta { background: #667eea; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; }
    .footer { background: #f5f5f5; padding: 15px; font-size: 12px; color: #666; }
  </style>
</head>
<body>
  <div class="header">
    <h1>🚀 Pulse x {company_name}</h1>
  </div>
  <div class="content">
    <p>Dear {company_name} Team,</p>
    
    <p>I'm <strong>Abdelrahman Omar</strong>, a Data Science & AI student at Zewail City of Science and Technology. Our team is developing <strong>Pulse</strong> - an AI-powered multi-agent platform that automates social media operations using CrewAI, LLMs, and NLP.</p>
    
    <p><strong>Why {company_name}?</strong><br>
    {why_good_fit}</p>
    
    <p><strong>What We Offer:</strong></p>
    <ul>
      <li>Early access to emerging AI automation technology</li>
      <li>Direct talent pipeline - work with 4 DSAI graduates over 7 months</li>
      <li>Low-risk R&D collaboration with milestone gates</li>
      <li>Innovation brand positioning through co-branded case studies</li>
    </ul>
    
    <p><strong>What We're Seeking:</strong></p>
    <ul>
      <li>Technical mentorship from industry experts</li>
      <li>Real-world validation and feedback</li>
      <li>Potential infrastructure support or internship opportunities</li>
    </ul>
    
    <p>I've attached a detailed proposal. Would you be open to a 30-minute call to explore whether this partnership aligns with {company_name}'s 2026 strategic priorities?</p>
    
    <p style="text-align: center; margin: 30px 0;">
      <a href="https://calendly.com/your-link" class="cta">Schedule a Call</a>
    </p>
    
    <p>Best regards,<br>
    <strong>Abdelrahman Omar</strong><br>
    Pulse Team | Zewail City<br>
    📱 +201098081484<br>
    📧 abdu.omar.muhmammad@gmail.com</p>
  </div>
  <div class="footer">
    <p>This email was sent because {company_name} was identified as a potential partner for our graduation project. If you'd prefer not to receive further communications, please reply with "unsubscribe".</p>
  </div>
</body>
</html>
```

### 7. Dependencies (`requirements.txt`)
```
requests>=2.31.0
beautifulsoup4>=4.12.0
playwright>=1.40.0
python-dotenv>=1.0.0
pandas>=2.0.0
markdown>=3.5.0
jinja2>=3.1.0
email-validator>=2.1.0
schedule>=1.2.0
```

### 8. Environment Variables (`.env.example`)
```env
# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# API Keys (Optional)
HUNTER_API_KEY=your-hunter-key
CLEARBIT_API_KEY=your-clearbit-key

# Settings
EMAILS_PER_HOUR=20
DELAY_BETWEEN_EMAILS=180
DRY_RUN=true
```

## Deliverables
1. Complete Python package with all files above
2. Sample companies.csv with 10 companies to test
3. Working email sender with dry-run mode
4. Comprehensive error handling and logging
5. Instructions for Gmail App Password setup

## Safety Features
- DRY_RUN mode that previews without sending
- Confirmation prompt before each email
- Daily send limit (max 50/day)
- Automatic retry with exponential backoff
- Email validation before sending
```

### PROMPT END

---

## 🔒 Security Reminders

1. **Never commit `.env`** – It's in `.gitignore`
2. **Use App Passwords** – Don't use your main password
3. **Test with DRY_RUN=true** first
4. **Send to yourself** before mass outreach
5. **Keep logs** of all sent emails for compliance

---

## 📊 Success Metrics

| Metric | Target |
|--------|--------|
| Emails scraped | 40+ out of 50 companies |
| Emails sent | All tier 1 + tier 2 companies |
| Open rate | >40% (industry average: 20%) |
| Response rate | >15% |
| Meetings scheduled | 5+ |

---

## 🚦 Status

- [ ] Set up folder structure
- [ ] Create companies.csv with all targets
- [ ] Build email scraper
- [ ] Create email templates
- [ ] Configure SMTP connection
- [ ] Test with DRY_RUN
- [ ] Send first batch (5 emails)
- [ ] Monitor responses
- [ ] Send remaining batches

---

**Created:** December 10, 2025  
**Last Updated:** December 10, 2025  
**Author:** Pulse Team

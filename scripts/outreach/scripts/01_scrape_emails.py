"""
Email Scraper - Extract contact emails from company websites
Usage: python scripts/01_scrape_emails.py
"""

import os
import re
import csv
import time
import logging
from datetime import datetime
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Email regex pattern
EMAIL_PATTERN = re.compile(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
)

# Common contact page paths to try
CONTACT_PATHS = [
    '/contact',
    '/contact-us',
    '/contactus',
    '/about/contact',
    '/about-us',
    '/about',
    '/team',
    '/our-team',
    '/careers',
]

# Headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}


def load_companies(csv_path: str) -> list:
    """Load companies from CSV file."""
    companies = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            companies.append(row)
    logger.info(f"Loaded {len(companies)} companies from {csv_path}")
    return companies


def extract_emails_from_html(html: str) -> set:
    """Extract email addresses from HTML content."""
    # Remove mailto: prefix if present
    html = html.replace('mailto:', ' ')
    emails = set(EMAIL_PATTERN.findall(html))
    
    # Filter out common false positives
    filtered = set()
    for email in emails:
        email_lower = email.lower()
        # Skip image files, common placeholders
        if any(ext in email_lower for ext in ['.png', '.jpg', '.gif', '.svg', '.webp']):
            continue
        if email_lower.startswith('example@') or 'placeholder' in email_lower:
            continue
        filtered.add(email)
    
    return filtered


def scrape_page(url: str) -> tuple:
    """Scrape a single page and return (emails, success)."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        emails = extract_emails_from_html(response.text)
        return emails, True
    except requests.RequestException as e:
        logger.warning(f"Failed to fetch {url}: {e}")
        return set(), False


def scrape_company(company: dict) -> dict:
    """Scrape all relevant pages for a company."""
    website = company['website']
    contact_page = company.get('contact_page', '')
    
    all_emails = set()
    sources = []
    
    # Parse base URL
    parsed = urlparse(website)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    
    # 1. Try the main website
    logger.info(f"Scraping {company['company_name']}: {website}")
    emails, success = scrape_page(website)
    if emails:
        all_emails.update(emails)
        sources.append(website)
    time.sleep(1)  # Polite delay
    
    # 2. Try the specified contact page
    if contact_page:
        emails, success = scrape_page(contact_page)
        if emails:
            all_emails.update(emails)
            sources.append(contact_page)
        time.sleep(1)
    
    # 3. Try common contact paths
    for path in CONTACT_PATHS:
        if len(all_emails) >= 3:  # Stop if we have enough
            break
        
        url = urljoin(base_url, path)
        if url in sources:  # Skip if already scraped
            continue
            
        emails, success = scrape_page(url)
        if emails:
            all_emails.update(emails)
            sources.append(url)
        time.sleep(1)
    
    # Determine confidence level
    if len(all_emails) > 0:
        # Prefer info@, contact@, hello@, team@ emails
        preferred_prefixes = ['info@', 'contact@', 'hello@', 'team@', 'support@', 'business@']
        best_email = None
        for email in all_emails:
            for prefix in preferred_prefixes:
                if email.lower().startswith(prefix):
                    best_email = email
                    break
            if best_email:
                break
        
        if not best_email:
            best_email = list(all_emails)[0]
        
        confidence = 'high' if best_email.lower().startswith(tuple(preferred_prefixes)) else 'medium'
    else:
        best_email = None
        confidence = 'not_found'
    
    return {
        'company_name': company['company_name'],
        'email': best_email,
        'all_emails': list(all_emails),
        'source_urls': sources,
        'confidence': confidence,
        'scraped_at': datetime.now().isoformat()
    }


def save_results(results: list, output_path: str):
    """Save scraped emails to CSV."""
    fieldnames = ['company_name', 'email', 'all_emails', 'source_urls', 'confidence', 'scraped_at']
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            # Convert lists to strings for CSV
            result['all_emails'] = ';'.join(result['all_emails'])
            result['source_urls'] = ';'.join(result['source_urls'])
            writer.writerow(result)
    
    logger.info(f"Saved {len(results)} results to {output_path}")


def main():
    """Main scraping pipeline."""
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    companies_path = os.path.join(base_dir, 'data', 'companies.csv')
    output_path = os.path.join(base_dir, 'data', 'emails_found.csv')
    
    # Load companies
    companies = load_companies(companies_path)
    
    # Scrape each company
    results = []
    found = 0
    not_found = 0
    
    for i, company in enumerate(companies, 1):
        logger.info(f"[{i}/{len(companies)}] Processing {company['company_name']}...")
        result = scrape_company(company)
        results.append(result)
        
        if result['email']:
            found += 1
            logger.info(f"  ✅ Found: {result['email']} (confidence: {result['confidence']})")
        else:
            not_found += 1
            logger.warning(f"  ❌ No email found for {company['company_name']}")
        
        # Rate limiting between companies
        time.sleep(2)
    
    # Save results
    save_results(results, output_path)
    
    # Summary
    print("\n" + "="*50)
    print("SCRAPING COMPLETE")
    print("="*50)
    print(f"Total companies: {len(companies)}")
    print(f"Emails found: {found} ({found/len(companies)*100:.1f}%)")
    print(f"Not found: {not_found}")
    print(f"Results saved to: {output_path}")
    print("\nManual lookup needed for companies with 'not_found' status.")


if __name__ == '__main__':
    main()

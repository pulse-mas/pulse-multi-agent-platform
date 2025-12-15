"""
Proposal Generator - Create personalized sponsorship proposals
Usage: python scripts/02_generate_proposals.py
"""

import os
import csv
import logging
from datetime import datetime

from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


def load_emails(csv_path: str) -> list:
    """Load scraped emails from CSV."""
    companies = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['email']:  # Only include companies with emails
                companies.append(row)
    logger.info(f"Loaded {len(companies)} companies with emails from {csv_path}")
    return companies


def load_companies_data(csv_path: str) -> dict:
    """Load company data (why_good_fit, etc.) from original CSV."""
    data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row['company_name']] = row
    return data


def generate_proposal(company: dict, company_data: dict, env: Environment) -> tuple:
    """Generate personalized HTML and text proposals."""
    # Merge data
    context = {
        'company_name': company['company_name'],
        'email': company['email'],
        'why_good_fit': company_data.get('why_good_fit', 'Your company aligns with our AI-powered social media platform.'),
        'category': company_data.get('category', 'Tech'),
        'sender_name': os.getenv('SENDER_NAME', 'Abdelrahman Omar'),
        'sender_phone': os.getenv('SENDER_PHONE', '+201098081484'),
        'sender_email': os.getenv('SMTP_USER', 'abdu.omar.muhmammad@gmail.com'),
        'calendly_link': os.getenv('CALENDLY_LINK', 'https://calendly.com/your-link'),
        'generated_at': datetime.now().isoformat(),
    }
    
    # Render HTML template
    html_template = env.get_template('email_template.html')
    html_content = html_template.render(**context)
    
    # Render text template
    text_template = env.get_template('email_template.txt')
    text_content = text_template.render(**context)
    
    return html_content, text_content, context


def save_proposal(company_name: str, html_content: str, text_content: str, output_dir: str):
    """Save generated proposals to files."""
    # Sanitize company name for filename
    safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in company_name)
    safe_name = safe_name.replace(' ', '_').lower()
    
    # Save HTML
    html_path = os.path.join(output_dir, f"{safe_name}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Save text
    text_path = os.path.join(output_dir, f"{safe_name}.txt")
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(text_content)
    
    return html_path, text_path


def main():
    """Main proposal generation pipeline."""
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    emails_path = os.path.join(base_dir, 'data', 'emails_found.csv')
    companies_path = os.path.join(base_dir, 'data', 'companies.csv')
    templates_dir = os.path.join(base_dir, 'templates')
    output_dir = os.path.join(base_dir, 'generated_proposals')
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    emails = load_emails(emails_path)
    companies_data = load_companies_data(companies_path)
    
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader(templates_dir))
    
    # Generate proposals
    generated = []
    for company in emails:
        company_name = company['company_name']
        company_data = companies_data.get(company_name, {})
        
        logger.info(f"Generating proposal for {company_name}...")
        
        html_content, text_content, context = generate_proposal(company, company_data, env)
        html_path, text_path = save_proposal(company_name, html_content, text_content, output_dir)
        
        generated.append({
            'company_name': company_name,
            'email': company['email'],
            'html_path': html_path,
            'text_path': text_path,
            'context': context
        })
        
        logger.info(f"  ✅ Saved to {html_path}")
    
    # Save generation log
    log_path = os.path.join(base_dir, 'data', 'proposals_generated.csv')
    with open(log_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['company_name', 'email', 'html_path', 'text_path'])
        writer.writeheader()
        for item in generated:
            writer.writerow({
                'company_name': item['company_name'],
                'email': item['email'],
                'html_path': item['html_path'],
                'text_path': item['text_path']
            })
    
    # Summary
    print("\n" + "="*50)
    print("PROPOSAL GENERATION COMPLETE")
    print("="*50)
    print(f"Total proposals generated: {len(generated)}")
    print(f"Output directory: {output_dir}")
    print(f"Generation log: {log_path}")
    print("\nReview the proposals before sending!")


if __name__ == '__main__':
    main()

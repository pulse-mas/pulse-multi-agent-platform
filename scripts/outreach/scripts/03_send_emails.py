"""
Email Sender - Send personalized sponsorship outreach emails
Usage: python scripts/03_send_emails.py
"""

import os
import csv
import smtplib
import time
import logging
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configuration
DRY_RUN = os.getenv('DRY_RUN', 'true').lower() == 'true'
DELAY_BETWEEN_EMAILS = int(os.getenv('DELAY_BETWEEN_EMAILS', 180))  # 3 minutes
MAX_EMAILS_PER_DAY = int(os.getenv('MAX_EMAILS_PER_DAY', 50))
SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')


def load_proposals(csv_path: str) -> list:
    """Load generated proposals from CSV."""
    proposals = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            proposals.append(row)
    logger.info(f"Loaded {len(proposals)} proposals to send")
    return proposals


def load_sent_log(log_path: str) -> set:
    """Load previously sent emails to avoid duplicates."""
    sent = set()
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['status'] == 'sent':
                    sent.add(row['email'])
    return sent


def create_email(
    sender_email: str,
    recipient_email: str,
    subject: str,
    html_content: str,
    text_content: str,
    attachment_path: str = None
) -> MIMEMultipart:
    """Create a multipart email with HTML and text versions."""
    msg = MIMEMultipart('alternative')
    msg['From'] = f"Abdelrahman Omar <{sender_email}>"
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Attach text version (fallback)
    part1 = MIMEText(text_content, 'plain', 'utf-8')
    msg.attach(part1)
    
    # Attach HTML version (preferred)
    part2 = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(part2)
    
    # Attach proposal PDF if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(attachment_path)}"'
            )
            msg.attach(part)
    
    return msg


def send_email(msg: MIMEMultipart) -> bool:
    """Send email via SMTP."""
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error: {e}")
        return False


def log_send(log_path: str, entry: dict):
    """Append send result to log file."""
    file_exists = os.path.exists(log_path)
    
    with open(log_path, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['company_name', 'email', 'subject', 'sent_at', 'status', 'error']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(entry)


def preview_email(company_name: str, email: str, html_path: str) -> bool:
    """Show preview and ask for confirmation."""
    print("\n" + "="*60)
    print(f"📧 PREVIEW: Email to {company_name}")
    print("="*60)
    print(f"To: {email}")
    print(f"Subject: Partnership Opportunity: AI-Powered Social Media Platform - Pulse x {company_name}")
    print(f"Content: {html_path}")
    print("="*60)
    
    if DRY_RUN:
        print("🔒 DRY RUN MODE - Email will NOT be sent")
        return True
    
    response = input("\nSend this email? (y/n/q to quit): ").strip().lower()
    return response == 'y'


def main():
    """Main email sending pipeline."""
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proposals_path = os.path.join(base_dir, 'data', 'proposals_generated.csv')
    log_path = os.path.join(base_dir, 'data', 'outreach_log.csv')
    
    # Validate configuration
    if not SMTP_USER or not SMTP_PASSWORD:
        logger.error("SMTP credentials not configured. Set SMTP_USER and SMTP_PASSWORD in .env")
        return
    
    # Load data
    proposals = load_proposals(proposals_path)
    already_sent = load_sent_log(log_path)
    
    # Filter out already sent
    to_send = [p for p in proposals if p['email'] not in already_sent]
    logger.info(f"Emails to send: {len(to_send)} (already sent: {len(already_sent)})")
    
    if not to_send:
        print("No new emails to send!")
        return
    
    # Limit per day
    to_send = to_send[:MAX_EMAILS_PER_DAY]
    
    # Send emails
    sent_count = 0
    failed_count = 0
    
    print(f"\n{'='*60}")
    print(f"EMAIL OUTREACH - {'DRY RUN' if DRY_RUN else 'LIVE MODE'}")
    print(f"{'='*60}")
    print(f"Emails to send: {len(to_send)}")
    print(f"Delay between emails: {DELAY_BETWEEN_EMAILS} seconds")
    
    for i, proposal in enumerate(to_send, 1):
        company_name = proposal['company_name']
        email = proposal['email']
        html_path = proposal['html_path']
        text_path = proposal['text_path']
        
        # Load content
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        with open(text_path, 'r', encoding='utf-8') as f:
            text_content = f.read()
        
        # Preview and confirm
        should_send = preview_email(company_name, email, html_path)
        
        if not should_send:
            logger.info(f"Skipped: {company_name}")
            continue
        
        # Create email
        subject = f"Partnership Opportunity: AI-Powered Social Media Platform - Pulse x {company_name}"
        msg = create_email(
            sender_email=SMTP_USER,
            recipient_email=email,
            subject=subject,
            html_content=html_content,
            text_content=text_content
        )
        
        # Send (or simulate)
        if DRY_RUN:
            logger.info(f"[DRY RUN] Would send to: {email}")
            status = 'dry_run'
            error = None
        else:
            success = send_email(msg)
            if success:
                logger.info(f"✅ Sent to: {email}")
                status = 'sent'
                error = None
                sent_count += 1
            else:
                logger.error(f"❌ Failed to send to: {email}")
                status = 'failed'
                error = 'SMTP error'
                failed_count += 1
        
        # Log result
        log_send(log_path, {
            'company_name': company_name,
            'email': email,
            'subject': subject,
            'sent_at': datetime.now().isoformat(),
            'status': status,
            'error': error
        })
        
        # Rate limiting
        if i < len(to_send) and not DRY_RUN:
            logger.info(f"Waiting {DELAY_BETWEEN_EMAILS} seconds before next email...")
            time.sleep(DELAY_BETWEEN_EMAILS)
    
    # Summary
    print("\n" + "="*60)
    print("SENDING COMPLETE")
    print("="*60)
    print(f"Total processed: {len(to_send)}")
    if not DRY_RUN:
        print(f"Successfully sent: {sent_count}")
        print(f"Failed: {failed_count}")
    else:
        print("DRY RUN - No emails were actually sent")
    print(f"Log saved to: {log_path}")


if __name__ == '__main__':
    main()

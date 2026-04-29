import requests
import smtplib
import os
from email.message import EmailMessage

def send_email(content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = "Daily AI Trends Report"
    msg['From'] = os.environ.get('EMAIL_USER')
    msg['To'] = os.environ.get('EMAIL_RECEIVER')

    # Connect to Gmail's server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
        smtp.send_message(msg)

def run_automation():
    # Fetch top 10 AI repos
    url = "https://api.github.com/search/repositories?q=topic:ai+stars:>1000&sort=stars&order=desc"
    response = requests.get(url)
    repos = response.json().get('items', [])[:10]
    
    report = "Top 10 Trending AI Repositories:\n\n"
    for i, repo in enumerate(repos, 1):
        report += f"{i}. {repo['name']} ({repo['stargazers_count']} stars)\n{repo['html_url']}\n\n"
    
    # Save to Markdown file
    with open("AITrends.md", "w") as f:
        f.write(report)
    
    # Trigger the email function
    send_email(report)

if __name__ == "__main__":
    run_automation()

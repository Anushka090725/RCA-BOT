import smtplib
from email.mime.text import MIMEText
from config import EMAIL_SENDER, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD, DEV_EMAILS

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = ", ".join(DEV_EMAILS)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, SMTP_PASSWORD)
        server.sendmail(EMAIL_SENDER, DEV_EMAILS, msg.as_string())

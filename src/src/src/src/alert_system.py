import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

def send_alert(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

def check_thresholds(data, thresholds):
    alerts = []
    for city, city_data in data.items():
        if city_data['temp'] > thresholds.get('high_temp', float('inf')):
            alerts.append(f"High temperature alert for {city}: {city_data['temp']}°C")
        elif city_data['temp'] < thresholds.get('low_temp', float('-inf')):
            alerts.append(f"Low temperature alert for {city}: {city_data['temp']}°C")
    return alerts

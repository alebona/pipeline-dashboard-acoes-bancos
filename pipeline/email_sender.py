import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("EMAIL_HOST")
SMTP_PORT = int(os.getenv("EMAIL_PORT", 587))
SMTP_USER = os.getenv("EMAIL_HOST_USER")
SMTP_PASS = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_HOST_USER")
EMAIL_TO = os.getenv("EMAIL_TO")


def send_email(subject: str, body: str):
    """Envia email com o log de erro"""
    try:
        msg = MIMEText(body, "plain", "utf-8")
        msg["From"] = formataddr(("Pipeline Logger", EMAIL_FROM))
        msg["To"] = EMAIL_TO
        msg["Subject"] = subject

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")


#send_email("Teste de Email", "Este é um email de teste do pipeline.")
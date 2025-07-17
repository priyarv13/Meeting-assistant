import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = "priyarvishwaroop33.connect@gmail.com"  # ← Replace with your Gmail
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")  # ← .env must have this

def send_task_email(to_email, name, task, date):
    subject = "📝 Task Assigned from Meeting Assistant"
    body = f"""
    Hi {name},

    You have been assigned a task:

    ➤ Task: {task}  
    ➤ Deadline: {date}

    This has been added to your Google Calendar. Please check and confirm.

    Regards,  
    Meeting Assistant Bot
    """

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # ✅ Define server BEFORE using it
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

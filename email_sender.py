import smtplib
from email.mime.text import MIMEText

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

def send_digest(content):

    msg = MIMEText(content)

    msg["Subject"] = "Daily News Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    with smtplib.SMTP("smtp.gmail.com",587) as server:

        server.starttls()

        server.login(
            EMAIL,
            APP_PASSWORD
        )

        server.send_message(msg)

    print("Email sent")
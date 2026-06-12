import schedule
import time

from digest import create_digest
from email_sender import send_digest

def job():

    digest = create_digest()

    send_digest(digest)

schedule.every().day.at("09:00").do(job)

while True:

    schedule.run_pending()

    time.sleep(60)
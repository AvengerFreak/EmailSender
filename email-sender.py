import smtplib
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv('SENDER_PASSWORD') # generate app password in gmail account
sender = os.getenv('SENDER_EMAIL') #gmail you used to generate app password
receiver = os.getenv('RECIPIENT_EMAIL') # email of person or people you want to send message
subject = "My first generated email"
body = "This email was generated in python!"
recipients = [receiver] # add as many recepients here as you'd like


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
    print("email was sent")

#send_email(subject, body, sender, recipients, password)
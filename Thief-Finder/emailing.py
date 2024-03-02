import smtplib
from email.message import EmailMessage

PASSWORD = "mcqw rdae rgkj didh"
SENDER = "shivam.gpt499@gmail.com"
RECEIVER = "shivam.gpt499@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'Thief found'
    email_message.set_content("Hey, we saw a thief found")

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, subtype="png", maintype='image')

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())

    gmail.quit()

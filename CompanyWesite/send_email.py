import smtplib
import ssl


def __init__():
    pass


def send_email(message, receiver):
    username = "shivam.gpt499@gmail.com"
    password = "***********"
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

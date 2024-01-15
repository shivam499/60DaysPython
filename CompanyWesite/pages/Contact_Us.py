import streamlit as gui
import pandas as pd
from send_email import send_email

gui.header("Contact Us")

df = pd.read_csv("topics.csv")

with gui.form(key="contact_form"):
    user_email = gui.text_input("Your email address")
    option = gui.selectbox("What topic do you want to discuss?", df["topic"])
    email_text = gui.text_area("Enter your Message")
    message = f"""\
Subject: Topic {option}
From: {user_email}
Topic {option}
{email_text}
    """
    subject = f"Subject: New email from {user_email}"
    btn_submit = gui.form_submit_button("Submit")
    if btn_submit:
        send_email(message, user_email)
        gui.info("Email sent.")



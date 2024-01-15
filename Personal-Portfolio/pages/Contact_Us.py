import streamlit as gui
from send_email import send_email

gui.header("Contact Us")


with gui.form(key="contact_form"):
    user_email = gui.text_input("Your email address")
    email_text = gui.text_area("Enter your Message")
    message = f"""\
    Subject: New email from {user_email}\
    From: {user_email}\
    {email_text}
    """
    btn_submit = gui.form_submit_button("Submit")
    if btn_submit:
        gui.info(send_email(message, user_email))

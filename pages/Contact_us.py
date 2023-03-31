import streamlit as st
from send_email import send_email



st.set_page_config(layout='wide')

st.title('Contact us')
with st.form(key='Email_form'):
    user_email = st.text_input('Your email address')
    user_topic = st.selectbox(label='What topic would you like to discuss?',
                              options=['Job Inquires', 'Project Proposals', 'Other'])
    user_email_body = st.text_area('Your message')

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {user_topic}

{user_email_body}
    """

    button = st.form_submit_button('Send')
    if button:
        send_email(message)
        st.info('Your email has been sent successfully')

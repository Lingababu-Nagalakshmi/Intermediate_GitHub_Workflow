import smtplib, ssl
import os
import base64


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')

message = """
Subject: GitHub Email report
This is your daily email Report.
"""

# Encode the password in Base64
password_base64 = base64.b64encode(PASSWORD.encode()).decode()

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(USERNAME,password_base64)
    server.sendmail(USERNAME,password_base64,message)

import smtplib, ssl
import os
import base64


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')


print("Username:", USERNAME)
print("Password:", PASSWORD)



message = """
Subject: GitHub Email report
This is your daily email Report.
"""

# Replace with your actual method to get the password

if PASSWORD is not None:
    password_base64 = base64.b64encode(PASSWORD.encode()).decode()
else:
    print("Password is not defined or is None.")


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(USERNAME,password_base64)
    server.sendmail(USERNAME,password_base64,message)

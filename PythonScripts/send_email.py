import smtplib, ssl
import os
import base64


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')

print("Username:", USERNAME)
print("Password:", PASSWORD)

message = '''
Subject: GitHub Email report
This is your daily email Report.
'''


if USERNAME is not None and PASSWORD is not None:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(USERNAME, PASSWORD)
            # Send your email here
        except smtplib.SMTPAuthenticationError as e:
            print("SMTP Authentication Error:", e)
        except Exception as e:
            print("An error occurred:", e)
else:
    print("Username or password is not defined or is None.")




import smtplib
import ssl

USERNAME = "guggilapulingababu1@gmail.com"
# Use the App Password you generated for your application
PASSWORD = "321@NagaLinga"

print("Username:", USERNAME)
print("Password:", PASSWORD)




smtp_server = "smtp.gmail.com"
port = 465  # Google SMTP port


message = '''
Subject: GitHub Email report
This is your daily email Report.
'''
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME,PASSWORD,message)
except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)
except Exception as e:
    print("An error occurred:", e)

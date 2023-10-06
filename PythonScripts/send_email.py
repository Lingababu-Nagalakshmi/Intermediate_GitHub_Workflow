import smtplib
import ssl
import os

#sender_email = os.environ.get('USER_EMAIL')
sender_email = "guggilapulingababu1@gmail.com"
#password = os.environ.get('USER_PASSWORD')
password = "UGFzc3dvcmQ6"



print("sender_email:", sender_email)
print("password:", password)

smtp_server = "smtp.gmail.com"
port = 465  # Google SMTP port
message = "***************Subject: GitHub Email report****************"

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email,password,message)
except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)
except Exception as e:
    print("An error occurred:", e)
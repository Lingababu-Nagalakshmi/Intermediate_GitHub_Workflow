import smtplib
import ssl

USERNAME = "guggilapulingababu1@gmail.com"
PASSWORD = "321@NagaLinga"

smtp_server = "smtp.gmail.com"
port = 465  

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        # Send your email here
except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)
except Exception as e:
    print("An error occurred:", e)
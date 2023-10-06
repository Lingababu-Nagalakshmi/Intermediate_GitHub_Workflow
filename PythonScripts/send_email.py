import smtplib
import base64
import os
import ssl


smtp_server = "smtp.gmail.com"
port = 587  
sender_email = os.environ.get('USER_EMAIL')
password = os.environ.get('USER_PASSWORD')

if password is not None and isinstance(password, str):
    password_base64 = base64.b64encode(password.encode()).decode()
else:
    print("Password is not defined or is not a valid string.")

message = "***************Subject: GitHub Email report****************"
   
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() 
    server.starttls(context=context) 
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email,password,message)
   
except Exception as e:
   
    print(e)
finally:
    server.quit()
    
    




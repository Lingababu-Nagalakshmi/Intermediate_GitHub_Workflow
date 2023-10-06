import smtplib, ssl
import os

smtp_server = "smtp.gmail.com"
port = 587  
# sender_email = "guggilapulingababu1@gmail.com"
# password = "321@NagaLinga"

sender_email = os.environ.get('USER_EMAIL')
password = os.environ.get('USER_PASSWORD')



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
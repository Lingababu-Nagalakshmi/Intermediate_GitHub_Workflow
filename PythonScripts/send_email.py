import smtplib

sender_email ="gowtham.j2012@gmail.com"
password = "hhup fxaq vsdm wkhc"
rec_email = "lingababu987@gmail.com"

message = "Hey this was sent using python"


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls
server.login(sender_email,password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to", rec_email)

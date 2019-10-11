# File Name learn_smtp.py
# Demo of python mail transfer
# link : https://www.tutorialspoint.com/python3/python_sending_email.htm
#!usr/bin/python3

import smtplib

sender = 'developer.mitra85@gmail.com'
receivers = ['mitra.pushan@gmail.com']

message = """From: Pushan Test <%s>
To: My Mail <%s>
Subject: SMTP e-mail test

This is a test e-mail message.
""" % (sender, receivers[0])

print("Message: ", message)
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login("developer.mitra85@gmail.com", "123@Mitra#1")
   smtpObj.sendmail(sender, receivers[0], message)
   smtpObj.close()
   print ("Successfully sent email")
except smtplib.SMTPException as excp:
   print ("Error: unable to send email: ", excp)

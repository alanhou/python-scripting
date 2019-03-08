import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'
port = 465

u_name = 'username/emailid'
password = getpass.getpass()
sender = 'sender_name'
receivers = ['receiver1_email_address', 'receiver2_email_address']

text = MIMEMultipart()
text['Subject'] = 'Test Attachment'
text['From'] = sender
text['To'] = ', '.join(receivers)

txt = MIMEText('sending a sample image.')
text.attach(txt)

f_path = '/home/student/Desktop/mountain.jpg'
with open(f_path, 'rb') as f:
	img = MIMEImage(f.read())

img.add_header('Content-Disposition',
		'attachment',
		filename=os.path.basename(f_path))

text.attach(img)

server = smtplib.SMTP_SSL(host_name, port)
server.login(u_name, password)
server.sendmail(u_name, receivers, text.as_string())
print("Email with attachment sent successfully !!")
server.quit() 

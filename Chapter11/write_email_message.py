import smtplib, getpass

# host_name = 'smtp.gmail.com'
host_name = 'smtp.exmail.qq.com'
# host_name = 'smtp.163.com'
port = 465

sender = '发件人 email'
receiver = '收件人 email'
password = getpass.getpass()

msg = """\
Subject: Test Mail
Hello from Alan !!!"""

s = smtplib.SMTP_SSL(host_name, port)
s.login(sender, password)
s.sendmail(sender, receiver, msg)
s.quit()

print("Mail sent Successfully")

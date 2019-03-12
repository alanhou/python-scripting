import poplib, getpass

# pop3_server = 'pop.gmail.com'
pop3_server = 'pop.exmail.qq.com'
username = 'Email地址'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)

email_stat = email_obj.stat()
NumofMsgs = email_stat[0]
for i in range(NumofMsgs):
	for mail in email_obj.retr(i+1)[1]:
		print(mail)

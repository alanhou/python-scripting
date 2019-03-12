import poplib, getpass

# pop3_server = 'pop.gmail.com'
pop3_server = 'pop.exmail.qq.com'
username = 'Email地址'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)

print("\nLatest Mail\n")
latest_email = email_obj.retr(1)
print(latest_email[1])

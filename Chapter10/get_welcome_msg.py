from ftplib import FTP

ftp = FTP('FTP的域名或 IP 地址')
ftp.login('用户名', '密码')

welcome_msg = ftp.getwelcome()
print(welcome_msg)

ftp.close()

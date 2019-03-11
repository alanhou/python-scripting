from ftplib import FTP

ftp = FTP('FTP服务器域名或 IP 地址')
ftp.login('用户名', '密码')

ftp.cwd('/home/student')
s_cmd_stat = ftp.sendcmd('STAT')
print(s_cmd_stat)
print()

s_cmd_pwd = ftp.sendcmd('PWD')
print(s_cmd_pwd)
print()

ftp.close()

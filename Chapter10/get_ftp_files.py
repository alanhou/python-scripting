mport os
from ftplib import FTP

ftp = FTP('FTP域名或IP')
with ftp:
        ftp.login('用户名', '密码')
        ftp.cwd('/home/student/work/')
        files = ftp.nlst()
        print(files)

        # 打印文件
        for file in files:
                print("Downloading..." + file)
                ftp.retrbinary("RETR " + file, open("/home/student/testing/" + file, 'wb').write)

ftp.close()

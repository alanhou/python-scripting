import paramiko, time

ip_address = '主机 IP'
usr = '主机用户名'
pwd = '主机密码'

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=ip_address, username=usr, password=pwd)

print("SSH connection is successfully established with ", ip_address)

rc = c.invoke_shell()
for n in range(2, 6):
	print("Creating VLAN " + str(n))
	rc.send("vlan database\n")
	rc.send("vlan " + str(n) + "\n")
	rc.send("exit\n")
	time.sleep(0.5)

time.sleep(1)
output = rc.recv(65535)
print(output)
c.close()

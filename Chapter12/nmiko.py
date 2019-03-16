from netmiko import ConnectHandler

remote_device = {
	'device_type': 'cisco_ios',
	'ip': '远程设备 IP地址',
	'username': '用户名',
	'password': '密码'
}

remote_connection = ConnectHandler(**remote_device)
# net_connect.find_prompt()

for n in range(2, 6)
	print("Creating VLAN " + str(n))
	commands = ['exit', 'vlan database', 'vlan ' + str(n), 'exit')
	output = remote_connection.send_config_set(commands)
	print(output)

command = remote_connection.send_command('show vlan-switch brief')
print(command)

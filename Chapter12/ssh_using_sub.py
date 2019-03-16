import subprocess, sys

HOST="主机用户名@主机 IP"
COMMAND = "ls"

ssh_obj = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	shell=False,
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE)

result = ssh_obj.stdout.readlines()
if result = []:
	err = ssh_obj.stderr.readlines()
	print(sys.stderr, "ERROR: %s" % err)
else:
	print(result)

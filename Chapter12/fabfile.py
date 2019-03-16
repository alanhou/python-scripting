from fabric.api import *

env.hosts = ["用户名@主机ip"]
env.password = '你的密码'

def dir():
	run('mkdir fabric')
	print('Directory named fabric has been created on your host network')

def diskspace():
	run('df')

import sys
import time
import paramiko 
import os
import cmd
import datetime

#set date and time
now = datetime.datetime.now()

#authentication
HOST = '192.168.100.1'
USER = 'user'
PASSWORD = 'password'
secret = 'password'

#prefix files for backup
filename_prefix ='cisco-backup'

#ssh session starts
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, username=USER, password=PASSWORD)

#ssh shell
chan = client.invoke_shell()
time.sleep(1)
#enter enable secret
chan.send('en\n')
chan.send(secret +'\n')
time.sleep(1)
#terminal lenght for no paging 
chan.send('term len 0\n')
time.sleep(1)
#show config and write output
chan.send('sh run\n')
time.sleep(10)
output = chan.recv(99999)
#show output config and write file with prefix, date and time
print output
filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
f = open(filename, 'a')
f.write(output)
f.close()
#close ssh session
client.close()
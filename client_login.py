import time
from paramiko import SSHClient
from scp import SCPClient
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('server_ip',username="username",password="password") # connect to the scp endpoint
scp = SCPClient(ssh.get_transport())
username=input("Enter your username : ")
pword=input("Enter your password : ")
with open(r"C:\Users\cswil\Desktop\hashprog\creds\client_login.txt","w") as f:
    f.write(username + "\n"+pword) # things to send
    f.close()
scp.put(r'C:\Users\cswil\Desktop\hashprog\creds\client_login.txt', recursive=True, remote_path='/home/nemo/hashit/sends') # sends the file through scp 
scp.close()
while 1:
    with open(r"C:\Users\cswil\Desktop\hashprog\creds\resp.txt","r") as f:
        txt=f.read()
    time.sleep(10) # make sure the file is closed so it can be written to 
    print(txt)
    if txt!="":
        f.close()
        break
    else:
        f.close()
if txt[0:4]=="true": # server returns true or false
    print("succesful login")
elif txt[0:5]=="false":
    print("inorrect")
else:
    print("there was some sort of invalid response ?")

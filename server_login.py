 
import hashlib, sqlite3, string, random, subprocess
conn =sqlite3.connect("main.db")
c = conn.cursor()

# get the id of the salt
def getid(myuser):
    c.execute("""SELECT pword FROM tbl_users WHERE uname = ?""",(myuser,))
    salt_id=c.fetchone()
    print(salt_id)
    salt_id=str(salt_id[0])[32::]
    print(salt_id)
    return salt_id

# get the actual password
def getreal(myuser):
    c.execute("""SELECT pword FROM tbl_users WHERE uname = ?""",(myuser,))
    real_pass=c.fetchone()
    real_pass=str(real_pass[0])
    return real_pass

# get the true value of the hash
def hash(pword,uname):
    myid=getid(uname)
    c.execute('''SELECT salt FROM tbl_salts WHERE saltid = ?''',(myid,))
    salt=str(c.fetchall())[3:-4]
    tot = salt+pword
    result = hashlib.md5(tot.encode('utf-8'))
    return str(result.hexdigest()) + str(myid)

# gets username and pass to use for hashing
with open(r"/home/nemo/hashit/sends/credits.txt","r") as f:
    all = f.read().split()
    username=all[0]
    pword=all[1]
    f.close()

# checks if correct login
if str(getreal(username)) == str(hash(pword,username)):
    with open("sends/resp.txt","w") as f:
        f.write("true")
        f.close()
else:
    with open("sends/resp.txt","w") as f:
        f.write("false")
        f.close()
p = subprocess.Popen(["scp","sends/resp.txt", "username@ip:location"]) # sends it off scp wouldnt work to go to windows machine for some reason so here we are
sts=os.waitpid(p.pid,0)

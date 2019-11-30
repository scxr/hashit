import hashlib, sqlite3, string, random
conn =sqlite3.connect("main.db")
c = conn.cursor()
# make the tables needed
def create_users_table():
    c.execute('''CREATE TABLE IF NOT EXISTS tbl_users (userid INTEGER PRIMARY KEY, uname TEXT NOT NULL, pword TEXT NOT NULL);''')
    conn.commit()
def register_user(uname,pword):
    c.execute('''INSERT INTO tbl_users VALUES (null,?,?)''',(uname,pword))
    conn.commit()
def create_salts_table():
    c.execute('''CREATE TABLE IF NOT EXISTS tbl_salts (saltid INTEGER PRIMARY KEY, salt TEXT NOT NULL);''')
    conn.commit()
# make the salts 
def create_salts():
    salt=''
    for i in range(16):
        salt+=random.choice(string.ascii_letters)
    c.execute('''INSERT INTO tbl_salts VALUES (null,?)''',(salt,))
    conn.commit()
def gettotal():
    c.execute('''SELECT * FROM tbl_salts''')
    conn.commit()
    r=c.fetchall()
    return len(r)
def cr_tables():
    create_users_table()
    create_salts_table()

#hash the password 
def hash(pword):
    tot1 = int(gettotal())
    num = random.randint(0,tot1)
    c.execute('''SELECT salt FROM tbl_salts WHERE saltid = ?''',(num,))
    salt=str(c.fetchall())[4:-4]
    print(len(salt))
    print(num)
    tot = salt+pword
    print(tot)
    result = hashlib.md5(tot.encode('utf-8'))
    return str(result.hexdigest()) + str(num)
with open("/home/nemo/hashit/sends/credits.txt","r") as f:
    all = f.read().split()
    username=all[0]
    pword=all[1]
if __name__ == "__main__":
    cr_tables()
    print(hash(pword))
    register_user(username,hash(pword))


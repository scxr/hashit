# hashit!

hashit is a new idea for securer login systems than pgp encyrption which is what we use today

## Installation

You need to have a local client (your home pc) and then another server, for my POC is used a RaspberryPI 3. On both these machines you need to enable SSH. If you are on windows I will have a powershell script that allows SSH on your windows pc because i personally found it a pain to setup manually however on linux its simple so you can just google it.

```bash
pip3 install paramiko
pip3 install scp
```

## Usage

You need to install the modules paramiko and scp, as scp is what i used for file transfer, i just found it easier to implement than sftp/ftp or others. This is purely a proof of concept project, there are security issues with it that i am aware of and when i have the time i will fix (for eg the credits.txt file needs to be erased as soon as is read). The main focus of this code though is the hash.py script.

In the scripts you will need to put your ssh username and password into the different files.

For a full run through of the script you do: client_register.py which will send your credentials to the server, then on the server you run server_hash.py, then on the client you use client_login.py to send a login request to the server then on the server you run server_login.py that will return whether you have the correct credentials.

## What it does

The program uses two databases. A database of salts and then the users database. What it does is it takes the password, generates a random number which will correspond to a salt id, the salt is then prefixed to the password and then hashed. The salt id is then appended to the hash and stored as the password.
When logging in the client sends the login details, the username is searched for and then the hash is found. The program gets the salt id from this by taking the digits after the 32nd one (as of course all MD5s are 32 in length) then the request password has the salt put at the front then is hashed, then the salt id is appended. If the request hash is equal to the actual then the true is returned and allowed to login, if it isnt then false is returned.

## Why i think it is better than pgp

I think it is better as hash is 1 way, they are impossible to be reversed, the only way they are cracked is by generating other hashes and seeing if its equal. This is fair enough to be cracked when someone has a password of password1 as it will be easily generated, but who is going to be able to guess kdjshUidjKolPsjkpassword1 ? nobody.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
I will update as and when i have time, all contribs are appreciated.
Please make sure to update tests as appropriate.

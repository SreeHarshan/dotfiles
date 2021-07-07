#!/usr/bin/python3
import time,vlc,subprocess
from pynput import keyboard

alt = False

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
#media = vlc_instance.media_new("../Music/Anime/06_-_.mp3")
#player.set_media(media)
#player.play()
#time.sleep(100)
keys= [
     keyboard.KeyCode(char='x')
]

def execute():
    activity_no = subprocess.Popen(['qdbus','org.kde.ActivityManager','/ActivityManager/Activities','org.kde.ActivityManager.Activities.CurrentActivity'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = activity_no.communicate()
    ac = str(stdout).replace('b','')
    ac = ac.replace("'",'')
    ac = ac[0:-2]
    print(ac)

def on_press(key):
    global alt
    if key == keyboard.Key.alt:
        alt = True
    if alt and key in keys:
        execute()

def on_release(key):
    global alt
    if key == keyboard.Key.alt:
        alt = False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()





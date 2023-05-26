import webbrowser,time,pyautogui,random,tkinter as tk,psutil, win32process, win32gui,pyttsx3,threading
from datetime import datetime

#---------------------------------
#FREDRIC the class joiner for xi-c
#---------------------------------
#By Sree Harshan


#win check
def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
    return (psutil.Process(pid[-1]).name()) #pid[-1] is the most likely to survive last longer

#Init
engine = pyttsx3.init()
engine.setProperty('rate', 210)

d = {
    "Monday":
        {
            1:"cs",2:"che",3:"math",4:"phy",5:"cs",6:"che"
        },
    "Tuesday":
    {
            1:"phy",2:"phy",3:"che",4:"eng",5:"math",6:"math"
    },
    "Wednesday":
    {
            1:"math",2:"eng",3:"cs",4:"che",5:"phy",6:"che"
    },
    "Thursday":
    {
            1: "phy", 2: "cs", 3: "che", 4: "math", 5: "phy", 6: "phy"
    },
    "Friday":
    {
            1: "math", 2: "math", 3: "eng", 4: "che", 5: "cs", 6: "circle_time"
    },
    "Saturday":
    {
            1: "math", 2: "che", 3: "che", 4: "math", 5: "phy"
    }
}

classes = {
    "phy":"physics",
    "math":"math",
    "che":"chemistry",
    "cs":"computer",
    "eng":"english"
}

#Timestamps
stamps = {
    ("08","20"):1,
    ("09","20"):2,
    ("10","20"):3,
    ("11","20"):4,
    ("12","20"):5,
    ("14","00"):6,
}
periodstamps = {
    1:("08","20"),
    2:("09","20"),
    3:("10","20"),
    4:("11","20"),
    5:("12","20"),
    6:("14","00"),
}

joined = {
    1:False,
    2:False,
    3:False,
    4:False,
    5:False,
    6:False,
    7:False
}

#Speak
def say(str):
    engine.say(str)
    engine.runAndWait()

#Scale value
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
scalex = screen_width/1920
scaley = screen_height/1080

#Check screen pixels
def check_pixels(x1,x2,y1,y2,r,g,b):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if not pyautogui.pixelMatchesColor(x, y, (r, g, b)):
                return False
            else:
                return True
    return True

#Join
def join(ctime):

    webbrowser.open(link[tt[stamps[ctime]]])
    time.sleep(9)
    while active_window_process_name() != "chrome.exe":
        pyautogui.hotkey('alt','tab')
        time.sleep(2)
    pyautogui.click(600*scalex, 310*scaley)#Goto meet
    time.sleep(12)

    while True:               #Check is class is available
        if not check_pixels(int(250*scalex),int(1100*scalex),int(350*scaley),int(550*scaley),255,255,255):
            break
        pyautogui.press('f5')
        time.sleep(9)

    pyautogui.hotkey('ctrl', 'e')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'd') #Mute
    time.sleep(2)
    pyautogui.click(1350*scalex,600*scaley)#Join
    time.sleep(1)
    pyautogui.doubleClick()#Fullscreen

#Day
day = datetime.today().strftime('%A')
tt = d[day]

#Links
link = {
    "eng":"https://classroom.google.com/u/1/c/MTAzNDIyNjIxMjU2",
    "phy":"https://classroom.google.com/u/1/c/MTMyODAzMDY2MzMz",
    "math":"https://classroom.google.com/u/1/c/MTMyODE4Mzk1Mjg3",
    "che":"https://classroom.google.com/u/1/c/MTMyODE4Mzk1MjQz",
    "cs":"https://classroom.google.com/u/1/c/MTMyNTMyNTExNTI0"
}

#Welcome
def BufferPrinter(strs):
    for str in strs:
        print(str, end="")
        time.sleep(0.1)
    print()

def BufferPrint(str):
    processThread = threading.Thread(target=BufferPrinter, args=(str,))
    processThread.start()

def sleep(str):
    time.sleep(len(str)*0.07)


print("-----------------------")
BufferPrinter("Class Joiner aka Fredric")
print("-----------------------")
BufferPrinter("by Sree Harshan")
print()
r = random.randint(1,4)
if r == 1:
    BufferPrint("Hey")
    say("hey")
    sleep("hey")
elif r == 2:
    BufferPrint("Hi")
    say("hi")
    sleep("hi")
elif r == 3:
    BufferPrint("How's it going?")
    say("how's it going")
    sleep("how's it going")
else:
    BufferPrint("Sup")
    say("Sup")
    sleep("sup")
BufferPrint("It seems today is "+day)
say("It seems today is "+day)
sleep("It seems today is "+day)
print(tt)
BufferPrint("And that is today's timetable")
say("And that is today's timetable")
sleep("And that is today's timetable")

#Period
period = 1
now = datetime.now()
ctime = ( now.strftime("%H"),now.strftime("%M") )

for i in range(1,8):
    c = periodstamps[i]
    if ctime[0] < c[0]:
        period = i
        break
    elif ctime[0] == c[0] and ctime[1] <= c[1]:
        period = i
        break
else:
    period = 8
    BufferPrint("Bruh there is no classes left")
    say("Bruh there is no classes left")
    sleep("Bruh there is no classes left")
    BufferPrint("Why did u open me")
    say("Why did you open me")
    sleep("Why did u open me")
    BufferPrint("I'm leaving.Bye")
    say("I'm leaving bye")
    sleep("I'm leaving.Bye")
    exit(0)

#Loop
while True:

    now = datetime.now()
    ctime = ( now.strftime("%H"),now.strftime("%M") )
    if ctime in stamps.keys() and not joined[stamps[ctime]]:
        BufferPrint("Joining " + tt[stamps[ctime]] + " class")
        say("Joining " + classes[tt[stamps[ctime]]] + " class")
        sleep("Joining " + tt[stamps[ctime]] + " class")
        joined[stamps[ctime]] = True
        join(ctime)
        period += 1
    else:
        if period != 8:
            hrs_left = str(int(periodstamps[period][0]) - int(ctime[0]))
            min_left = ""
            if int(periodstamps[period][1]) > int(ctime[1]):
                min_left = str(int(periodstamps[period][1]) - int(ctime[1]))
            else:
                hrs_left = str(int(hrs_left)-1)
                min_left = str(60 - (int(ctime[1]) - int(periodstamps[period][1])))
            secs_left = str(60-int(now.strftime("%S")))
            min_left =str(int(min_left)-1)
            BufferPrint("Joining "+tt[stamps[periodstamps[period]]]+" class in "+hrs_left+":"+min_left+":"+secs_left)
            if int(hrs_left) == 0 and int(min_left) < 5:
                say("Joining "+classes[tt[stamps[periodstamps[period]]]]+" class in "+min_left+" minutes "+secs_left+"seconds")
                sleep("Joining "+tt[stamps[periodstamps[period]]]+" class in "+hrs_left+":"+min_left+":"+secs_left)
        else:
            r = random.randint(1,3)
            if r == 1:
                BufferPrint("No more classes today :)")
                say("No more classes today")
                sleep("No more classes today :)")
            elif r == 2:
                BufferPrint("Yes classes are over")
                say("Yes classes are over")
                sleep("Yes classes are over")
            elif r == 3:
                BufferPrint("Good news classes are over")
                say("Good news classes are over")
                sleep("Good news classes are over")

            r = random.randint(1,4)
            if r == 1:
                BufferPrint("Good Bye!")
                say("Good Bye")
                sleep("Good Bye!")
            elif r == 2:
                BufferPrint("C ya afterwards")
                say("See ya afterwards")
                sleep("C ya afterwards")
            elif r == 3:
                BufferPrint("I'm gonna sleep")
                say("I'm gonna sleep")
                sleep("I'm gonna sleep")
                BufferPrint("Please don't restart this computer")
                say("Please don't restart this computer")
                sleep("Please don't restart this computer")
                time.sleep(1)
                BufferPrinter("Please")
                say("Please")
                sleep("Please")
            elif r == 4:
                BufferPrint("Eyyy time up.Bye")
                say("Heey time up bye")
                sleep("Eyyy time up.Bye")
            time.sleep(3)
            exit(0)
    time.sleep(20)

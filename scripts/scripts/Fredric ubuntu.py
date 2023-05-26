
from tkinter import *
from datetime import datetime
import subprocess#,pyttsx3



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
            1: "math", 2: "che", 3: "che", 4: "math", 5: "phy",6:"None"
    }
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

periodstamps = [
    ("08","20"),
    ("09","20"),
    ("10","20"),
    ("11","20"),
    ("12","20"),
    ("14","00")
]

#Links
link = {
    "eng":"https://classroom.google.com/u/1/c/MTA0Mzc2MTE0NjQ1",
    "phy":"https://classroom.google.com/u/1/c/MTMyODAzMDY2MzMz",
    "math":"https://classroom.google.com/u/1/c/MTMyODE4Mzk1Mjg3",
    "che":"https://classroom.google.com/u/1/c/MTMyODE4Mzk1MjQz",
    "cs":"https://classroom.google.com/u/1/c/MTMyNTMyNTExNTI0"
}

#GLOBAL VARS
#engine = pyttsx3.init()
p1 = p2 = p3 = "None"
day = datetime.today().strftime('%A')

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
def join():

    pyautogui.click(600*scalex, 310*scaley)#Goto meet
    time.sleep(12)

    while True:               #Check is class is available
        if not check_pixels(int(250*scalex),int(1100*scalex),int(350*scaley),int(550*scaley),255,255,255):
            break
        pyautogui.press('f5')
        time.sleep(10)

    pyautogui.hotkey('ctrl', 'e')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'd') #Mute
    time.sleep(2)
    pyautogui.click(1350*scalex,600*scaley)#Join


def prev():
    if p1 != "None":
        test = subprocess.Popen(["google-chrome", link[p1]], stdout=subprocess.PIPE)

def cur():
    if p2 != "None":
        test = subprocess.Popen(["google-chrome", link[p2]], stdout=subprocess.PIPE)

def next():
    if p3 != "None":
        test = subprocess.Popen(["google-chrome", link[p3]], stdout=subprocess.PIPE)


def loop():
    global p1,p2,p3
    display1.delete(0.0, END)
    display2.delete(0.0, END)
    display3.delete(0.0, END)

    #get the time
    now = datetime.now()
    ctime = (now.strftime("%H"), now.strftime("%M"))
    ch,cm = (int(now.strftime("%H")), int(now.strftime("%M")))

    #calculate period
    s = ""
    for i in range( len(periodstamps) ):
        h = int(periodstamps[i][0])
        if ch <= h:
            m = int(periodstamps[i][1])
            if cm <= m:
                # c period is -1
                # next p is this
                # p period is -2
                p1 = i - 2
                p2 = i - 1
                p3 = i
                if m - cm == 0:
                    subprocess.Popen(['notify-send', "Join class"])
                    #engine.say("Join class")
                    #engine.runAndWait()

            else:
                # c period is this
                # next p is +1
                # p period is -1
                p1 = i - 1
                p2 = i
                p3 = i + 1

            break
    else:
        display1.insert(END, "No")
        display2.insert(END, "class")
        display3.insert(END, ":)")
        return

    if int(p1) >= 0:
        p1 = d[day][stamps[periodstamps[p1]]]
    else:
        p1 = "None"

    if int(p2) >= 0:
        p2 = d[day][stamps[periodstamps[p2]]]
    else:
        p2 = "None"

    if p3 < len(periodstamps):
        p3 = periodstamps[p3]
        p3 = stamps[p3]
        p3 = d[day][p3]
    else:
        p3 = "None"

    #print it
    display1.insert(END, p1)
    display2.insert(END, p2)
    display3.insert(END, p3)
    
    main.after(45000, loop)


main = Tk()
main.title("Fredric")
main.minsize(200,100)
main.maxsize(200,100)
main.configure(background = "black")
main.geometry("200x100+800+300")

t = Label(main,text = "Class Joiner",bg = "black",fg = "white")
t.grid(row = 0,column = 1)

Label(main,text = "           ",bg = "black").grid(row = 0,column = 0)

display1 = Text(main, width = 7, height = 1, wrap = WORD, background ="black", foreground ="white")
display1.grid(row = 3, column = 0)
display2 = Text(main, width = 7, height = 1, wrap = WORD, background ="black", foreground ="white")
display2.grid(row = 3, column = 1)
display3 = Text(main, width = 7, height = 1, wrap = WORD, background ="black", foreground ="white")
display3.grid(row = 3, column = 2)

Button(main,text = "PREV",width = 4,command = prev).grid(row = 4,column = 0)
Button(main,text = "JOIN",width = 4,command = cur).grid(row = 4,column = 1)
Button(main,text = "NEXT",width = 4,command = next).grid(row = 4,column = 2)

loop()
main.after(45000,loop)
main.mainloop()

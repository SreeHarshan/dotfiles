import json,pickle

d = {}
d2 = {}
staffabs = {}
staffabs["MONDAY"] = []

print("                            ---- ----- -------                                  ")
print("                            TIME TABLE PROGRAM                                  ")
print("                            ---- ----- -------                                  ")

print("ENTER STAFF DETAILS")

def TT():
    name = input("     ENTER STAFF NAME:-")
    d2[name] = {}
    d2[name]["MONDAY"] = {}
    a = input("PRESS a IF YOU WANT ADD MORE:-")
    if a == "a":
        TT()
f1 = open("d.dat","rb")
f2 = open("d2.dat","rb")
while True:
	try:	
		d = pickle.load(f1)
	except EOFError:
		break
while True:
	try:	
		d2 = pickle.load(f2)
	except EOFError:
		break
f1.close()
f2.close()
if len(d2.keys()) <= 0:
	TT()

while True:
    print("1)ADD NEW SECTION")
    print("2)ADD NEW DAY")
    print("3)PRINT TIME TABLE FOR STUDENTS")
    print("4)PRINT TIME TABLE FOR STAFF")
    print("5)MODIFY TIMETABLE FOR ABSENT STAFF")
    print("6)ASSIGN PERIOD TO STAFF")
    print("7)QUIT")
    
    inp = input()
    
    if inp == "1":
        section = input("ENTER SECTION NAME:")
        d[section] = {}
        
        print("NEW SECTION IS CREATED")
        print("ADD MONDAY'S PERIOD FOR THIS SECTION")
        d[section]["MONDAY"] = {}
        for i in range(1,10):
            print("ENTER STAFF NAME FOR PERIOD",i,":",end = "")
            sname = input()
            d[section]["MONDAY"][i] = sname
            d2[sname]["MONDAY"][i] = section
        
    elif inp == "2":
        day = input("ENTER DAY NAME:")
        for section in d:
            d[section][day] = {}
            staffabs[day] = []
            for i in d2:
                d2[i][day] = {}
            print("ENTER PERIOD FOR",section,"SECTION")
            for i in range(1,10):
                print("ENTER STAFF NAME FOR PERIOD",i,":",end = "")
                sname = input()
                d[section][day][i] = sname
                d2[sname][day][i] = section
        print("NEW DAY IS CREATED")

    elif inp == "3":
        section = input("ENTER SECTION:")
        day = input("ENTER DAY(leave blank space for all days):")
        if day == "":
            for i in d[section]:
                print(i,end = "  ")
                print(json.dumps(d[section][i],indent = 2))
                print()
        else:
            print(json.dumps(d[section][day],indent = 2))
        
            
    elif inp == "4":
        sname = input("ENTER STAFF NAME:")
        day = input("ENTER DAY(leave blank space for all days):")
        if day == "":
            for i in d2[sname]:
                print(i,end = "  ")
                print(json.dumps(d2[sname][i],indent = 2))
                print()
        else:
            print(json.dumps(d2[sname][day],indent = 2))

    elif inp == "5":   
        absstaff = input("ENTER STAFF WHO IS ABSENT:")
        day = input("WHICH DAY HE/SHE ABSENT:")
        staffabs[day].append(absstaff)
        toremove = []
        for i in d2[absstaff][day]:
            p = {}
            mincount = 0
            selectedp = ""
            for j in d2:
                if j not in staffabs[day]:
                    if i not in d2[j][day].keys():
                        p[j] =  len(d2[j][day].keys())
                        mincount = p[j]
            
            for j in p:
                if p[j] <= mincount:
                    mincount = p[j]
                    selectedp = j


            if selectedp == "":
                print("NOBODY HAS ANY PERIOD TO COME")
            else:
                d2[selectedp][day][i] = d2[absstaff][day][i]
                d[d2[selectedp][day][i]][day][i] = selectedp
                print(selectedp,"IS GOING TO COME FOR",d2[absstaff][day][i]," SECTION IN PERIOD ",i)
                toremove.append(i)
                
        for i in toremove:
            d2[absstaff][day].pop(i)
        d2[absstaff][day] = ''
    elif inp == "6":
        sname = input("ENTER STAFF NAME:")
        section = input("ENTER SECTION:")
        day = input("ENTER DAY:")
        pnum = input("ENTER PERIOD NUMBER:")
        if pnum not in d[section][day]:
            if pnum not in d2[sname][day]:
                d[section][day][pnum] = sname
                d2[sname][day][pnum] = section
            else:
                inp = input("THE TEACHER IS TAKING AN OTHER PERIOD FOR ANOTHER CLASS.Overwrite(Y/N)")
                if inp == "Y":
                    d[section][day][pnum] = sname
                    d2[sname][day][pnum] = section
        else:
            inp = input("PERIOD ALREADY EXIST IN CLASS.Overwrite(Y/N)")
            if inp == "Y":
                d2[d[section][day][pnum]][day].pop(pnum)
                d[section][day][pnum] = sname
                d2[sname][day][pnum] = section
                
                
    elif inp == "7":
        a = input("Press y if you want to save the timetable:")
        if a == 'y':
            f1 = open("d.dat","wb")
            f2 = open("d2.dat","wb")
            pickle.dump(d,f1)
            pickle.dump(d2,f2)
            f1.close()
            f2.close()
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("THANK YOU FOR USING THE PROGRAM")
        break
    
    else:
        print("INVALID INPUT")

    print()

        
        
        


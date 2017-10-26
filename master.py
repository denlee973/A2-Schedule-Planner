# Denise Lee
# master.py
# Created 19 October 2017
# Schedule Planner for CS 12 A2
import datetime

def user():
    name = raw_input("username: ")
    return name
    
def update_data(files):
    try:
        f = open(files+'.txt')
    except:
        data = []
    else:
        data = f.readlines()
        f.close()
    return data

def tryexc(do,max):
    trying = True
    while trying:
        try:
            answer = input(do)
        except:
            print "Please input a numerical value."
        else:
            if answer > 25:
                print "Please input a value less than {}.".format(max)
            else:
                trying = False
    return answer

def p_date():
    from datetime import date
    import calendar 
    now = datetime.datetime.now()
    weekday = date.today().weekday()
    nmonth = now.month
    nday = now.day
    print "~~~~~~~~~~ {}, {} {}, {} ~~~~~~~~~~".format(calendar.day_name[weekday],calendar.month_name[nmonth],nday,now.year)
    return weekday,nmonth,nday

def school_blocks():
    school = raw_input("What school do you go to? ")
    if school != "Havergal" and school != "Havergal College" and school != "havergal" and school != "havergal college" and school != "HC" and school != "hc":
        days = tryexc("How many days are in your schedule? ",25)
        print days
        
        periods = tryexc("How many periods are in a day? (If it is not evenly divided by time, please input the common denominator of times.)",25)
        print periods
        
        blocks = tryexc("How many courses do you have? ",25)
        print blocks

    else:
        school = "Havergal"
        days = 8
        blocks = 8
        periods = 4
    
    return school, days, blocks, periods

def in_schedule(school, days, blocks, periods): 
    schedule = []
    for i in range(days):
        schedule.append([0]*periods)
    print "Please input your courses in the order that they occur."
    f = open('schedule.txt','a')
    for k in range(blocks):
        course = raw_input("What is block #{}? ".format(k+1))
        f.write(course+'\n')
    info = ["S: "+str(school),"D: "+str(days),"B: "+str(blocks),"P: "+str(periods)]
    for r in range(len(info)):
        f.write(info[r]+'\t')

    f.close()
    
def late_start():
    late = raw_input("Is today a 9:20 or 9:30 schedule? ")
    twenty = False
    thirty = False
    if late.find("20") >= 0 or late.find("twenty") >= 0:
        twenty = True
    elif late.find("30") >= 0 or late.find("thirty") >= 0:
        thirty = True

    return twenty, thirty
    
def g_schedule(data,school):
    if school == "Havergal":
        a = data[0][0:len(data[0])-1]
        b = data[1][0:len(data[1])-1]
        c = data[2][0:len(data[2])-1]
        d = data[3][0:len(data[3])-1]
        e = data[4][0:len(data[4])-1]
        f = data[5][0:len(data[5])-1]
        g = data[6][0:len(data[6])-1]
        h = data[7][0:len(data[7])-1]
        
        schedule = [[a,b,c,d],[e,f,g,h],[c,d,a,b],[g,h,e,f],[b,a,d,c],[f,e,h,g],[d,c,b,a],[h,g,f,e]]
        return schedule
    else:
        print "Sorry, the schedule for your school is not yet supported."
        
def p_schedule(data,schedule,):
    tabs = [1,1,1,1,1,1,1,1]
    for e in range(8):
        if len(data[e]) > 10:
            tabs[e] += 2
        elif len(data[e]) > 5:
            tabs[e] += 1
    print tabs
    print " -=+=- SCHEDULE -=+=- "
    print "Day 1"+"\t"*3+"Day 2"+"\t"*3+"Day 3"+"\t"*3+"Day 4"
    for j in range(4):
        for k in range(4):
            if len(schedule[k][j]) < 8:
                print schedule[k][j] +'\t'*3,
            elif len(schedule[k][j]) >= 8 and len(schedule[k][j]) <= 10:
                print schedule[k][j] +'\t'*2,
            else:
                print schedule[k][j]+'\t',
        print ""
    print ""
    print "Day 5"+"\t"*3+"Day 6"+"\t"*3+"Day 7"+"\t"*3+"Day 8"
    for j in range(4):
        for k in range(4):
            if len(schedule[k+4][j]) < 8:
                print schedule[k+4][j] +'\t'*3,
            elif len(schedule[k+4][j]) >= 8 and len(schedule[k+4][j]) <= 10:
                print schedule[k+4][j] +'\t'*2,
            else:
                print schedule[k+4][j]+'\t',
        print ""
    print ""
        
def today(data,schedule,weekday,nmonth,nday):
    times = []
    classes = []
    first = 1
    weekday = 2
    # day = tryexc("What day of the schedule is it today? ",9)
    day = abs(weekday - first)
    day9 = False
    latewed = False
    sdata = update_data("special_schedules")
    for i in range(len(sdata)):
        new = sdata[i].split('\\t')
        for k in range(len(new)):
            sdate = new[k].split('.')
            try:
                sdate[0] = int(sdate[0])
                sdate[1] = int(sdate[1])
            except:
                pass
            else:
                if sdate[0] == nmonth and sdate[1] == nday:
                    if i == 0:
                        day9 = True
                    elif i == 1:
                        latewed = True
    
    now = datetime.datetime.now()
    if day9 == False:
        if weekday == 2:
            if latewed:
                print "It is a late Wednesday schedule."
                times = ["9:20am","10:20am","10:30am","11:30am","12:30pm","1:30pm","1:40pm","2:40pm"]
            else:
                times = ["8:20am","9:30am","9:55am","11:05am","12:10pm","1:20pm","1:30pm","2:40pm"]
            classes = [schedule[day][0],"Break",schedule[day][1],"Lunch",schedule[day][2],"Break",schedule[day][3]]
        elif weekday != 5 and weekday != 6:
            if now.hour >= 9:
                twenty, thirty = late_start()
                if twenty:
                    times = ["9:20am","10:30am","10:55am","12:05pm","1:00pm","2:10pm","2:20pm","3:30pm"]
                elif thirty:
                    times = ["9:30am","10:40am","10:50am","12:00pm","1:00pm","2:10pm","2:20pm","3:30pm"]
                else:
                    times = ["8:20am","8:30am","9:00am","9:10am","10:20am","10:45am","11:55am","1:00pm","2:10pm","2:20pm","3:30pm"]
            else:
                times = ["8:20am","8:30am","9:00am","9:10am","10:20am","10:45am","11:55am","1:00pm","2:10pm","2:20pm","3:30pm"]
            classes = ["TA Attendance","Prayers/House/Assembly","Break",schedule[day][0],"Break",schedule[day][1],"Lunch",schedule[day][2],"Break",schedule[day][3]]
        else:
            print "There is no school."
        for f in range(len(times)*2-2):
            try:
                timing = times[f]+" - "+times[f+1]
                if len(timing) < 16:
                    print timing+"\t"*2,
                else:
                    print timing+"\t",
                print classes[f]+'\n' 
            except:
                pass
    else:
        print "It is a Day 9 schedule. Have fun!"

        

        
def main():
    quit = False
    name = user()
    data = update_data(name)
    if len(data) >= 8:
        info = data[len(data)-1].split('\t')
        if info[0] == "S: Havergal":
            school = "Havergal"
        else:
            school = "Other"
    else:
        print "User not found."
        ans = raw_input("Would you like to create a new account? ")
        if ans.find("Y") >= 0 or ans.find("y") >= 0:
            school, days, blocks, periods = school_blocks()
            in_schedule(school,days,blocks,periods)
        else:
            quit = True
    if quit == False:
        print "\n"*50
        weekday,nmonth,nday = p_date()
        print "\n"
        data = update_data(name)
        schedule = g_schedule(data,school)
        while quit == False:
            call = raw_input("What would you me like to do? ")
            if call.find("help") >= 0 or call.find("can") >= 0:
                print "I can print out your schedule, give you the times for your classes today,\nand tell you what times you have for tomorrow.\nSimply type what you would like me to do.\n"
            elif call.find("today") >= 0 or call.find("Today") >= 0:
                print "1"
                today(data,schedule,weekday,nmonth,nday)
            elif call.find("schedule") >= 0 or call.find("table") >= 0:
                print'2'
                p_schedule(data,schedule)
            elif call.find("tomorrow") >= 0 or call.find("Tomorrow") >= 0:
                print "3"
                today(data,schedule,weekday+1,nmonth,nday)
            
            elif call.find("credits")  >= 0 or call.find("Credits") >= 0 or call.find("who") >= 0 or call.find("cool") >= 0:
                print "Made by Denise Lee\nComSci 12 - A2\nOctober 26, 2017\n"
            elif call.find("quit") >= 0 or call.find("Quit") >= 0 or call.find("stop") >= 0 or call.find("Stop") >= 0:
                print "4"
                quit = True
            else:
                print "Sorry, I can't do that. Try something else?"



main()

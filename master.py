# Denise Lee
# master.py
# Created 19 October 2017
# Schedule Planner for CS 12 A2
import datetime

def user():
    print "\t\t-=+=- Havergal Planner 2017/18 -=+=-"
    name = raw_input("username: ")
    return name
    
def update_data(files,split,by):
    try:
        f = open(files+'.txt')
    except:
        data = []
    else:
        data = f.readlines()
        f.close()
        if split == 0:
            return data
        else:
            for w in range(split):
                sdata = split_data(data,by)
            return sdata
def split_data(data,by):
    sdata = []
    ndata = []
    if len(by) == 2:
        for k in range(len(data)):
            new = data[k].split(by[0])
            for p in range(len(new)):
                new[p] = new[p].split(by[1])
            ndata.append(new)
        sdata.append(ndata)
    elif len(by) == 1:
        for t in range(len(data)):
            new = data[t].split(by[0])
            sdata.append(new)
    return sdata

def change_data(files,lines):
    try:
        f = open(files+'.txt',"a")
    except:
        data = []
    else:
        for i in range(len(lines)):
            f.write(lines[i]+'\n')
        f.close()
        

def tryexc(do,max):
    trying = True
    while trying:
        try:
            answer = input(do)
        except:
            print "Please input a numerical value."
        else:
            if answer > 25:
                print "Please input a value less than {}.".format(str(max))
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
    nweek = datetime.date.today().isocalendar()[1]
    print nweek
    print "~~~~~~~~~~ {}, {} {}, {} ~~~~~~~~~~".format(calendar.day_name[weekday],calendar.month_name[nmonth],nday,now.year)
    return weekday,nmonth,nday,nweek

def start():
    quit = False
    name = user()
    data = update_data(name,0,"")
    if len(data) >= 8:
        info = data[len(data)-1].split('\t')
        if info[0] == "S: Havergal":
            school = "Havergal"
        else:
            school = "Other"
    if len(data) < 8:
        print "User not found."
        ans = ""
        while len(ans) < 1:
            ans = raw_input("Would you like to create a new account? ")
            if len(ans) < 1:
                print "Please input an answer."
                continue
            if ans.find("Y") >= 0 or ans.find("y") >= 0:
                f = open(name+'.txt','w+')
                school, days, blocks, periods = school_blocks()
                in_schedule(name,school,days,blocks,periods)
            elif ans.find("N") >= 0 or ans.find("n") >= 0:
                quit = True
            else:
                print "Please input an answer."
                ans = ""
    if quit == False:
        print "\n"*50
        weekday,nmonth,nday,nweek = p_date()
        print "\n"
        schedule = g_schedule(data,school)
    return quit,name,school,weekday,nmonth,nday,nweek,schedule

def school_blocks():
    school = raw_input("What school do you go to? ")
    if school != "Havergal" and school != "Havergal College" and school != "havergal" and school != "havergal college" and school != "HC" and school != "hc" and school != "Hc":
        days = tryexc("How many days are in your schedule? ",25)
        
        periods = tryexc("How many periods are in a day? (If it is not evenly divided by time, please input the common denominator of times.)",25)
        
        blocks = tryexc("How many courses do you have? ",25)

    else:
        school = "Havergal"
        days = 8
        blocks = 8
        periods = 4
    
    return school, days, blocks, periods

def in_schedule(name,school, days, blocks, periods): 
    schedule = []
    for i in range(days):
        schedule.append([0]*periods)
    print "Please input your courses in the order that they occur."
    f = open(name+'.txt','a')
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
    print "\n -=+=- SCHEDULE -=+=- "
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

def special_schedule(sdata,num,nmonth,nday):
    special_day = False
    for k in range(len(sdata[0][num])):
        sdate = sdata[0][num][k]
        if k != 0:
            sdate[0] = int(sdate[0])
            sdate[1] = int(sdate[1])
            if sdate[0] == nmonth and sdate[1] == nday:
                special_day = True
                print ":D"
    return special_day
        
def today(schedule,weekday,nmonth,nday,nweek,tomorrow):
    times = []
    classes = []
    sdata = update_data("dates",2,["\t","."])
    best = [0,0]
    weekend = False
    print nday
    if tomorrow:
        if (nmonth == 2 and nday == 28) or ((nmonth == 1 or nmonth == 3 or nmonth == 5 or nmonth == 7 or nmonth == 8 or nmonth == 10 or nmonth == 12) and nday == 31) or ((nmonth == 4 or nmonth == 6 or nmonth == 9 or nmonth == 11) and nday == 30):
            nmonth += 1
            nday = 1
            print nmonth,
            print nday
        else:
            nday += 1
        weekday += 1
        if weekday > 6:
            weekday -= 6
    
    day9 = special_schedule(sdata,0,nmonth,nday)
    latewed = special_schedule(sdata,1,nmonth,nday)
    no_school = special_schedule(sdata,2,nmonth,nday)
    
    for r in range(len(sdata[0][3])):
        try:
            
            if int(sdata[0][3][r][0]) == int(nmonth) and int(sdata[0][3][r][1]) < int(nday) and int(sdata[0][3][r][1]) > int(best[1]):
                best[0] = int(sdata[0][3][r][0])
                best[1] = int(sdata[0][3][r][1])
            elif int(sdata[0][3][r][0])-1 == int(nmonth) and int(sdata[0][3][r][1]) < int(nday) and int(sdata[0][3][r][1]) > int(best[1]):
                best[0] = int(sdata[0][3][r][0])
                best[1] = int(sdata[0][3][r][1])

        except:
            pass
    print best
    if best[0] >= 9:
        first = datetime.date(2017,best[0],best[1]).weekday()
        if int(nweek) != datetime.date(2017,best[0],best[1]).isocalendar()[1]:
            weekend = True
            day = int(weekday)-int(first)+6 # technically end weekday + (7(ie. days in a week so that it's not negative)-2(for the weekend) - start weekday + 1(just because)
        else:
            day = int(weekday)-int(first)+1 # doesn't need the +(7-5) because it's the same week
    else:
        first = datetime.date(2018,best[0],best[1]).isoweekday()
        if nweek == datetime.date(2018,best[0],best[1]).isocalendar()[1]:
            weekend = True
            day = int(first)-int(weekday)+6 # technically end weekday + (7(ie. days in a week so that it's not negative)-2(for the weekend) - start weekday + 1(just because)
        else:
            day = int(weekday)-int(first)+1 # doesn't need the +(7-5) because it's the same week
    day9 = special_schedule(sdata,0,nmonth,nday)
    latewed = special_schedule(sdata,1,nmonth,nday)
    no_school = special_schedule(sdata,2,nmonth,nday)
    past = 0
    if weekend:
        for p in range(day+2):
            nschool_past = False
            if nday-p < 1:
                if nmonth-1 == 2:
                    nschool_past = special_schedule(sdata,2,nmonth-1,nday-p+28)
                elif nmonth-1 == 1 or nmonth-1 == 3 or nmonth-1 == 5 or nmonth-1 == 7 or nmonth-1 == 8 or nmonth-1 == 10 or nmonth-1 == 12:
                    nschool_past = special_schedule(sdata,2,nmonth-1,nday-p+31)
                else:
                    nschool_past = special_schedule(sdata,2,nmonth-1,nday-p+30)

            else:
                nschool_past = special_schedule(sdata,2,nmonth,nday-p)
                print nschool_past
            if nschool_past:
                past += 1
    else:
        for p in range(day):
            nschool_past = False
            if nday-p < 1:
                if nmonth-1 == 2:
                    nschool_past = special_schedule(sdata,2,nmonth-1,nday-p+28)
                elif nmonth-1 == 1 or nmonth-1 == 3 or nmonth-1 == 5 or nmonth-1 == 7 or nmonth-1 == 8 or nmonth-1 == 10 or nmonth-1 == 12:
                    nschool_past = special_schedule(sdata,2,nmonth-1,nday-p+31)
                else:
                    nschool_past = special_schedule(sdata,2,nmonth-1,nday-p+30)

            else:
                nschool_past = special_schedule(sdata,2,nmonth,nday-p)
            if nschool_past:
                past += 1
    if past >=5:
        for p in range(day+2):
            nschool_past = special_schedule(sdata,2,nmonth,nday-p)
            if nschool_past:
                past += 1
        if past > 8:
            past -= 8
    print past
    day -= past
    print day
    
    now = datetime.datetime.now()
    if day9 == False:
        if weekday == 2:
            if latewed:
                print "It is a late Wednesday schedule."
                times = ["9:20am","10:20am","10:30am","11:30am","12:30pm","1:30pm","1:40pm","2:40pm"]
            else:
                times = ["8:20am","9:30am","9:55am","11:05am","12:10pm","1:20pm","1:30pm","2:40pm"]
            print day
            classes = [schedule[day-1][0],"Break",schedule[day-1][1],"Lunch",schedule[day-1][2],"Break",schedule[day-1][3]]
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
            print day
            classes = ["TA Attendance","Prayers/House/Assembly","Break",schedule[day-1][0],"Break",schedule[day-1][1],"Lunch",schedule[day-1][2],"Break",schedule[day-1][3]]
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
        # print "\nNot day {}? Type \"edit\" followed by \"day\".".format(day)
    else:
        print "It is a Day 9 schedule. Have fun!"
    print '\n'


# def edit(name,schedule):
#     change = raw_input("What would you like to edit? (block/note/times/special schedule)")
#     # data = update_data(name,True)
# 
#     if change.find("switch") >= 0 or change.find("schedule") >= 0:
#         which = tryexc("What block would you like to change? ",len(data)-1)
#         data[which][0] = raw_input("What would you like to rename this block to? ")
#         change_data(name,data)
    

        
def main():
    quit,name,school,weekday,nmonth,nday,nweek,schedule = start()
    while quit == False:
        data = update_data(name,0,[])
        call = raw_input("What would you me like to do? (schedule/today/tomorrow/log out/credits/quit) ")
        
        if call.find("schedule") >= 0 or call.find("table") >= 0:
            p_schedule(data,schedule)
        
        elif call.find("today") >= 0 or call.find("Today") >= 0:
            print "\nToday's schedule is : \n"
            today(schedule,weekday,nmonth,nday,nweek,False)
            
        elif call.find("tomorrow") >= 0 or call.find("Tomorrow") >= 0:
            print "\nTomorrow's schedule is: \n"
            today(schedule,weekday,nmonth,nday,nweek,True)
        
        elif call.find("credits") >= 0 or call.find("Credits") >= 0 or call.find("who") >= 0 or call.find("cool") >= 0:
            print "\nMade by Denise Lee\nComSci 12 - A2\nOctober 31, 2017\n"
        
        elif call.find("log") >= 0 or call.find("Log") >= 0 or call.find("out") >= 0 or call.find("Out") >= 0:
            print "\n"*50
            print "\nSuccessfully logged out.\n\n"
            quit,name,school,weekday,nmonth,nday,nweek,schedule = start()
            
        elif call.find("quit") >= 0 or call.find("Quit") >= 0 or call.find("stop") >= 0 or call.find("Stop") >= 0:
            quit = True
            
        else:
            print "Sorry, I can't do that. Try something else?"
            print "I can print out your schedule, give you the times for your classes today,\nand tell you what times you have for tomorrow.\nSimply type what you would like me to do.\n"




main()

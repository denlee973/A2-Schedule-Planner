# Denise Lee
# master.py
# Created 19 October 2017
# Schedule Planner for CS 12 A2
import datetime


def update_data():
    f = open('schedule.txt')
    data = f.readlines()
    f.close()
    return data
data = update_data()

def tryexc(do):
    trying = True
    while trying:
        try:
            answer = input(do)
        except:
            print "Please input a numerical value."
        else:
            if answer > 25:
                print "Please input a value less than 25."
            else:
                trying = False
    return answer

def date():
    from datetime import date
    import calendar
    now = datetime.datetime.now()
    weekday = calendar.day_name[date.today().weekday()]
    print "~~~~~~~~~~ {}, {} {}, {} ~~~~~~~~~~".format(weekday,calendar.month_name[now.month],now.day,now.year)
    return weekday

def school_blocks():
    school = raw_input("What school do you go to? ")
    if school != "Havergal" and school != "Havergal College" and school != "havergal" and school != "havergal college" and school != "HC" and school != "hc":
        days = tryexc("How many days are in your schedule? ")
        print days
        
        periods = tryexc("How many periods are in a day? (If it is not evenly divided by time, please input the common denominator of times.)")
        print periods
        
        blocks = tryexc("How many courses do you have? ")
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
    
def p_schedule(data,school):
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
        
        tabs = [1,1,1,1,1,1,1,1]
        for e in range(8):
            if len(data[e]) > 10:
                tabs[e] += 2
            elif len(data[e]) > 5:
                tabs[e] += 1
        print tabs
        print "-=+=- SCHEDULE -=+=-"
        print "Day 1\tDay 2\tDay 3\tDay 4\tDay 5\tDay 6\tDay 7\tDay 8"
        for j in range(4):
            for k in range(8):
                print schedule[k][j] +'\t',
            print ""
        print ""
    else:
        print "Sorry, the schedule for your school is not yet supported."
def main(data):
    if len(data) >= 8:
        print "Schedule found."
        info = data[len(data)-1].split('\t')
        if info[0] == "S: Havergal":
            school = "Havergal"
        else:
            school = "Other"
    else:
        print "Need to input schedule."
        school, days, blocks, periods = school_blocks()
        in_schedule(school,days,blocks,periods)
    print "\n"*50
    weekday = date()
    print "\n"
    data = update_data()
    p_schedule(data,school)


main(data)

# Denise Lee
# master.py
# Created 19 October 2017
# Schedule Planner for CS 12 A2

def update_data():
    f = open('schedule.txt')
    data = f.readlines()
    f.close()
    return data
data = update_data()

def tryexc(value,do,wrong):
    trying = True
    while trying:
        try:
            if value == "int" or value == "float":
                answer = input(do)
            elif value == "str":
                answer = raw_input(do)
        except:
            print wrong
        else:
            trying = False
    return answer
def school_blocks():
    school = raw_input("What school do you go to? ")
    if school != "Havergal" and school != "Havergal College" and school != "havergal" and school != "havergal college" and school != "HC" and school != "hc":
        days = tryexc("int","How many days are in your schedule? ","Please input a numerical value.")
        while days > 50:
            print "Please input a value less than 50."
            days = tryexc("int","How many days are in your schedule? ","Please input a numerical value.")
        print days
        
        periods = tryexc("int","How many periods are in a day? ","Please input a numerical value.")
        while periods > 50:
            print "Please input a value less than 50."
            periods = tryexc("int","How many periods are in a day? (If it is not evenly divided by time, please input the common denominator of times.) ","Please input a numerical value.")
        print periods
        
        blocks = tryexc("int","How many courses do you have? ","Please input a numerical value.")
        while blocks > 50:
            print "Please input a value less than 50."
            blocks = tryexc("int","How many courses do you have? ","Please input a numerical value.")
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
    print schedule
    f = open('schedule.txt','a')
    for k in range(blocks):
        course = raw_input("What is block #{}? ".format(k+1))
        f.write(course+'\n')
    info = ["S: "+str(school),"D: "+str(days),"B: "+str(blocks),"P: "+str(periods)]
    for r in range(len(info)):
        f.write(info[r]+'\t')

    f.close()
def main(data):
    print data
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
        
    data = update_data()
    for i in range(len(data)):
        dat = data[i]
        dat = dat[0:len(dat)-1]
        print dat,
    print ""
    print school
    if school == "Havergal":
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]
        e = data[4]
        f = data[5]
        g = data[6]
        h = data[7]
        tabs = [1,1,1,1,1,1,1,1]
        # for e in range(8):
        #     if len(data[e]) > 8:
        #         tabs[e] += 1
        schedule = [[a,b,c,d],[e,f,g,h],[c,d,a,b],[g,h,e,f],[b,a,d,c],[f,e,h,g],[d,c,b,a],[h,g,f,e]]
        print "Day 1\tDay 2\tDay 3\tDay 4\tDay 5\tDay 6\tDay 7\tDay 8"
        for j in range(4):
            for k in range(8):
                course = schedule[k][j]
                print course[0:len(course)-1]+'\t',
            print ""

main(data)
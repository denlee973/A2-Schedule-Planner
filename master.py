# Denise Lee
# master.py
# Created 19 October 2017
# Schedule Planner for CS 12 A2

f = open('schedule.txt','w+')

data = f.readlines()
if len(data) >= 4:
    print "Schedule found."

else:
    print "Need to input schedule."
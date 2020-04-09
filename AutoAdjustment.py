import string
import os
import sys

#login verfication Portal

def login_Verification(username,password):
    Password=open("LoginID.txt",'r')
    Login=False
    for i in Password:
        str1=i.rstrip()#returns a copy of strings in which all chars are have been stripped
        temppassword=str1.split()
        if len(temppassword)==0:
            continue
        if(username==temppassword[1] and password==temppassword[3]):
            Login=True
    return Login


#Starting Portal
print("\n\n***************Leave Allocation portal********************\n\n")
n=3
while(n):
    username=input("Enter username: \n")
    password=input("Enter the password: \n")
    if login_Verification(username,password):
        os.system('cls' if os.name == 'nt' else 'clear')# 'nt' means that you are running windows
        break
    else:
        print("Wrong username or password\n")
        n=n-1
        print("Trial Left : ",n)
if(n==0):
    print("This portal is Locked Retry after some Time\n\n")
    sys.exit()

#Main interface
print("\n\n**************Faculty LEAVE REQUEST PORTAL*****************\n")
print("                  Welcome!.{}".format(username))
schedule=open("STUDENTTB//K18KH.txt",'r')
timeTable=[]
for i in schedule:
    print(i)
    tempTimeTable=i.split()
    if len(tempTimeTable)==0 or tempTimeTable[0] not in ['MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY']:
        continue
    timetable.append(tempTimeTable)
schedule.close()

print("\n ********{} Time Table for K18KH***********\n".format(username))

file=open("STUDENTTB//{}.txt".format(username),'r')
for i in file:
    print(i)        
    
#Day for leave    
Day=input("Enter leave day (like TUESDAY): ")

#finding timeSlots for adjustment
TimeSlots=[]
fh=open("STUDENTTB//{}.txt".format(username),'r')
for k in fh:
    tempArr=k.split()
    if len(tempArr)==0:
        continue
    if tempArr[0]==Day:
        TimeSlots=[z for z,val in enumerate(tempArr) if val==username]
fh.close()

#finding available teachers for adjustment
Teachers=['Sarbodaya','Tanveer','Manish','Sai_Pavan','Teacher']
TeacherAvailable=[]
for i in Teachers:
    if i==username:
        continue
    fh=open("Faculty_Timetable//{}.txt".format(i),'r')
    for k in fh:
        tempArr=k.split()
        if len(tempArr)==0:
            continue
        if tempArr[0]==Day:
            for p in TimeSlots:
                if tempArr[p]=='B':
                    TeacherAvailable.append([tempArr.count('O'),p,i])
    fh.close()
#Check for any left timeSlots
count=0
for x in TimeSlots:
    for i in TeacherAvailable:
        if i[1]==x:
            count+=1
            break
if len(TeacherAvailable)==0:
    print("No Teachers available for adjustment")
    print("Cannot apply for leave")
    sys.exit()
elif count!=len(TimeSlots): 
    print("No Teachers available for adjustment for some lectures")
    print("Cannot apply for leave")
    sys.exit()

#Choose Teacher for adjustment according to less workload on teacher that day
TimeSlotsDic={1:'9-10',2:'10-11',3:'11-12',4:'12-1',5:'1-2',6:'2-3',7:'3-4',8:'4-5'}
TeacherAssigned=[]
for i in TimeSlots:
    workload=[]
    for t in TeacherAvailable:
        if t[1]==i:
            workload.append([t[0],t[1],t[2]])
    workload.sort(reverse=True)
    TeacherAssigned.append([workload[0][1],workload[0][2]])
    print("\nTeacher for Adjustments for {0} slot from {1} with least Workload: ".format(Day,TimeSlotsDic[i]),workload[0][2])

#change the timetable
TeacherAssigned.sort()
schedule=open("STUDENTTB//K18KH.txt",'r')
leave=open("STUDENTTB//LEAVE.txt", 'w')
for i in schedule:
    if Day in i:
        if len(TeacherAssigned)==1:
            line=i.replace(username,TeacherAssigned[0][1],1)
            leave.write(line)
            continue
        elif len(TeacherAssigned)==2:
            line=i.replace(username,TeacherAssigned[0][1],1).replace(username,TeacherAssigned[1][1],1)
            leave.write(line)
            continue
    leave.write(i)
schedule.close()   
leave.close()

#print adjusted timetable
print("\n\n\t\t\t\t\t\t\t\t\tAdjusted time table")
leave=open("STUDENTTB//LEAVE.txt", 'r')
for i in leave:
    print(i)
leave.close()

print("\n\n\t\t\t\t\t\t\t\t\t\tAdjustement Successful")




        
    

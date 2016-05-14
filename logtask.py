#!/usr/bin/python3
from datetime import date,datetime
import os

print("===================== Log My Task ====================\n\n");

tasktitle = input("What you workign on ? : ");
time = input("How long it took [ HH:MM , default hr. ] ? : ");
status = input("Task status : ");
note = input("Any Note ? : ");



client_name="Densimple"; # change ur client name here 

d=date.today()
filename = client_name+"_"+d.strftime("%B_%Y")+".csv" #("%d/%m/%y")
t= datetime.now()
timestamp = t.strftime("%H:%M:%S")

# open file with write and append mode
fp = open(filename,"a+");

no_of_line = len(list(open(filename))) #number of line in a file
if no_of_line==0:
	header = "Serial No,Task Name,Time Taken,Status,Note,Log Time\n"
	fp.write(header);

insertdata = str(no_of_line+1)+","+tasktitle+","+time+" hr(s),"+status+","+note+","+timestamp+"\n"
fp.write(insertdata);
fp.close();
print("\n\nDone!")
print("\n\nSheet Updated. File Location "+os.path.abspath(filename)+"\n\n");

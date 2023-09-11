import csv
import sys

#Second command line argument is name of origianl csv file to be cleaned.
filename = sys.argv[1]
fieldname_input = sys.argv[2]
new_rows = []
with open(filename+".csv", newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    fieldnames = csvreader.fieldnames
    for line in csvreader:
        #retrieve the date-time text.
        dateval = line[fieldname_input]  #this line is edited for each different file
        year_val, time_val, suffix = dateval.split(" ")
        month, day, year = year_val.split("/")
        hour, minute, second = time_val.split(":")
        if int(day) < 10:
            day = "0" + day
        if int(month) < 10:
            month = "0" + month
        #print(year,month,day,time_val,suffix)  to check correct parsing
        if suffix == "PM" and hour == "12":
            hour = "00"
        if suffix == "PM" and hour in {"10","11"}:
            hour = str(int(hour) + 12)
        if suffix == "PM" and hour in {"1","2","3","4","5","6","7","8","9"}:
            hour = str(int(hour) + 12)
        if suffix == "AM" and hour in {"1","2","3","4","5","6","7","8","9"}:
            hour = "0" + str(int(hour))
        if suffix == "AM" and hour == "12":
            hour = "00"
        line[fieldname_input] = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second #this line is edited for each different file
        new_rows.append(line)
#Now, write lines to new file, with updated time values.
newfilename = filename+"updated"
n = len(new_rows)
with open(newfilename+".csv", "w", newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    for i in range(n):
        csvwriter.writerow(new_rows[i])


        

#raw source file.
f = open("Results.txt", "r")

#save each line into a list; ignore blank lines.
lines = []
for line in f:
    if line != "\n":
        lines.append(line[:-1])

#primary key
place = [i+1 for i in range(len(lines)//9)]
#extract other fields of interest
name = lines[slice(1,len(lines)+1,9)]
sexAge = lines[slice(2,len(lines)+1,9)]
sex = [entry[0] for entry in sexAge]
age = [entry[2:4] for entry in sexAge]
time = lines[slice(8,len(lines)+1,9)]

f.close()

#check that each field list is the same length.
print(len(place),len(name),len(sex),len(age),len(time))

#save output.
with open("Results_Cleaned.csv", "w") as output:
    output.write("place,name,sex,age,time\n")
    for i in range(len(time)):
        output.write(",".join([str(place[i]),name[i],sex[i],age[i],time[i]]))
        output.write("\n")
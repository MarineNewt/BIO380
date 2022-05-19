#! /usr/bin/env python3

##This File will open a sorted data text file to get data related to the graph that we intend to create.
##It will then further sort that data into an organized and readable format in the form of a text file, a bar graph, and a pie chart which will be sent to an output folder for ease of export.
## This file takes no arguments and only has one prompted input requesting the name of the file to be analyzed. The ending of the file (.txt) does not need to be included.

#import matplot lib for plot creation. 
import matplotlib.pyplot as plt

#Take user input to determine text file to be analyzed.
ffile = input("\nEnter filename to analyze:")
#Create a variable with the filename/location of both input and output.
InFileName = ffile+".txt"
OutFileName = "./output/output.txt"

#Create and open a file object for reading 'r', and writing 'w'
InFile = open(InFileName, "r")
OutFile = open(OutFileName, "w")

#Initialize line counter and value storages.
linenum = 0
one = 0
two = 0
three = 0
four = 0
negone = 0
negtwo = 0
negthree = 0
negfour = 0

#Read teh file line by line, if any answer compares to a value raise the counts of that value by 1
for line in InFile:
    #if statement to avoid the first line header
    if (linenum > 0):
        if line.strip() == "1":
            one = one + 1
        if line.strip() == "2":
            two = two + 1
        if line.strip() == "3":
            three = three + 1
        if line.strip() == "4":
            four = four + 1
        if line.strip() == "-1":
            negone = negone + 1
        if line.strip() == "-2":
            negtwo = negtwo + 1
        if line.strip() == "-3":
            negthree = negthree + 1
        if line.strip() == "-4":
            negfour = negfour + 1
    # increments LineNumber by 1
    linenum += 1

#Create and write outsring with grouped values.
OutString = "%s\n\n1:%s\n2:%s\n3:%s\n4:%s\n-1:%s\n-2:%s\n-3:%s\n-4:%s" % (ffile, one, two, three, four, negone, negtwo, negthree, negfour)
OutFile.write(OutString)

#Change values into porportions of the whole (linenum)
perone = one/(linenum-1)
pertwo = two/(linenum-1)
perthree = three/(linenum-1)
perfour = four/(linenum-1)
pernegone = negone/(linenum-1)
pernegtwo = negtwo/(linenum-1)
pernegthree = negthree/(linenum-1)
pernegfour = negfour/(linenum-1)
#Create and write outstring with values as porportions.
OutString = "\n\n\n1:%s\n2:%s\n3:%s\n4:%s\n-1:%s\n-2:%s\n-3:%s\n-4:%s" % (perone, pertwo, perthree, perfour, pernegone, pernegtwo, pernegthree, pernegfour)
OutFile.write(OutString)

# always close an open file!  
InFile.close()
OutFile.close()

#Init x and y axis variables for graphs along with the pie chart's percent data.
xAxis = []
yAxis = []
sliceData = []

#If the value of a stored varaible is greater than 0 the varaible name, and values are added to the graph variables
if four > 0:
    xAxis.append('4')
    yAxis.append(four)
    sliceData.append(perfour)
if three > 0:
    xAxis.append('3')
    yAxis.append(three)
    sliceData.append(perthree)
if two > 0:
    xAxis.append('2')
    yAxis.append(two)
    sliceData.append(pertwo)
if one > 0:
    xAxis.append('1')
    yAxis.append(one)
    sliceData.append(perone)
if negone > 0:
    xAxis.append('-1')
    yAxis.append(negone)
    sliceData.append(pernegone)
if negtwo > 0:
    xAxis.append('-2')
    yAxis.append(negtwo)
    sliceData.append(pernegtwo)
if negthree > 0:
    xAxis.append('-3')
    yAxis.append(negthree)
    sliceData.append(pernegthree)
if negfour > 0:
    xAxis.append('-4')
    yAxis.append(negfour)
    sliceData.append(pernegfour)

#xAxis = ['4','3','2','1','-1','-2','-3','-4']
#yAxis = [four, three, two, one, negone, negtwo, negthree, negfour]
#Creates bar graph and saves it to the output folder.
plt.bar(xAxis,yAxis)
plt.title("Non-Voter Responses to " + ffile)
plt.ylabel('Count')
plt.xlabel('Response')
plt.savefig('./output/outbar.png')
#Clear matplotlib graph
plt.clf()

#sliceData = [perfour, perthree, pertwo, perone, pernegone, pernegtwo, pernegthree, pernegfour]
#Creates pie chart and saves it to output folder.
plt.pie(sliceData, labels=xAxis, autopct='%1.1f%%')
plt.title("Non-Voter Responses to " + ffile)
plt.axis('equal')
plt.savefig('./output/outpie.png')

#Updates user to let them know the program is finished.
print("Output Complete")

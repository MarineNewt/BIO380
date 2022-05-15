#! /usr/bin/env python3

##This File will call the appropriate files to get data related to the graph that we intend to create.
## Then produce graphs to best represent that data to asnwer our target questions.

import matplotlib.pyplot as plt

ffile = input("\nEnter filename to analyze:")
#Create a variable with the filename/location
InFileName = ffile+".txt"
OutFileName = "./output/output.txt"

#Create and open a file object for reading 'r'
InFile = open(InFileName, "r")
OutFile = open(OutFileName, "w")
#Initialize a line number variable set to zero
# when python reads a file, each line is read as a string
linenum = 0

one = 0
two = 0
three = 0
four = 0
negone = 0
negtwo = 0
negthree = 0
negfour = 0



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
  #      OutString = "%s" % (line) 
  #     OutFile.write(OutString)
    # increments LineNumber by 1
    linenum += 1
OutString = "1:%s\n2:%s\n3:%s\n4:%s\n-1:%s\n-2:%s\n-3:%s\n-4:%s" % (one, two, three, four, negone, negtwo, negthree, negfour)
OutFile.write(OutString)

perone = one/(linenum-1)
pertwo = two/(linenum-1)
perthree = three/(linenum-1)
perfour = four/(linenum-1)
pernegone = negone/(linenum-1)
pernegtwo = negtwo/(linenum-1)
pernegthree = negthree/(linenum-1)
pernegfour = negfour/(linenum-1)
OutString = "\n\n\n1:%s\n2:%s\n3:%s\n4:%s\n-1:%s\n-2:%s\n-3:%s\n-4:%s" % (perone, pertwo, perthree, perfour, pernegone, pernegtwo, pernegthree, pernegfour)
OutFile.write(OutString)

# always close an open file!  
InFile.close()
OutFile.close()
xAxis = []
yAxis = []
sliceData = []
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
plt.bar(xAxis,yAxis)
plt.title("Non-Voter Responses to " + ffile)
plt.ylabel('Count')
plt.xlabel('Response')
plt.savefig('./output/outbar.png')
plt.clf()

#sliceData = [perfour, perthree, pertwo, perone, pernegone, pernegtwo, pernegthree, pernegfour]
plt.pie(sliceData, labels=xAxis, autopct='%1.1f%%')
plt.title("Non-Voter Responses to " + ffile)
plt.axis('equal')
plt.savefig('./output/outpie.png')
plt.show()

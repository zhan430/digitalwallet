import functions as fc
import csv
import sys

# Since we run script using run.sh, here we don't need to check
# command-line arguments. 
g = fc.Create(sys.argv[1])

f1 = open(sys.argv[3], "w+")
f2 = open(sys.argv[4], "w+")
f3 = open(sys.argv[5], "w+")

stream = open(sys.argv[2],"r")
line = stream.readline()
while line:
	line = stream.readline()
	row = line.split(',')
	if len(row) < 5:
		continue
	u1, u2 = row[1].strip(), row[2].strip()	
	if u1.isdigit() and u2.isdigit():
		fc.WriteToOutput(f1,f2,f3,fc.get_degree(u1,u2,g))

stream.close()
f1.close()
f2.close()
f3.close()

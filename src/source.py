import functions as fc
import csv
import sys

# Since we run script using run.sh, here we don't need to check
# command-line arguments. 
g = fc.Create(sys.argv[1])

f1 = open(sys.argv[3], "w+")
f2 = open(sys.argv[4], "w+")
f3 = open(sys.argv[5], "w+")

with open(sys.argv[2],"rU") as csvfile:
	reader = csv.reader(csvfile, skipinitialspace = True)
	csv.field_size_limit(sys.maxsize)
	reader.next()
	for row in reader:
		if len(row) < 5:
			continue
		if row[1].isdigit() and row[2].isdigit():
			fc.WriteToOutput(f1,f2,f3,fc.get_degree(row[1],row[2],g))
f1.close()
f2.close()
f3.close()

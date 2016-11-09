import create_graph as cg
import csv
import sys
import os

user_network = cg.User_Network(sys.argv[1])
# user_network = cg.User_Network(os.path.join(os.path.dirname(__file__),sys.argv[1]))
g = user_network.Create()
f1 = open(sys.argv[3], "wb")
f2 = open(sys.argv[4], "wb")
f3 = open(sys.argv[5], "wb")
# with open("data.csv","rU") as csvfile:
with open(sys.argv[2],"rU") as csvfile:
	reader = csv.reader(csvfile, skipinitialspace = True)
	csv.field_size_limit(sys.maxsize)
	reader.next()
	for row in reader:
		if len(row) < 5:
			continue
		cg.WriteToOutput(f1,f2,f3,cg.get_degree(row[1],row[2],g))
f1.close()
f2.close()
f3.close()

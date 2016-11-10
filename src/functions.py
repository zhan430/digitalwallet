import networkx as nx 
import csv
import sys

def Create(filename):
	g = nx.Graph()
	with open(filename, 'rU') as csvfile:
		reader = csv.reader(csvfile, skipinitialspace = True)
		csv.field_size_limit(sys.maxsize)
		reader.next()
		for row in reader:
			if len(row) < 5:
				continue
			g.add_edge(row[1],row[2])
	return g

def get_degree(user1, user2,graph):
	if graph.has_node(user1) and graph.has_node(user2):
		return nx.shortest_path_length(graph, user1, user2)
	else:
		graph.add_edge(user1,user2)
		return 0

def WriteToOutput(f1,f2,f3,degree):
	if degree == 1:
		f1.write("trusted\n")
		f2.write("trusted\n")
		f3.write("trusted\n")
	elif degree == 2:
		f1.write("unverified\n")
		f2.write("trusted\n")
		f3.write("trusted\n")
	elif degree == 3 or degree == 4:
		f1.write("unverified\n")
		f2.write("unverified\n")
		f3.write("trusted\n")
	else:
		f1.write("unverified\n")
		f2.write("unverified\n")
		f3.write("unverified\n")

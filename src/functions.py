import networkx as nx 
import csv
import sys

def Create(filename):
	"""
	Input: filename -> batch_payment.csv file path (str)
	Output: g (nx.Graph)
	Function: Generate a user network graph according to the 
			  records in batch_payment.csv
	"""
	g = nx.Graph()
	with open(filename, 'rU') as csvfile:
		reader = csv.reader(csvfile, skipinitialspace = True)
		csv.field_size_limit(sys.maxsize)
		reader.next()
		for row in reader:
			# Check invalid line. Just in case.
			if len(row) < 5:
				continue
			# Check whether user id is valid.
			if row[1].isdigit() and row[2].isdigit():
				g.add_edge(row[1],row[2])
	return g

def get_degree(user1, user2,graph):
	"""
	Input: user1 id (str)
	       user2 id (str)
	       graph (nx.Graph)
	Output: degree between two users (int)
	Function: Return the degree between two users in graph
	"""
	# Check if user1 and user2 are in the network
	if graph.has_node(user1) and graph.has_node(user2):
		return nx.shortest_path_length(graph, user1, user2)
	# If not, add them to the network and return degree(0)for this transaction.
	else:
		graph.add_edge(user1,user2)
		return 0

def WriteToOutput(f1,f2,f3,degree):
	"""
	Input: f1 & f2 & f3 (file object)
	Output: degree (int)
	Function: Write the notification into file.
	"""
	if degree == 1:                     # Feature 1
		f1.write("trusted\n")
		f2.write("trusted\n")
		f3.write("trusted\n")
	elif degree == 2:                   # Feature 2
		f1.write("unverified\n")
		f2.write("trusted\n")
		f3.write("trusted\n")
	elif degree == 3 or degree == 4:    # Feature 3 inside 4th-degree-network
		f1.write("unverified\n")
		f2.write("unverified\n")
		f3.write("trusted\n")
	else:                               # Feature 3 outside 4th-degree-network
		f1.write("unverified\n")
		f2.write("unverified\n")
		f3.write("unverified\n")

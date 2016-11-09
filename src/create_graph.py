import networkx as nx 
import csv
import sys
import os

class User_Network(object):
	"""docstring for User_Network"""
	def __init__(self, filename):
		self.filename = filename
		self.g = nx.Graph()

	def Create(self):
		# with open(os.path.join(os.path.dirname(__file__),self.filename), 'rU') as csvfile:
		with open(self.filename, 'rU') as csvfile:
			reader = csv.reader(csvfile, skipinitialspace = True)
			csv.field_size_limit(sys.maxsize)
			reader.next()
			for row in reader:
				if len(row) < 5:
					continue
				self.g.add_edge(row[1],row[2])
		return self.g

def feature(user1, user2, option, graph):
	if get_degree(user1,user2,graph) == option:
		return "trusted\n"
	else:
		return "unverified\n"

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

# g = nx.Graph()
# csv.field_size_limit(sys.maxsize)
# # with open('batch_payment.csv','rU') as csvfile:
# 	# dialect = csv.Sniffer().sniff(csvfile.read(1024))
# 	# csvfile.seek(0)
# 	# dialect.skipinitialspace = True
# 	# dialect.strict = True
# 	# reader = csv.reader(csvfile, skipinitialspace = True, lineterminator = '\n')
# 	# reader.next()
# 	# for row in reader:
# 	# 	# if len(row) < 5:
# 	# 	# 	continue
# 	# 	g.add_edge(row[1],row[2])
# with open('data.csv','rU') as csvfile2:
# 	reader1 = csv.reader(csvfile2, skipinitialspace = True)
# 	reader1.next()
# 	for row in reader1:
# 		# if len(row) < 5:
# 		# 	continue
# 		print row
# 		# print nx.shortest_path_length(g,row[1],row[2])
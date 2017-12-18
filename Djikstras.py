
import heapq

distance = {}
number_of_nodes = 0

def initialize_single_source(s):
	for i in range(0,number_of_nodes):
		distance[i] = -1
		
	distance[s-1] = 0


def find_shortest_paths(G, W, s):

	heapq.heapify(distance)

	while len(distance) != 0:

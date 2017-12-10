
import math
import timeit
import sys

charlies_map = []
dictionary = {}

def get_charlies_map():
	n = input()
	for i in range(0,int(n)):
		charlies_map.append(list(map(float, input().split())))
	return charlies_map


def gold_rush(charlies_map, pointN):
	key = str(charlies_map[0][0]) + str(pointN[0]) + str(len(charlies_map))
	if len(charlies_map) == 1:
		return charlies_map[0][2]

	if key in dictionary:
		return dictionary[key]

	value = -10000000
	
	for i in range(1, len(charlies_map)):
		gold_collected = gold_rush(charlies_map[i:], charlies_map[0]) + charlies_map[0][2] - distance_travlled(charlies_map[i], charlies_map[0])
		if gold_collected > value:
			value = gold_collected

	dictionary[key] = value
	return value



def distance_travlled(pointA, pointB):
	return math.sqrt(math.pow((pointB[0] - pointA[0]),2) 
					+ math.pow((pointB[1] - pointA[1]),2))

sys.setrecursionlimit(30000)
start = timeit.default_timer()
answer = gold_rush(get_charlies_map(), charlies_map[0])
stop = timeit.default_timer()

print(stop-start)
print(str(round(answer,6)))
'''

Algorithm Description: 

Reccurence relation: OPT(i) = max(OPT(i + j) for all i < j <= n)
                     Solve for OPT(0)

Time Complexity: O(n^2)

Space Complexity: O(n) for storing the map + O(n^2) for memoization with dictionary
                  Therefore: Space Complexity: O(n^2)
                  
'''
import math

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
	
	for i in range(len(charlies_map)-2, -1, -1):
		gold_collected = gold_rush(charlies_map[:i+1], charlies_map[-1]) + charlies_map[-1][2] - distance_travlled(charlies_map[i], charlies_map[-1])
		if gold_collected > value:
			value = gold_collected

	dictionary[key] = value
	return value

def distance_travlled(pointA, pointB):
	value = math.sqrt(math.pow((pointB[0] - pointA[0]),2) 
					+ math.pow((pointB[1] - pointA[1]),2)) 
	return value

answer = gold_rush(get_charlies_map(), charlies_map[-1])
print("%.6f" % answer)
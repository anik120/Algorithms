
import math

charlies_map = []
dictionary = {}

def get_charlies_map():
	n = input()
	for i in range(0,int(n)):
		charlies_map.append(list(map(int, input().split())))
	return charlies_map

def gold_rush(charlies_map):
	if len(charlies_map) == 0:
		return
	if len(charlies_map) == 1:
		return charlies_map[0][2]
	if len(charlies_map) == 2:
		d1 = math.sqrt(math.pow((charlies_map[1][0] - charlies_map[0][0]),2) 
					+ math.pow((charlies_map[1][1] - charlies_map[0][1]),2))
		return charlies_map[0][2] + charlies_map[1][2] - d1
	else:
		d1 = math.sqrt(math.pow((charlies_map[1][0] - charlies_map[0][0]),2) 
					+ math.pow((charlies_map[1][1] - charlies_map[0][1]),2))
		d2 = math.sqrt(math.pow((charlies_map[2][0] - charlies_map[0][0]),2) 
					+ math.pow((charlies_map[2][1] - charlies_map[0][1]),2))
		return max(charlies_map[0][2] + gold_rush(charlies_map[1:]) - d1,
					charlies_map[0][2] + gold_rush(charlies_map[2:]) - d2 )



answer = gold_rush(get_charlies_map())

print(str(round(answer,6)))
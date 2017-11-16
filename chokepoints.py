G = {1: [2,3], 2: [3,4], 3: [2,4], 4: [5,6], 5: [8], 6: [7], 7: [5,8,4], 8: []}

W = {(1,2): 5, (1,3): 1, (2,3): 9, (2,4): 1, (2,5): 2, 
				(3,2): 6, (3,4):11, (3,6): 3, (4,5): 6, 
				(4,6): 6, (5,8): 8, (6,7): 15, (7,4): 7, (7,5): 3, (7,8): 1 }

chokepoint = {}

def Initialize_single_source(G,s):
	for v in G.keys():
		chokepoint[v] = 1000
	chokepoint[s] = 0

def Relax(u,v,W):
	if (chokepoint[v] > W[(u,v)]):
		chokepoint[v] = W[(u,v)]
	if (chokepoint[v] < chokepoint[u]):
		chokepoint[v] = chokepoint[u]

def find_chokepoints(G,W,s):
	Initialize_single_source(G,s)
	for i in range(0, len(G.keys()) - 1):
		for edge in W.keys():
			Relax(edge[0], edge[1], W)

find_chokepoints(G,W,1)

print(chokepoint)

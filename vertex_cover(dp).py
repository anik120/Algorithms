w = [1,9,6,3,7]

def vertex_cover(W):
	if len(W) == 0:
		return 0
	if (len(W) == 1):
		return W[0]
	else:
 		minimum = min(W[0] + vertex_cover(W[1:]), 
 						W[0] + vertex_cover(W[2:]),
 						W[1] + vertex_cover(W[2:]))
 		return minimum


print(vertex_cover(w))
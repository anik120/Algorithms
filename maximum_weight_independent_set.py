G = [1,9,6,3,7]


def maximum_weight_independent_set_value(G):
	if len(G) == 0:
		return 0
	else:
		return max(G[0] + maximum_weight_independent_set_value(G[2:]), 
					maximum_weight_independent_set_value(G[1:]))



print(maximum_weight_independent_set_value(G))
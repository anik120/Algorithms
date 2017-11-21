a = [1,2,5]
M = 13

def sequence_for_sum(a,X):
	if len(a) == 0:
		return 1000
	if X < M:
		return 1000
	return min(a[0] + sequence_for_sum(a,M-X),
				sequence_for_sum(a[1:],X))

print(sequence_for_sum(a,M))
x = "ALGORITHMS"
y = "ALTURISTIC"
d = []
for i in range(len(x) + 1):
	d.append([0] * (len(y) + 1))


# def longest_common_subsequence(X,Y):
# 	if len(X) <= 0 or len(Y) <= 0:
# 		return 0
# 	elif len(X) > 0 and len(Y) > 0 and X[0] == Y[0]:
# 		return 1 + longest_common_subsequence(X[1:], Y[1:])
# 	else:
# 		return max(longest_common_subsequence(X[1:], Y), 
# 					longest_common_subsequence(X, Y[1:]))

def longest_common_subsequence(X,Y,D):
	for i in range (1, len(X) + 1):
		for j in range(1, len(Y) + 1):
			

print(longest_common_subsequence(x,y, d))


x = "ALGORITHMS"
y = "ALTURISTIC"
z = "ALR"

def longest_common_subsequence(X,Y,Z):
	if len(X) <= 0 or len(Y) <= 0 or len(Z) <= 0:
		return 0
	elif len(X) > 0 and len(Y) > 0 and len(Z) > 0 and X[0] == Y[0] and X[0] == Z[0]:
		return 1 + longest_common_subsequence(X[1:], Y[1:], Z[1:])
	else:
		return max(longest_common_subsequence(X[1:], Y, Z), 
					longest_common_subsequence(X, Y[1:], Z),
					longest_common_subsequence(X, Y, Z[1:]))


print(longest_common_subsequence(x,y,z))
a = [[1,2,3], [4,5,6]]

def largest_sum_possible(A, i, j, k):
	if i > len(A) - 1:
		return 0
	if j > len(A[0]) - 1:
		return 0
	if k <= 0:
		return 0
	else:
		return max(A[i][j] + largest_sum_possible(A, i+1, 0, k-1),
					A[i][j] + largest_sum_possible(A, i, j+1, k-1),
					largest_sum_possible(A, i+1, 0, k))


print(largest_sum_possible(a,0,0,2))
a = [3,5,9,-1,0,2]
b = [1,2,3,4,5,6,7]
def find_smallest_element(A):
	if len(A) == 1:
		return A[0]
	if len(A) == 2:
		return min(A)
	else:
		mid_index = int(len(A) / 2)
		if A[mid_index] < A[mid_index + 1]:
			return find_smallest_element(A[:mid_index + 1])
		else:
			return find_smallest_element(A[mid_index + 1:])


print(find_smallest_element(a))

	
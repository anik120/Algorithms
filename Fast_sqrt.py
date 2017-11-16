def fast_sqrt(original_input):
	if (original_input >= 1):
		return find_sqrt(0, original_input, original_input)
	else:
		return (find_sqrt(0,original_input * 100, original_input * 100)) / 10

def find_sqrt(lower_bound, higher_bound, original_input):
	#print("Lower bound:" + str(lower_bound))
	#print( "Higher_bound: " + str(higher_bound))
	q = (higher_bound + lower_bound)/ 2
	#print(q)
	if abs( (q * q) - original_input) < 0.01:
		return q
	elif (q * q) > original_input:
			return find_sqrt(lower_bound, q, original_input)
	else:
		return find_sqrt(q, higher_bound, original_input)

print(fast_sqrt(0.56))
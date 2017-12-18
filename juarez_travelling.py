



type_dict = {}

def process_input():
	line1 = input()
	N = int(line1.split()[0])
	Q = int(line1.split()[1])	

	types = input()
	types = types.split()

	i = 0

	for t in types:
		type_dict[int(t)] = i
		i += 1

	output = []
	for i in range(0,Q):
		query = input()
		parts = query.split()
		city1 = int(parts[0])
		city_type = int(parts[1])

		try:
			city2 = type_dict[city_type]
			direction = parts[2]
			number_of_steps = steps_by_juarez(city1, city2, direction, N) 
			output.append(number_of_steps)
		except Exception:
			output.append(-1)

	for o in output:
		print(o)

'''
def steps_by_juarez(city1, city2, direction, N, no_of_steps):

	if city1 == city2:
		return no_of_steps
	else:
		if direction == "R":
			next_city = (city1 + 1) % N
		else:
			next_city = (city1 - 1 + N) % N

		return steps_by_juarez(next_city,city2,direction, N, no_of_steps + 1)
'''

def steps_by_juarez(city1, city2, direction, N):
	no_of_steps = 0

	while city1 != city2:
		if direction == "R":
			city1 = (city1 + 1) % N
		else:
			city1 = (city1 -1 + N) % N
		no_of_steps += 1

	return no_of_steps

process_input()

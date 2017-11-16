
# RETURNS: A graph taken as the input from the user
def get_graph():
	graph = {}
	while True:
		relation = input()
		if not relation:
			break
		nodes = relation.split()
		if int(nodes[0]) not in graph:
			graph[int(nodes[0])] = [int(nodes[1])]
		else:
			graph[int(nodes[0])].append(int(nodes[1]))
	return graph


# GIVEN: A graph
# RETURNS: The reverse of the graph. (All edges reversed)
def reverse_graph(graph):
	g_rev = {}
	for key,nodes in graph.items():
		for node in nodes:
			if node not in g_rev:
				g_rev[node] = [key]
			else:
				g_rev[node].append(key)
	return g_rev


# GIVEN: A graph, a node to start dfs from and a list indicating
#        which nodes have already been discovered

# RETURNS: The nodes discovered, in order of their finish time
#          during dfs
def dfs(graph,starting_node,explored):
	nodes_in_order_of_finish_time = []
	stack = []
	stack.append(starting_node)
	explored[starting_node-1] = True
	while len(stack) != 0:
		next_node = stack[-1]
		next_nodes_to_explore = graph[next_node]
		for node in next_nodes_to_explore:
			further_nodes_to_explore = False
			if explored[node-1] == False:
				stack.append(node)
				explored[node-1] = True
				further_nodes_to_explore = True
		if further_nodes_to_explore == False:
			nodes_in_order_of_finish_time.append(stack.pop())
	return nodes_in_order_of_finish_time 

def dfs_accord_fin_time(graph,n,starting_node,explored, ordered_nodes):
	stack = []
	stack.append(starting_node)
	explored[starting_node-1] = True
	while len(stack) != 0:
		next_node = stack[-1]
		next_nodes_to_explore = graph[next_node]
		for node in next_nodes_to_explore:
			further_nodes_to_explore = False
			if explored[node-1] == False:
				stack.append(node)
				explored[node-1] = True
				further_nodes_to_explore = True
		if further_nodes_to_explore == False:
			ordered_nodes.append(stack.pop())
	if (len(ordered_nodes) < n): 
		restart_node = -1
		for i in range(0,n):
			if explored[i] == False:
				restart_node = i + 1
				break;
		return dfs_accord_fin_time(graph,n,starting_node,explored,ordered_nodes)
	else:
		return ordered_nodes
		

 
def connected_components(graph, explored, ordered_nodes,components):
	component = dfs(graph,ordered_nodes[-1],explored)
	key = len(components.keys()) + 1
	components[key] = component
	for node in component:
		if (len(ordered_nodes) != 0):
			ordered_nodes.pop()
			explored[node-1] = True
	if len(ordered_nodes) != 0:
		return connected_components(graph, explored, ordered_nodes,components)
	else:
		return components

#print(dfs_accord_fin_time(get_graph(), 1, []))

def find_connected_components(n,graph):
	explored = init_explored(n)
	nodes_in_order_of_finish_time = dfs_accord_fin_time(graph,n,1,explored,[])
	explored = []
	for node_number in range(0,n):
		explored.append(False)
	g_rev = reverse_graph(graph)
	return connected_components(g_rev,explored,
								nodes_in_order_of_finish_time,{})

def __main__():
	n = int(input())
	graph = get_graph()
	states = find_connected_components(n,graph)
	city_states = states_of_cities(states)
	daggers = number_of_daggers_needed(states,n,reverse_graph(graph),city_states)
	print(daggers)

def number_of_daggers_needed(states,n,graph,city_states):
	max_dagger_required = 0
	for state in states.values():
		start_from_city = state[-1]
		explored = init_explored(n)
		cities_cleared_up = dfs(graph,start_from_city,explored)
		states_clear_of_white_walkers = set()	
		for city in cities_cleared_up:
			state_city_belongs_to = city_states[city]
			states_clear_of_white_walkers.add(state_city_belongs_to)
		if(len(states_clear_of_white_walkers) > max_dagger_required):
			max_dagger_required = len(states_clear_of_white_walkers)
	return max_dagger_required


def states_of_cities(states):
	state_of_city = {}
	for state in states.keys():
		cities = states[state]
		for city in cities:
			state_of_city[city] = state
	return state_of_city

def init_explored(n):
	explored = []
	for node_number in range(0,n):
		explored.append(False)
	return explored

__main__()
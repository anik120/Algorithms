s = [3,5,7,1]

d = {}

def taking_turn(s,d):
	if(d.get((s[0],s[-1],len(s))) != None):
		return d.get((s[0],s[-1],len(s)))
	if(len(s) == 1):
		return s[0]
	if(len(s) == 2):
		return abs(s[0]-s[1])
	else:
		s_a1_an = []
		s_a1_a2 = []
		s_an_an1 = []
		for i in range(0,len(s)):
			if (i == 0):
				s_an_an1.append(s[i])
			elif(i == 1):
				s_a1_an.append(s[i])
				s_an_an1.append(s[i])
			elif(i == (len(s) - 1)):
				s_a1_a2.append(s[i])
			elif(i == (len(s) - 2)):
				s_a1_an.append(s[i])
				s_a1_a2.append(s[i])
			else:
				s_a1_an.append(s[i])
				s_a1_a2.append(a[i])
				s_an_an1.append(a[i])

		max_value = max((s[0]-s[-1]) + taking_turn(s_a1_an,d),
						(s[0]-s[1]) + taking_turn(s_a1_a2,d),
						(s[-1]-s[0]) + taking_turn(s_a1_an,d),
						(s[-1] - s[-2]) + taking_turn(s_an_an1,d))
		d[(s[0], s[-1], len(s))] = max_value
		return max_value

print(taking_turn(s,d))
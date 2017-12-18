M = 13
n = [2,1,5]

def decompose(M,n):
	
	if M == 0:
		return 0
	else:
		choices = []
		s = 0
		for i in range(0,len(n)):
			if n[i] < M:
				s = 1 + decompose(M-n[i],n)		
		choices.append(s)
		return min(choices)

print(decompose(M,n))

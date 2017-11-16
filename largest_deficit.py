R = [1,6,5,4]

def largest_deficit_interval(R):
	total_avg_rainfall = 0
	for i in range(0,len(R)):
		total_avg_rainfall += R[i]
	total_avg_rainfall = total_avg_rainfall / len(R)
	d = {}
	return dp_deficit(R,total_avg_rainfall,d,len(R)-1,len(R)-1)

def dp_deficit(R,total_avg_rainfall,d,i,j):
	if i > j or i < 0 or j < 0:
		return -1000
	total_actual_rainfall = 0
	if ( (i, j-1) in d):
		total_actual_rainfall = d[(i, j-1)] + R[j]
	if( (i+1, j) in d):
		total_actual_rainfall = d[(i+1, j)] + R[i]
	else:
		for k in range(i, j+1):
			total_actual_rainfall += R[k] 
		d[(i,j)] = total_actual_rainfall

	return max(total_avg_rainfall * (j- i + 1) - total_actual_rainfall,
		    	dp_deficit(R,total_avg_rainfall,d,i-1, j),
		    	dp_deficit(R,total_avg_rainfall,d,i,j-1))

print(largest_deficit_interval(R))
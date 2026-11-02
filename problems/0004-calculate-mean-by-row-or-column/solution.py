def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	n = len(matrix)
	m = len(matrix[0])
	if mode =="row":
		i = n
		j = m
	else:
		i = m 
		j = n 
	means = []
	for a in range(i):
		sum = 0
		for b in range(j):
			if mode=="row":
				sum+=matrix[a][b]
			else: 
				sum+=matrix[b][a]
			# print (a, b, matrix[a][b] , sum)
		if mode=="row":
			means.append(sum/m)
		else: 
			means.append(sum/n)


	return means
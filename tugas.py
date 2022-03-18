def py(n):
	for i in range(1, n+1):
		for j in range(0, n):
			if j = n-i:
				print(i, end=" ")
			elif j > n-i:
				print("0", end=" ")
			else:
				print(" ", end=" ")
		print("\r")
n=5
py(n)
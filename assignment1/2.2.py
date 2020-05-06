for i in range(6):
	for j in range(i):
		print("* ",end="")
	print("\n")
	if i==5:
		x = i
		while x>0:
			y = 1
			while y < x:
				print("* ",end="")
				y = y+1
			x = x-1
			print("\n") 

			
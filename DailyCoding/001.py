#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def main():
	n = int(input("Enter No. of Elements : "))
	a = []
	ans = 0
	for i in range(n):
		x = int(input("Enter Element : "))
		a.append(x)
	k = int(input("Enter k : "))
	for i in a:
		for j in a:
			if i+j==k:
				ans = 1
				break;
	if ans==1:
		print("true")
	else:
		print("False")

if __name__ == '__main__':
	main()
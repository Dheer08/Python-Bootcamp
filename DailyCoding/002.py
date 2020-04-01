#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the 
#numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def main():
	a = []
	ans = []
	n = int(input("Enter No. of Elements : "))
	for i in range(n):
		x = int(input("Enter Number : "))
		a.append(x)
	i=0
	while(i<n):
		ans.append(1)
		i=i+1
	i=0
	j=0
	while(i<n):
		while(j<n):
			if(i!=j):
				ans[i] = ans[i]*a[j]
			j=j+1
		i=i+1
	print(ans)


if __name__ == '__main__':
	main()		
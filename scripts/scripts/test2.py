def m(a,b): 
	for i in range(a,b):
		if (a-b) % i == 0 and i != 1:
			return [j for j in range(a,b+1,i)]




print(m(1,9))

'''

[2, 4, 6, 8]


'''
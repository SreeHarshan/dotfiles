def mutability(v1,v2,v3,v4): 
	print("Values inside the function: \n","v1:",v1,"v2:",v2,"v3:",v3,"v4:",v4)

        #Lists - Mutable
	#Changing v1 value by a new variable
	l = [2,3]
	v1 = l
	v1.extend([4,5])

	#Chagning v2 value
	v2.extend([4,5])

	#Integer - Immutable
	#Changing v3 value by a new variable
	i = 10
	v3 = i 
	v3 += 5

	#Changing v4 value
	v4 += 5

	print("Values inside the function after execution: \n","v1:",v1,"v2:",v2,"v3:",v3,"v4:",v4)

n1 = [0,1]
n2 = [0,1]
n3 = 5
n4 = 5

print("Values before function  call: \n","n1:",n1,"n2:",n2,"n3:",n3,"n4:",n4)

mutability(n1,n2,n3,n4)

print("Values after function call: \n","n1:",n1,"n2:",n2,"n3:",n3,"n4:",n4)

#Output
'''
Values before function  call: 
 n1: [0, 1] n2: [0, 1] n3: 5 n4: 5
Values inside the function: 
 v1: [0, 1] v2: [0, 1] v3: 5 v4: 5
Values inside the function after execution:
 v1: [2, 3, 4, 5] v2: [0, 1, 4, 5] v3: 15 v4: 10
Values after function call:
 n1: [0, 1] n2: [0, 1, 4, 5] n3: 5 n4: 5
'''

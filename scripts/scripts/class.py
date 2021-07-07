#-----------------
        
print("\nQ1\n")
#----------------
def Q1(v):
	l = [2,3]

	v = l
	v += [4,5]

	print(v)

a = [0,1]
Q1(a)

print(a)

#-----------------
print("\nQ2\n")
#----------------
def Q2(v):
	l = [2,3]

	v += [4,5]

	print(v)

	return l

a = [0,1]
print(Q2(a))
print(a)

#----------------
print("\nQ3\n")
#---------------

def Q3(v):
	l = 5

	l = v

	l += 5
	print(l)


a = 10
Q3(a)
print(a)

#-----------
print("\nQ4\n")
#----------

def Q4(v,v2):
	v += 1
	v = v2

	print(v,v2)

a,b = 5,10

Q4(a,b)
print(a,b)

#-----------
print("\nchange\n")
#----------

def change(x):
  x.append([50])
  return x[0],x[1],x[2],x[3]
list=[33,45,24]  
a,b,c,d=change(list)
print(list)
print(a,b,c,d)
print(list[2]==d)
#---------------------------
print("\nexchange\n")
#---------------------------
'''
'''
def exchange(x):
	if len(x) % 2 == 0:
		for i in range(0,len(x),2):
			x[i],x[i+1] = x[i+1],x[i]
		print(x)
	else:
		x.extend([0,])
		exchange(x)

l = [1,2,3,4]
l2 = [1,2,3,4,5]
exchange(l)
exchange(l2)

#---------------------------
print("\nQ5\n")
#---------------------------

def Q5(x,y,z):
	if x[0] != y:
		if x[0] < y :
			x[0] += 1
			x[1] += x[0]
		else:
			x[0] -= 1
			x[1] += x[0]
		z += x[1]
		Q5(x,y,z)

a,b,c = [10,15],13,20
Q5(a,b,c)
print(a,b,c)
'''

#PRACTICALS
'''
f = open("Temp.txt","r")
i = f.readline()

while i != "":
	print(i.replace(" ","#"))
	i = f.readline()

f.close()
'''
'''
f = open("Temp.txt","r")
c,v,u,l = 0,0,0,0
vowels = ['a','e','i','o','u']
for i in f.read():
	if i.isupper(): u += 1
	else: l += 1
	if i in vowels: v += 1
	elif i != " ": c += 1

print("Vowels",v)
print("Consonants",c)
print("Uppercase",u)
print("Lowercase",l)
f.close()
'''
'''
f = open("Temp.txt","r")
f2 = open("Temp2.txt","w")

for i in f.readlines():
	if 'a' not in i:
		f2.write(i)

f.close()
f2.close()
'''
'''
import random
print(random.randint(1,6))
'''
'''
def factorial(n):
	v = 1
	for i in range(1,n+1): v *= i
	return v
'''
'''
def list_sum(l):
	return sum(eval(input("Enter the list")))
'''
'''
def fibonacci(n,n1=1,n2=1):
	n-=1
	if n > 0:
		n1,n2 = n2,n2 + n1
		n-=1
		fibonacci(n,n1,n2)
	else:
		print(n2)

fibonacci(4)
'''
l = []
def add(v):
	l.append(v)

def remove(v):
	l.pop(0)

l = []
def add(v):
	l.append(v)

def remove(v):
	l.pop(-1)
        '''

'''
t = int(input())
for i in range(t):
    i = input().split()
    a = int(i[0])
    b = int(i[1])
 
    while (0 < a) or (0 < b):
        if a > b :
            a -= 2
            b -= 1
        else:
            a -= 1
            b -= 2
 
        if a < 0 or b < 0:
            print("NO")
            break
    else:
        print("YES")

'''

b = 6
def a(b):
	b=2
	print(b)
a(5)
print(b)
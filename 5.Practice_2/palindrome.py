N=int(input())
A=[]
for i in range(N):
    element=int(input())
    A.append(element)
if A==A[::-1]:
   print("YES")
else:
    print("NO")
#Pallindrome _2
n = int(input())
a = list(map(int, input().split()))

if a == a[::-1]:
    print("YES")
else:
    print("NO")

n= int(input())
a = list(map(int, input().split()))
op= 0
while all(x%2==0 for x in a):
    a = [x // 2 for x in a]
    op+= 1
print(op)


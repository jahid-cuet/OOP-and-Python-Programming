n=int(input())

a=list(map(int,input().split()))

from collections import Counter

b=Counter(a)
re=0
for k,c in b.items():
    if k!=c:
        re=sum(min(c,abs(k-c)))
     
print(re)
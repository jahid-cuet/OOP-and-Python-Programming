# n=int(input())
# a=list(map(int,input().split()))
# cnt={}
# for i in a:
#     if i in cnt:
#         cnt[i]+=1
#     else:
#         cnt[i]=1
# re=0

# for k,c in cnt.items():
#     if k!=c:
#         re+=min(c,abs(k-c))
# print(re)

# Doing this usig counter


n=int(input())

a=list(map(int,input().split()))

from collections import Counter

b=Counter(a)
re=0
for k,c in b.items():
    if k!=c:
        re+=(min(c,abs(k-c)))
     
print(re)
    
    

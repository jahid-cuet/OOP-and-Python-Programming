# n=int(input())
# a=[]
# a = [int(input()) for i in range(n)]
# mn=min(a)
# mx=max(a)
# for i in range(0,n):
#     if a[i]==mn:
#         a[i]=mx
#     elif a[i]==mx:
#         a[i]=mn
#     else:
#         a[i]=a[i]
# print(a)

# Method_2
n=int(input())
a = list(map(int, input().split()))
min_idx=a.index(min(a))
max_idx=a.index(max(a))
a[min_idx],a[max_idx]= a[max_idx],a[min_idx]
print(*a)




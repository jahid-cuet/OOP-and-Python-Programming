a=list(map(str,input()))
cnt_L=0
cnt_R=0
cnt=0
b=[]
for i in a:
    
    if i=='L':
        cnt_L+=1
    else:
        cnt_R+=1
    if cnt_L==cnt_R:
        cnt+=1
        b.append(''.join((a[:cnt_L+cnt_R])))
        a=a[cnt_L + cnt_R:]
        cnt_L=0
        cnt_R=0
print(cnt)       
for s in b:
    print(s) 



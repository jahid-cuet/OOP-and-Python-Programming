""" Given two numbers X and Y. Print the sum of all odd numbers between them, excluding X and Y.

Input
First line contains a number T (1≤T≤10) number of test cases.

Next T lines will contain two numbers X and Y (0≤X,Y≤10^4).

Output
Print the sum of all odd numbers between X and Y (excluding X and Y).

Example
inputCopy
3
5 6
10 4
4 9
outputCopy
0
21
12 """

t=int(input(" "))
for i in range(t):
    x=int(input(" "))
    y=int(input(" "))

    if(x>y):
       x,y=y,x
    sum=0
    for i in range(x+1,y):
        
      if i%2==1:
        sum+=i
    print(sum)
    
# Another way to doing this code->
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())

    if x > y:
        x, y = y, x
    total_sum = sum(i for i in range(x + 1, y) if i % 2 == 1)
    print(total_sum)


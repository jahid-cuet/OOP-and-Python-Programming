n=int(input())
a=list(map(int, input().strip()))
sum=0
while a>0:
    b=a%10
    sum+=b
    a=a//10

print(sum)

# Read the number of digits
N = int(input())

# Read the array of digits as a string and convert each character to an integer
digits = list(map(int, input().strip()))

# Calculate the sum of digits
sum_of_digits = sum(digits)

# Print the result
print(sum_of_digits)

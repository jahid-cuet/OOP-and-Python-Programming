a = list(map(str, input()))
cnt_L = 0
cnt_R = 0
cnt = 0
balanced_strings = []

for i in a:
    if i == 'L':
        cnt_L += 1
    else:
        cnt_R += 1

    # When counts become equal, consider it a balanced string
    if cnt_L == cnt_R:
        cnt += 1
        balanced_strings.append("".join(a[:cnt_L + cnt_R]))
        a = a[cnt_L + cnt_R:]
        cnt_L = 0
        cnt_R = 0

# Print the maximum number of balanced strings
print(cnt)

# Print the balanced strings
for string in balanced_strings:
    print(string)

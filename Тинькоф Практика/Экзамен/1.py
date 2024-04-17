n = int(input())
grades = list(map(int, input().split()))

maximum = 0
counter = 0

for i in range(n - 6):
    sublist = grades[i:i+7]
    if 2 in sublist or 3 in sublist:
        counter = 0
    else:
        counter = sublist.count(5)

    if counter > maximum:
        maximum = counter

print(maximum if maximum > 0 else -1)

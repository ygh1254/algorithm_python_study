n = int(input())

towers = [int(x) for x in input().split()]
res = []
temp = []
missed = []

for i in range(0, n-1) :
    temp.append(towers[i] - towers[i+1])

for k in range(-1, -n, -1) :
    if temp[k] < 0 :
        res.append(-1)
        missed.append(towers[k])
    else :
        res.append(n+k)

print(missed)

# count = 1   

# for k in range(-1, -n, -1) :
#     if temp[k] < 0 :
#         count += 1
#         missed.append(towers[k])
#     else :
#         for _ in range(count):
#             res.append(n+k)
#         count = 1

# for _ in range(count):
#     res.append(0)

res.reverse()

print(*res)
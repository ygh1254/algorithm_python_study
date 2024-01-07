from collections import deque

n = int(input())

towers = deque([int(x) for x in input().split()])
towers.reverse()

res, temp, missed = deque([]), deque([]), deque([])
maximum = 0

for i in range(0, n-1) :
    temp.append(towers[i] - towers[i+1])
    
temp.append(0)

print(towers)
print(temp)

for k in range(0, n) :
    # print(f'max : {maximum}, tower{k} : {towers[k]}')
    if maximum < towers[k] :
            maximum = towers[k]
            for element in missed:
                res[element] = k
            missed.clear()
            
    if temp[k] > 0 :
        res.append(-1)
        missed.append(k)
    else :
        res.append(k+1)

    print(missed)

res = deque([n-x for x in res])
for element in missed:
    res[element] = 0
    
res.reverse()
res[0] = 0

print(*res)
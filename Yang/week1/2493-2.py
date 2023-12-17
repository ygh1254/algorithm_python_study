from collections import deque

n = int(input())

towers = deque([int(x) for x in input().split()])
towers.reverse()

answer = deque([0])

for i in range(1, len(towers)):
    Break = False
    for k in range(i+1, len(towers)):
        if towers[i] < towers[k] :
            answer.append(n-k)
            Break = True
            break
    if Break == False :
        answer.append(0)
    
answer.reverse()

print(*answer)
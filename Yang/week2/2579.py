# 2579번: 계단 오르기
n = int(input())
stairs = []
visited = [0 for _ in range(n)]
score, stack = 0, 0

for _ in range(n):
    stairs.append(int(input()))
    
stairs.reverse
score += stairs[0]

print(visited)
# case 1 : 1, 2, 1, 2, ..
# case 2 : 2, 2, 2, 2, ..
# case 3 : 2, 1, 2, 1
for i in range(1, n-1):
    pass
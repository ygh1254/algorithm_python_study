'''
M, N = map(int, input().split())

prime_num = []

for i in range(2, N+1):
    flag = True
    if i == 2 and M<=2:
        print(2)
        prime_num.append(2)
        continue
    for j in prime_num:
        if i % j == 0:
            flag=False
            break
    if flag == True:
        prime_num.append(i)
        print(i)

시간 초과 '''

# 에라토스테네스의 체 (특정 범위의 모든 수를 나열하고, 소수로 나누어 떨어지지 않은 수만 남긴다. 이때 (범위가 소수의 제곱보다 작은 경우에만 계산))
from math import sqrt
import sys

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if i == 1:
        continue
    
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            break
    
    else:
        print(i)
    

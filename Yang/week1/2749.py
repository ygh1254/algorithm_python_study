# 2749. 피보나치 수 3
# 피사노 주기

n = int(input()) % 1500000

fibo = [0, 1]

for k in range(n) :
    fibo[k % 2] = sum(fibo) % 1000000
    
print(fibo[n % 2])
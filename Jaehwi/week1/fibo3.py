'''
n = int(input())

def fibo(n):
    first = 0
    second = 1

    if n == 1:
        return 1

    for i in range(1, n+1):
        current = first + second
        first = second
        second = current

    return current


print(fibo(n) % 1000000)

시간 초과 '''

# 피사노 주기 활용 (N번째 피보나치 수를 M으로 나눈 나머지는 항상 P라는 주기를 가진다. 즉, N % M == (N%P) % M . 이때 M이 10^k라면, P = 15 * 10^(k-1))

N = int(input())
N = N % (15*(10**5))

fibo = [0, 1]

for i in range(2, N):
    fibo[i%2] = (fibo[0]%1000000) + (fibo[1]%1000000)

print(sum(fibo) % 1000000)



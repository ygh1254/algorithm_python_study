from math import sqrt

m, n = map(int, input().split())

# 홀수만
prime = [i for i in range(3, n, 2)]

# 2 포함
# if m <= 2 and 2 <= n :
#     prime.append(2)

# #
# for i in range(3, int(sqrt(n))+1, 2) :
#     not_prime = [i * k for k in range(3, n//i+1, 2)]
#     prime = list(set(prime) - set(not_prime))

# for element in sorted(prime) :
#     print(element)

for i in range(3, int(sqrt(1000000))+1, 2) :
    not_prime = [i * k for k in range(3, 1000000//i+1, 2)]
    prime = list(set(prime) - set(not_prime))

prime.append(2)

prime = sorted(prime)

for element in prime :
    if element < m :
        continue
    if element > n :
        break
    else :
        print(element)

# print(len(prime))
# Time complexity : O(n)
# It is essential to reduce time complexity to O(log n)

n = int(input())

fibo = [0, 1]
k = 0

while k < n :
    fibo[k % 2] = sum(fibo)
    k += 1
    
print(fibo[n % 2])


# O(n)을 짜는 것은 엄청나게 간단한데 O(log n)을 짜는 것은 어렵다!
# 피사노 주기? 라는 것을 이용하라고 한다.
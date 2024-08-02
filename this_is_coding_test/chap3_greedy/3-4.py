# 실전 문제 4. 1이 될 때까지

n, k = map(int, input().split())
result = 0

while n >= k:           # n이 k보다 큰 경우에는 1, 2번 둘 다 가능
    while n % k != 0:   # k로 나누어 떨어지지 않는다면 1번 연산
        n -= 1
        result += 1
    n //= k             # 나누어 떨어진다면 2번 연산
    result += 1

while n > 1:            # n이 k보다 작고 1보다 큰 경우에는, 1이 될 때까지 1번 연산만
    n -= 1
    result += 1

print(result)





# 다른 답안 예시
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
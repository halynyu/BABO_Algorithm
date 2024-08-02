# 실전 문제 2. 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()         # 입력받은 수들 정렬
first = data[n-1]   # 가장 큰 수 결정
second = data[n-2]  # 두 번째로 큰 수 결정
# 해당 문제에서는 세 번째로 큰 수부터는 절대 쓸모가 없음

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result)

"""
해당 문제에서는 M이 10,000 이하이므로 이 방식으로도 문제를 해결할 수 있으나,
M의 크기가 100억 이상처럼 커진다면 시간 초과 판정!!을 받을 수 있다.
-> 다른 해결방안
(K+1)개가 반복되는 수열 : K개의 first와 한 개의 second 숫자
ex) 2, 4, 5, 4, 6 / m=8, k=3
{6, 6, 6, 5} + {6, 6, 6, 5}의 형태가 될 것
즉, M을 (K+1)로 나눈 몫 만큼 {6, 6, 6, 5}의 형태는 반복될것이고,
나머지 숫자만큼 first 숫자를 더해주게 된다.

"""




# 다른 답안 예시 -> 시간복잡도 감소

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k      # 가장 큰 수가 더해지는 횟수계산
count += m % (k + 1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
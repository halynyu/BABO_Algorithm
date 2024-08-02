# 실전 문제 3. 숫자 카드 게임

"""
각 행마다 가장 작은 수를 찾은 뒤, 그 수 중에서 가장 큰 수를 찾는다.

- for문에서 각 행에 해당하는 숫자들을 입력받는데, 이 때 list로 입력받아 그 중에서 최저값을 찾는다. (min_value)
- 처음에는 0으로 초기화되어있는 result를 min_value값으로 바꾼다
- 그 후, 다음 행의 숫자들을 입력받아 그 중 최저값과 result에 저장되어있는 min_value값을 비교해 둘 중 큰 값을 찾는다
- 결론적으로, 각 행의 최저값들 중 가장 큰 값이 result에 저장되어있다.

"""

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)




# 다른 답안 예시 -> 2중 for문 구조 이용
"""
- 위의 예시와는 다르게 min_value값을 큰 값 (범위를 넘어가는)으로 초기화시켜놓는다 (min_value = 10001)
- 각 행에 들어있는 data(list)의 원소들을 min_value값과 비교하며 더 작은 값을 min_value로 저장시킨다.
- 행에 있는 모든 원소들과 비교하면 (for문이 한 루프 돌아가면), 해당 행에 있는 가장 작은 값이 min_value로 저장되어있다.
- 마지막으로, result값(초기값이 0인)과 min_value값을 비교하여 더 큰 값을 result에 저장한다.
-> 위의 풀이와는 각 행의 min_value값을 정하는 방법이 다름
"""

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
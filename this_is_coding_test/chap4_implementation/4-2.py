# 실전 문제 2. 왕실의 나이트

"""
- 8X8 좌표 평면
- L자 형태로만 이동
    - 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    - 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

"""


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:   # 체스판 안에 있다면
        result += 1
print(result)
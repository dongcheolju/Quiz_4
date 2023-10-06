print("구구단을 출력합니다.\n")
for x in range(2, 10):
    print ("------- [" + str(x) + "단] -------")
    for y in  range(1, 10):
        print(x,"X", y, "=", x*y)
print("----------------------")

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0], matrix[1], matrix[2])

for row in matrix:
    for element in row:
        print(element)


matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0], matrix[1], matrix[2])
print(matrix[0][0])

for row in matrix:
    for element in row:
        print(element)


matrix = [[1,2,3], 4, [5,6,7,8,9]]
total = 0

for row in matrix:
    for element in row:
        total = total + element

# 디버깅을 위한 print 함수 사용
matrix = [[1,2,3], 4, [5,6,7,8,9]]
total = 0

for row in matrix:
    print("현재 행, 첫 번째 이중 반복문:", row)
    for element in row:
        print("현재 요소, 두 번째 이중 반복문:", element)
        total = total + element


results = []
numbers = [[1, 2, 3],  [4, 5, 6], [7, 8, 9]]
for row in numbers:
    for n in row:
        if n % 2 == 0:
            results.append(n)
print(results)


print("구구단을 출력합니다.\n")
for x in range(1, 19+1):
    print ("------- [" + str(x) + "단] -------")
    for y in  range(1, 19+1):
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



#두 수를 더하는 함수
def add_number(a, b):
    result = a + b
    return result

# 함수 호출 및 반환값 사용
sum_result = add_number(5, 3)
print("합계:", sum_result)



pingpong_list = ["나영", "예진", "원빈", "현빈"]
results = []

def create_contents_of_mail(a):
    apple = f"한국교통대학교 천하제일 탁구대회, {a}님 탁구 대회에 참여해주셔서 감사합니다. \n행사 일시: 2023-10-06, 시간: 10:30 AM, \n복장: 트레이닝 복 행사 당일에 뵙겠습니다. \n{a}님 감사합니다.\n"
    return apple

for a in pingpong_list:
    email = create_contents_of_mail(a)
    results.append(email)

for aaa in results:
    print(aaa)

print(results)


print("구구단을 출력합니다. \n")
    for x in range(1, a):
        print("------[ " + str(x) + "단 ] ------")
        for y in range(1, 10):
            print(x, "X", y, "=", x*y)



for x in range(1, a+1):
        print ("------- [" + str(x) + "단] -------")
        for y in  range(1, a+1):
            print(x,"X", y, "=", x*y)

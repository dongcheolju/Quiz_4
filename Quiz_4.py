a=int(input("몇 단까지 입렵할까요?"))
print(a, type(a))
print("구구단을 출력합니다.\n")
def 구구단 (a):
    for x in range(1, a+1):
        print ("------- [" + str(x) + "단] -------")
        for y in  range(1, a+1):
            print(x,"X", y, "=", x*y)
    # if a < 10:
    #     for y in  range(1, 11):
    #         print(x,"X", y, "=", x*y)
구구단(a)
print("--------------------")


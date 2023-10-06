pingpong_list = ["나영", "예진", "원빈", "현빈"]
results = []

def create_contents_of_mail(a):
    str(a)
    return f"한국교통대학교 천하제일 탁구대회, {a}님 탁구 대회에 참여해주셔서 감사합니다. 행사 일시: 2023-10-06, 시간: 10:30 AM, 복장: 트레이닝 복 행사 당일에 뵙겠습니다. {a}님 감사합니다."

for a in pingpong_list:
    email = create_contents_of_mail(a)
    results.append(email)

for email in results:
    print(email)


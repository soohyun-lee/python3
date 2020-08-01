n = input('주민번호 입력:').split('-') # 하이푼 같이 입력하고 하이푼 기준으로 쪼개기
i = n[1]
for x in i[0]:
    if x[0] == '1' or '3':
        print('남자')
    elif x[0] == '2' or '4':
        print('여자')
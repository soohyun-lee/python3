money = int(input('금액을 투입하세요:'))
menu = {'콜라':1000, '핫식스':2000, '환타':500, '커피':3000}
select = ['돈 투입','다른 음료 선택']
vle = list(menu.values())
# print(vle)
# print(menu['콜라'])
cnt = 0
while cnt < 3:
    a = input('메뉴명 입력하세요:')
    if menu[a] <= money:
        money -= menu[a]
        print('{}를 선택했습니다. 남은 잔돈은 {}입니다.'.format(a,money))
        cnt += 1
    elif menu[a] > money:
        print('{}를 선택했습니다. {}만큼 잔돈이 부족합니다.'.format(a,menu[a]-money))
        print("*"*60)
        while True:
            for i, l in enumerate(select, start=1):
                print('{}:{}'.format(i, l))
            sel = int(input('돈을 투입하거나, 다른 음료를 선택해주세요(번호 선택):'))
            print('{}을 선택했습니다'.format(select[sel - 1]))
            if sel == 1:
                add_money = int(input('돈을 투입하세요:'))
                money += add_money
                print('총 잔액은 {}입니다.'.format(money))
            if 0 < sel < 3:
                break
print('3회가 끝났습니다.')
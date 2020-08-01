# 자판기 내의 음식이나 음료의 종류는 2가지 이상. (한번에 같은 음료 선택 가능)
# 금액 투입 후, 잔돈을 계산 하는 알고리즘도 함께. (예: 1000원 투입 후, 300원짜리 선택하면, 700원이 남으므로 더 살 수 있게끔 짜주세요, 단 금액 투입 후 금액이 남더라도 최대 3가지만 선택)

# ver1
menu = {'콜라': 1000, '사이다':500,'환타':1500, '핫식스':2000}
ks = menu.keys()
key_list = list(menu.keys())
vals = menu.values()
print(vals)
for k in ks:
    print('메뉴명:%s, 가격:%d' %(k,menu[k]))
money = int(input('돈을 투입하세요'))
n = input('메뉴를 입력하세요:')
if n in menu:
    print('%s의 가격은 %d입니다.' %(n,menu[n]))
    j = int(money) - int(menu[k])
    print('남은 잔돈은', j, '입니다')
    while True:
        for i in vals:
            if j >= i:
                n2 = input('음료를 추가로 구매하세요')
                j -= int(menu[n2])
                if j >= i:
                    print('남은 잔돈은', j, '입니다')
                    if j < i:
                        print('잔액이 부족합니다')

# edit
menu = {'콜라': 1000, '사이다':500,'환타':1500, '핫식스':2000}
ks = menu.keys()
key_list = list(menu.keys())
vals = menu.values()
print(vals)
for k in ks:
    print('메뉴명:%s, 가격:%d' %(k,menu[k]))
money = int(input('돈을 투입하세요'))
n = input('메뉴를 입력하세요:')
if n in menu:
    print('%s의 가격은 %d입니다.' %(n,menu[n]))
    j = int(money) - int(menu[n])
    print('남은 잔돈은', j, '입니다')
    while True:
        for i in vals:
            if j >= i:
                n2 = input('음료를 추가로 구매하세요')
                j -= int(menu[n2])
                print('남은 잔돈은', j, '입니다')
            elif j == 0:
                print('잔액이 0원입니다.')
                break
            else:
                print('잔액이 부족합니다')
                break
        break

h = float(input('키:'))
w = float(input('체중:'))

n = w / ((h * 0.01) ** 2)
if n < 18.5:
    print('평균 이하입니다')

elif 18.5 <= n < 25.0:
    print('표준입니다.')

elif 25.0 <= n < 30.0:
    print('비만입니다.')

else:
    print('고도 비만입니다.')
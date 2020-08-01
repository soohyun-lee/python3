# 자연수 n을 입력하고, 자연수 n의 약수들의 총 합을 구하시오

n = int(input('숫자입력: '))

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

print(solution(n))
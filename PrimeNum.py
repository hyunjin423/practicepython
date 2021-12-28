# -*- coding: utf-8 -*-


#소수 판별함수
def is_prime_number(x):
    for i in range(2,x): #2~(x-1)까지 확인
        if x % i ==0: #x가 i로 떨어지면 소수아님
            return False
    return True #만족값이 없으면 소수

print(is_prime_number(4))
print(is_prime_number(7))
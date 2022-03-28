# demodict.py

# 함수를 정의
import re


def calc(a,b):
    return a+b, a*b

#첫번째 컬럼 이동
result = calc(3,4)
#슬라이싱 사용
print(result[0])
print(result[1])

#하나로 모아서 입력
# * 는 포인터가 아닐 튜플타입이라고 알려주는것
args = (5,6)
print(calc(*args))

#타입캐스팅(형식변환)
a = set ((1,2,3,))
print(a)
print(type(a))
b = list(a)
print(b)
b.append(5)
print(b)

#dictionay (JSON: 자바스크립트의 객체표기)
d = {'apple':'red', 'kiwi':'green'}
print(len(d))
print(d["apple"])
d['banana'] = 'yellow'
print(d)


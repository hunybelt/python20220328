#function3.py

#가변인자
def union(*ar):
    #지역변수를 리스트로 초기화
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
#디버깅할때 브레이크 포인트
print(union('HAM', 'EGG'))
print(union('HAM', 'EGG', 'SPAM'))


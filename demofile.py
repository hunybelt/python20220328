# DemoFile.py 

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("--약간 서식을 변경---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3))

#문자열 결합 연산
url = "http://www.credu.com/?page=" + str(1) 
print(url)

print("--서식문자--")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))

#파일에 쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("한글데이터\nabcd\n1234\n")
f.close()
print(f.closed)

#파일을 읽기
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
#첫줄부터 끝까지 읽어서 str로 리턴 
result = f.read()
print(result)
print('어디쯤: ', f.tell())
f.seek(0)

print(f.readline())
print(f.readline())

f.close()
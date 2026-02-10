import turtle
import math

def 다각형그리기(n) :
    for i in range(n):
        turtle.forward(1000 / n)
        turtle.right(360 / n)

def 대각선추출(n) :
    print("대각선 개수:", int(n*(n-3)/2), end="개")

def 세팅() :
    turtle.screensize()
    turtle.left(90)
    turtle.forward(320)
    turtle.right(90)
    turtle.clear()

def 각도(n) :
    print("(내)한 각:", 180*(n-2)/n)
    print("(내)전부:", 180*(n-2))
    print("(외)한 각:", 360/n)
    print("(외)전부:", 360)

def 원(r) :
    print("원주", r*2*math.pi)
    print("원주", r*2, end="π")
    print()
    print("넓이", r*r*math.pi)
    print("넓이", r*r, end="π")

def 부채꼴넓이(r) :
    mode = input("각도/호: ")
    if mode == "각도입력" or mode == "각도" :
        각도 = int(input("각도 입력: "))
        print(각도/360*r*r*math.pi)
        print(각도/360*r*r, end='π')
    elif mode == "호" or "호 입력" :
        호길이 = int(input("호 길이 입력: "))
        print(호길이*r*math.pi/2)
        print(호길이*r/2, end='π')

def 회전체(x,y) :
    종류 = input("원기둥/원뿔/구: ")
    if 종류 == '원기둥' :
        print(x*x*math.pi*y, end='cm³')
        print()
        print(x*x*y, end='πcm³')
    if 종류 == '원뿔' :
        print(x*x*math.pi*y/3, end='cm³')
        print()
        print(x*x/3, end='πcm³')
    if 종류 == '구' :
        print(x*x*math.pi*y/3*2, end='cm³')
        print()
        print(x*x*y/3*2, end='πcm³')

def 각기둥(x, y, z) :
    print(x*y*z, end='cm³')

def 각뿔(x, y, z) :
    print(x*y*z/3, end='cm³')

def 각기둥겉넓이(x, y, z) :
    print((x*y*2)+(x*z*2)+(z*y*2), end='cm²')

while True:
    print()
    input("다시 시작하려면 enter 누르쇼")
    모드 = input("""
모드 선택
================
그리기/대각선개수/각도
/원/부채꼴넓이/회전체
/각기둥/각뿔
================
>> """)

    if 모드 == "그리기" :
        다각형 = int(input("O각형: "))
        세팅()
        다각형그리기(다각형)
    elif 모드 == '대각선개수' or 모드 == '대각선' :
        다각형 = int(input("O각형: "))
        대각선추출(다각형)
    elif 모드 == "각도" or 모드 == '각' :
        다각형 = int(input("O각형: "))
        각도(다각형)
    elif 모드 == "원" :
        반지름 = int(input("반지름: "))
        원(반지름)
    elif 모드 == "부채꼴넓이" :
        반지름 = int(input("반지름: "))
        부채꼴넓이(반지름)
    elif 모드 == '회전체' :
        반지름 = int(input("반지름: "))
        높이 = int(input("높이: "))
        회전체(반지름, 높이)
    elif 모드 == '각기둥' :
        가로 = int(input("가로 입력: "))
        세로 = int(input("세로 입력: "))
        높이 = int(input("높이 입력: "))
        각기둥(가로, 세로, 높이)
        print()
        각기둥겉넓이(가로, 세로, 높이)
    elif 모드 == '각뿔' :
        가로 = int(input("가로 입력: "))
        세로 = int(input("세로 입력: "))
        높이 = int(input("높이 입력: "))
        각뿔(가로, 세로, 높이)
    else :
        print("없는 모드입니다.")
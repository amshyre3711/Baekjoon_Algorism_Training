from datetime import datetime as dt

num = 10000000
#Time Test Case1
#일반 for문. 리스트 추가
start= dt.now()
list = []
for i in range(num):
    list.append(i)
end = dt.now()
#print(*list)
print(f"일반 for문 리스트 추가 결과 : {end-start}s")

#Time Test Case2
#반복문 콜론 제외 문법 사용.
#반복문 안에 콜론이 들어가면 느려짐.
start= dt.now()
list = []
ap = list.append
for i in range(num):
    ap(i)
end = dt.now()
#print(*list)
print(f"반복문 내 콜론 제외 결과 : {end-start}s")


#Time Test Case3
#리스트 컴프리헨션 문법 사용
start= dt.now()
list = [i for i in range(num)]
end = dt.now()
#print(*list)
print(f"리스트 컴프리헨션 결과 : {end-start}s")

#Time Test Case4
#제네레이터 표현식 사용
start= dt.now()
list = (i for i in range(num))
end = dt.now()
#print(*list)
print(f"제네레이터 표현식 결과 : {end-start}s")

'''
제네레이터 표현식 그 다음으로 
리스트 컴프리헨션이 가장 빠르고 
반복문 내에 .이 들어가면 느려짐. 
반복문 내 콜론 사용은 가급적이면 지양해야 함. 

일반 for문 리스트 추가 결과 : 2.454565s
반복문 내 콜론 제외 결과 : 2.267382s
리스트 컴프리헨션 결과 : 0.845890s
제네레이터 표현식 결과 : 0.151164s
'''
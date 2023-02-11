#https://www.acmicpc.net/problem/1000

A, B = input().split()

def plus(A, B):
    A, B = int(A), int(B)
    result = A+B
    for i in range(1,100):
        result = str(result)
        result = int(result)
    return result

C = plus(A,B)

print(C)

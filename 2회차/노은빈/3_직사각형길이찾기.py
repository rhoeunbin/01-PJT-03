import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())
lst = []

for i in range(t):
    a,b,c = map(int, input().split())
    if a == b :
        print(f'#{i+1} {c}')
    elif a == c :
        print(f'#{i+1} {b}')
    elif b == c :
        print(f'#{i+1} {a}')

#    lst.sort() #정렬해서 남은 하나 값 구하기
#    if lst[i]<lst[i+1] :
#     print(f'')
#    print(f'#{i+1} {lst[2]}')


# 1 1 2  i=0
# 3 4 4   i=1
# 5 5 5   1=2
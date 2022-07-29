import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())
num = list(map(int, input().split()))
cnt = 0
n = ''

for i in range(t):
    if num[(i%2 !=0)] :
        cnt += (num[i]*2)
    else :
        cnt += (num[i])
    print(cnt)



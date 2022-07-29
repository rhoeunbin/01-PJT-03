import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input())

for i in range(t):
    n = int(input())
    number = list(map(int,input().split()))
    number.sort()
    cnt = 0
    max_number = 0

    for j in range(len(number)-1):
        if number[j] == number[j+1]:
            cnt += 1
        else :
            cnt = 0

    print(f'#{i+1} {max_number}')

    #다시풀어야됨,,,정답 아님
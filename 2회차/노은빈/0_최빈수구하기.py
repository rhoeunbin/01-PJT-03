import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input())

for i in range(t):
    n = int(input())
    number = list(map(int,input().split()))
    
    #여기부터 구글링(도저히 모르겠다)
    max_num = 0
    max_idx = 0

    counts = [0] * 101  #0점 ~ 100점까지 사람 수

    for j in range(1000):  #1000명의 학생
        counts[number[j]] += 1
    # print(counts)

    for j in range(101):  #
        if counts[j] >= max_num:  #0점부터 반복하면서 최빈수 찾기
            max_num = counts[j] #최빈수가 여러개이면 더 큰 값 출력
            max_idx = j
    print(f'#{i+1} {max_idx}')
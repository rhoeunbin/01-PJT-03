from re import L
import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())  #테스트 케이스

for i in range(t): 
    n = int(input())
    lst = list(map(int,input().split()))  #리스트로 받기
    sum_= sum(lst)   #합 계산
    total = len(lst)  #리스트 길이 개수로 받음
    avg = sum_/total
    lst2 = []  #빈 리스트
    for j in range(len(lst)):
        if avg >= lst[j]:   #평균보다 리스트의 값이 작거나 같으면
            lst2.append(j)  #빈 리스트에 추가
    print(f'#{i+1} {len(lst2)}')  #lst2의 길이 = 사람 수

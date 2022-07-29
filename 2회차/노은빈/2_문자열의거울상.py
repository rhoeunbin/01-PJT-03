import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())

for i in range(t):
    alpha = list(str(input()))  #알파벳을 리스트로 받음
    lst = ' '
    #replace쓰려고 했으나 리스트에는 적용 안 되는 오류 나옴->따로 대입
    for j in range(len(alpha)):
        if alpha[j] == 'b': 
            lst += 'd'
        elif alpha[j] == 'd': 
            lst += 'b'
        elif alpha[j] == 'p': 
            lst += 'q'
        elif alpha[j] == 'q': 
            lst += 'p'

    print(f'#{i+1} {(lst[::-1])}')  #[::-1]을 사용해 문자 뒤집어줌


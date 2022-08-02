import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input()) #test case

for i in range(t): #t만큼 리스트 받기
    num = input()
    num2 = num.replace('-', '')  #-(하이픈)을 아예 없애줌 -> 이 부분 다른 분 코드 참고함
    #비슷한 코드를 만들었지만 계속 단이 6개만 나왔는데 참고 후 풀렸다 

    for j in range(len(num2)): #num2의 길이만큼
        if num2[0] == '3' or num2[0] == '4' or num2[0] == '5' or num2[0] == '6' or num2[0] == '9':
            if len(num2) == 16 :  #만약 카드자리수가 16개라면
                print(f'#{i+1} {1}') #카드 만들기 가능 -> 1 출력
                break
            else : #그 외에는
                print(f'#{i+1} {0}') #카드 만듥기 불가능 -> 0 출력
                break
        else :  #첫 숫자가 3, 4, 5, 6, 9가 아니면
            print(f'#{i+1} {0}')    
            break   

#다른 분 코드 참고해서 함
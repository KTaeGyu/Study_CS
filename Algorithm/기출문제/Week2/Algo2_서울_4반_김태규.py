T = int(input())  # 테스트 수 입력

for tc in range(1, T+1):
    N = int(input())  # 정수의 갯수 입력
    Ai = list(map(int, input().split()))  # 각 칸의 점수 입력

    # 점수의 총합을 구하는 코드
    sum_v = 0  # 점수의 총합
    for j in range(1, N+1):  # 한번에 공이 튀는 칸 수(1 ~ N 까지)
        for i in range(N // j + 1):  # 공이 튀는 횟수(N // j + 1)
            if j*i < N:
                sum_v += Ai[j*i]  # 공이 탈출(j*i >= N)하기 전까지 부딛힌 정수를 모두 더해준다.
    
    # 점수가 0 이하일 경우 0을 출력하도록 함
    if sum_v <= 0:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum_v}')
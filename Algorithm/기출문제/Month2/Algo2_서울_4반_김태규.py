T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(input().split())

    bonus = 0   # 보너스 점수
    B = []      # 카드덱 B, Queue
    C = []      # 카드덱 C, Stack

    for i in A:
        if i.isdigit():                     # 숫자일 경우
            if (int(i) + bonus) % 2 == 1:   # 홀수일 경우
                B.append(int(i) + bonus)
            else:                           # 짝수일 경우
                C.append(int(i) + bonus)
        else:                               # '+'일 경우
            bonus += 1

    if len(B) >= M:     # 카드덱 B에서 김싸피가 얻을 점수
        b = B[M - 1]
    else:               # 만약 카드덱 B가 비었다면 0점
        b = 0
    if len(C) >= M:     # 카드덱 C에서 김싸피가 얻을 점수
        c = C[len(C) - M]
    else:               # 만약 카드덱 C가 비었다면 0점
        c = 0

    print(f'#{tc} {b + c}')

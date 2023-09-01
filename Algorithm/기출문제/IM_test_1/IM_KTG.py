import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    max_s = 0
    min_s = float('inf')
    for n in range(N):
        stu = list(map(int, input().split()))
        score = 0
        bonus = 0
        for i in range(M):
            if stu[i] == ans[i]:
                bonus += 1
                score += bonus
            else:
                bonus = 0
        if max_s < score:
            max_s = score
        if min_s > score:
            min_s = score
    print(f'#{tc} {max_s - min_s}')


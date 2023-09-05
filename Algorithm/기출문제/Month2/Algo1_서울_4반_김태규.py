T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 물풍선이 뻗어나가는 방향

    max_v = 0               # 최대 점수
    min_v = float('inf')    # 최소 점수

    for y in range(N):
        for x in range(N):
            now = arr[y][x]     # 현재 좌표의 값 (물풍선의 세기)
            add_v = arr[y][x]   # 현재 좌표에서 얻을 수 있는 점수
            for r in range(1, now + 1):
                for dy, dx in direction:             # 방향배열로 점수 합 계산
                    ny, nx = y + dy * r, x + dx * r
                    if 0 <= ny < N and 0 <= nx < N:  # 좌표가 벗어나지 않는 조건
                        add_v += arr[ny][nx]

            if min_v > add_v:   # 최소 점수 갱신
                min_v = add_v
            if max_v < add_v:   # 최대 점수 갱신
                max_v = add_v

    print(f'#{tc} {max_v - min_v}')

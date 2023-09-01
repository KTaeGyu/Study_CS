import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint


def solve(now, size):
    if set(select) in visited:
        return
    elif size == 4:
        val = 0
        for cy, cx in select:
            val += arr[cy][cx]
        ans = val ** 2
        global result
        if result < ans:
            result = ans
        visited.append(set(select))
        return
    else:
        for i in graph[now]:
            if i not in select:
                side = i
                select.append(side)
                solve(side, size + 1)
                select.pop()


T = int(input())
for tc in range(1, T+1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    # 인접 셀 그래프로 정리
    u_cell = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0)]
    d_cell = [(-1, 0), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    graph = {}
    for i in range(H):
        for j in range(W):
            graph[(i, j)] = []
            if j % 2 == 0:
                for di, dj in u_cell:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W:
                        graph[(i, j)].append((ni, nj))
            elif j % 2 == 1:
                for di, dj in d_cell:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W:
                        graph[(i, j)].append((ni, nj))

    # DFS로 대부분의 경우의 수를 확인
    result = 0
    for y in range(H):
        for x in range(W):
            now = (y, x)
            select = [now]
            visited = []
            solve(now, 1)

    # DFS 에서 빠진 경우의 수 확인
    u_c = [(-1, -1), (-1, 1), (1, 0)]
    d_c = [(0, -1), (0, 1), (1, 0)]
    for y in range(H):
        for x in range(W):
            select = [(y, x)]
            if x % 2 == 0:
                for dy, dx in u_c:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < H and 0 <= nx < W:
                        select.append((ny, nx))
                    else:
                        break
                else:
                    sum_v = 0
                    for cy, cx in select:
                        sum_v += arr[cy][cx]
                    ans = sum_v ** 2
                    if result < ans:
                        result = ans
            elif x % 2 == 1:
                for dy, dx in d_c:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < H and 0 <= nx < W:
                        select.append((ny, nx))
                    else:
                        break
                else:
                    sum_v = 0
                    for cy, cx in select:
                        sum_v += arr[cy][cx]
                    ans = sum_v ** 2
                    if result < ans:
                        result = ans

    print(f'#{tc} {result}')





















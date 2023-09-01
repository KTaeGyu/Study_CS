import sys
sys.stdin = open("input.txt", "r")
from copy import deepcopy


def check(arr):
    cnt = 0
    ans = []
    visited = []
    for i in range(N):
        if i not in visited:
            temp = []
            cnt += 1
            stack = [i]
            visited.append(i)
            while stack:
                now = stack.pop()
                temp.append(now)
                for j in range(N):
                    if arr[now][j] == 1 and j not in visited:
                        stack.append(j)
                        visited.append(j)
            result = 0
            for j in temp:
                result += Pi[j]
            ans.append(result)
    return cnt, max(ans) - min(ans)


def solve(i, n):
    if i == n:
        arr = deepcopy(Rrc)
        for i in range(n):
            if bit[i] == 0:
                cy, cx = nodes[i][0], nodes[i][1]
                arr[cy][cx], arr[cx][cy] = 0, 0
        cnt, result = check(arr)
        if cnt == 2:
            global min_v
            if min_v > result:
                min_v = result
        return
    else:
        bit[i] = 1
        solve(i+1, n)
        bit[i] = 0
        solve(i+1, n)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Rrc = [list(map(int, input().split())) for n in range(N)]
    Pi = list(map(int, input().split()))

    # 노드 계산
    node_num = 0
    nodes = []
    for i in range(N):
        for j in range(i+1, N):
            if Rrc[i][j] == 1:
                node_num += 1
                nodes.append((i, j))

    bit = [0] * node_num
    min_v = float('inf')
    solve(0, node_num)
    print(f'#{tc} {min_v}')












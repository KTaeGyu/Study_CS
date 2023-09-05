T = int(input())  # 테스트 수 입력

for tc in range(1, T+1):
    N = int(input())  # 배열의 크기 입력
    r1, c1, r2, c2 = map(int, input().split())  # 평탄화할 두 지점 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력

    # 두 지점의 평균값을 구하는 코드
    add_v = 0  # 각 칸의 총 합
    count = 0  # 각 칸의 갯수
    # 두 지점 사이의 값을 모두 탐색
    for y in range(r1, r2+1):
        for x in range(c1, c2+1):
            add_v += arr[y][x]
            count += 1
    mean = add_v//count  # 각 칸의 총 합//칸의 수 = 평균값

    # 작업 횟수를 구하는 코드
    work = 0  # 총 작업 횟수
    # 두 지점 사이를 모두 탐색, 평균값과 각 칸의 값의 차이를 1회 작업량으로
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            # 차이가 양수일 경우
            if (mean - arr[i][j]) >= 0:
                work += (mean - arr[i][j])
            # 차이가 음수일 경우
            else:
                work -= (mean - arr[i][j])
    
    # 출력 양식
    print(f'#{tc} {work}')
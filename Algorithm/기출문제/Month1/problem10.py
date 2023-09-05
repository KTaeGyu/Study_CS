############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def find_one(matrix):
    # 행과 열을 계산하기 위한 변수
    row = -1
    colomn = -1

    # 반복문을 끝내기 위한 불리언값
    is_break = False

    # 열의 길이를 재기 위한 반복문
    full_row = 0
    for i in matrix[0]:
        full_row += 1
    
    # 행의 길이를 재기 위한 반복문
    full_colomn = 0
    for i in matrix:
        full_colomn += 1

    # 숫자 1의 위치를 찾는 반복문 (열의 위치는 여기서 계산 종료)
    for i in matrix:
        row += 1
        for j in i:
            colomn += 1
            if j == 1:
                is_break = True
                break
        if is_break == True:
            break
    
    # 행이 열에 나눠지는 경우를 고려 (맨 끝열일 경우)
    if colomn % full_row != 0:
        col = colomn % full_row
    else:
        col = full_colomn

    # 최종 결과 반환
    return (row, col)
            


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    sample_matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    # 각각 행과 열의 합을 담을 리스트
    row_sum_list = []
    colomn_sum_list = []

    # 행의 합을 리스트에 추가
    for i in matrix:
        row_sum = 0
        for j in i:
            row_sum += j
        row_sum_list.append(row_sum)

    # zip 함수를 이용하여 매트릭스를 90도 뒤집음
    turned_matrix = list(zip(*matrix))

    # 뒤집은 매트릭스의 행의 합(=원래 열의 합)을 리스트에 추가
    for x in turned_matrix:
        colomn_sum = 0
        for y in x:
            colomn_sum += y
        colomn_sum_list.append(colomn_sum)

    # 행의 합 중 최댓값을 골라냄
    max_row = 0
    for row in row_sum_list:
        if max_row <= row:
            max_row = row
        else:
            max_row = max_row
    
    # 열의 합 중 최댓값을 골라냄
    max_col = 0
    for col in colomn_sum_list:
        if max_col <= col:
            max_col = col
        else:
            max_col = max_col

    # 행과 열 최댓값 중 더 큰 값을 비교하여 결과 반환
    if max_row > max_col:
        return ('row', max_row)
    elif max_col > max_row:
        return ('col', max_col)
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
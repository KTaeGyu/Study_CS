############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def count_over_speed(speed_list):
    # 반환할 값
    count = 0

    # 속도가 넘는 차량당 카운트 1개씩 늘림
    for i in speed_list:
        if i > 100:
            count += 1
    
    # 카운트 반환
    return count
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(count_over_speed([119, 124, 178, 192,]))  #=> 4

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    

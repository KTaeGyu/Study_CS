############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):
    # 전체 합이 될 값
    my_sum = 0

    # 나눌 값(항의 갯수)
    count = 0

    # 반복 한번에 항의 갯수 +1, 속도는 전체 합으로 더해짐
    for i in speed_list:
        if i > 100:
            my_sum += i
            count += 1
            
    # 전체 합에서 항의 갯수를 나누어 평균값 계산 후 반환
    mean = my_sum/count
    return mean
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
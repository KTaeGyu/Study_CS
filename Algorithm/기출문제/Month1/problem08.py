############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calculate_sum_number(word):
    # 숫자만 넣을 리스트를 생성
    num_list = []

    
    for i in word:
        # 숫자인 경우 숫자로 바꾸어 리스트에 넣고,
        try:
            num_list.append(int(i))
        # 아닐 경우 아무것도 하지 않고 pass
        except:
            pass
    
    # 숫자만 넣은 리스트의 합을 반환
    return sum(num_list)
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calculate_sum_number('ab123cd45ef6')) # => 21
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
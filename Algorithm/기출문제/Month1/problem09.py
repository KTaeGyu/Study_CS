############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_digits(number):
    # 숫자 리스트에 문자열 형식으로 각 자릿수를 저장
    num_list = []
    for i in str(number):
        num_list.append(i)
    
    # 맨 끝의 한 자리를 숫자로 바꾸며 pop
    a = int(num_list.pop())

    # 리스트가 빌 경우, 마지막 숫자를 반환하고 종료
    if num_list == []:
        return a
    # 그 외의 경우 나머지 문자열을 다시 숫자로 바꿈
    else:
        number = int(''.join(num_list))

    # 바꾼 숫자를 재귀함수 형태로 다시 함수에 넣음
    return a + sum_digits(number)
    
    
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_digits(123))  # => 6
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
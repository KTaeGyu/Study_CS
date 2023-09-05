############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    # 숫자가 제일 작은 소수인 2가 되었을 때 2를 반환하고 종료
    if number == 2:
        return 2
    
    # 조건에서 17을 제외하라고 하였으니 반복문에 들어가기 재귀
    elif number == 17:
        return sum_primes(number-1)
    
    else:
        # n-1 부터 2까지 나눠본 후, 나머지가 0인 경우가 있으면 소수가 아니므로 재귀
        for i in reversed(range(2, number)):
            if number % i == 0:
                return sum_primes(number-1)
        # 이외엔 소수이므로 합산하여 반환, 재귀
        else:
            return number + sum_primes(number - 1)



# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
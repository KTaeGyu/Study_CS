############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    # 새로운 문자들을 담을 리스트
    new_str = []

    for i in word:
        # 대문자일 경우,
        if 64 < ord(i) < 91:
            # 범위를 넘어가면 - 26 + num) 만큼 빼서 아스키 코드를 계산
            if ord(i) + num > 90:
                new_str.append(chr(ord(i) - 26 + num))
            # 이외에는 그냥 + num 하여 리스트에 추가
            else:
                new_str.append(chr(ord(i) + num))
        # 소문자일 경우,
        elif 96 < ord(i) < 123:
            # 범위를 넘어가면 - 26 + num) 만큼 빼서 아스키 코드를 계산
            if ord(i) + num > 122:
                new_str.append(chr(ord(i) - 26 + num))
            # 이외에는 그냥 + num 하여 리스트에 추가
            else:
                new_str.append(chr(ord(i) + num))

    # 새로운 리스트에 담긴 문자들을 조합하여 반환
    code = ''.join(new_str)
    return code
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def make_answer(security_str, security_code):
    # 코드 문자를 담을 리스트
    code_lsit = []

    # 코드를 이용하여 문자열의 인덱스로 접근하여 리스트에 추가
    for i in security_code:
        code_lsit.append(security_str[i])

    # 리스트의 코드들을 연결하여 반환
    code = ''.join(code_lsit)
    return code
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4,11,17,21,24])
    print(answer)   # => SSAFY
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
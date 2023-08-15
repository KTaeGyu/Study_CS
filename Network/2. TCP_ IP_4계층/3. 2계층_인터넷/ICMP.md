#### [전체 목차로 돌아가기](../../README.md)
## 1. ICMP 프로토콜
1. ICMP(인터넷 제어 메세지 프로토콜)가 하는 일
    - 네트워크 컴퓨터 위에서 돌아가는 운영체제에서 **오류 메세지**를 전송받는 데 주로 쓰인다.<br><br>
2. ICMP 프로토콜의 구조<br>
        <figure>
        <img src="../../imgsrc/ICMP.PNG" width="500">
        </figure>
    - Type, Code (1, 1): 오류 메세지의 대분류와 소분류
    - Checksum (2): 헤더 오류 검사용 코드
    - Others<br><br>
3. Type, Code<br>
        <figure>
        <img src="../../imgsrc/ICMP_TypeCode.PNG" width="500">
        </figure>
    - 0, 8 : 응답, 요청
    - 3 : 경로상 요청 문제 (라우터 문제 등)
    - 11 : 상대방 문제 (방화벽 등)
    - 5 : 라우팅 테이블 원격 수정 (보안)
    
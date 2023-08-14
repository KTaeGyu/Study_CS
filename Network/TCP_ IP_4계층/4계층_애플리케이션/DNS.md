## 1. 정의
- 도메인 이름과 IP 주소를 매핑해주는 서버<br>
    <figure>
    <img src="../../imgsrc/DNS_concept.png" width=350>
    </figure>

## 2. 주소 매핑 과정
- DNS 서버에서는 다음과 같은 순서로 매핑을 진행한다.<br>
    <figure>
    <img src="../../imgsrc/DNS_mapping.jpg" width=500>
    </figure>
1. 클라이언트에서 host파일, 캐시를 확인한다.
2. 클라이언트에서 로컬 DNS 서버로 DNS 주소를 보낸다. (ex, www.naver.com)
3. 로컬 DNS 서버에서 루트 도메인을 검색하여 정보를 얻음 (ex, .com/.net/.org/etc...)
4. 로컬 DNS 서버에서 최상위 레벨 도메인을 검색하여 정보를 얻음 (ex, naver/google/etc...)
    - 레벨 루트 도메인은 여러번 검색하기도 함(ex, .co.kr)
5. 로컬 DNS 서버에서 호스트 레벨 도메인을 검색하여 정보를 얻음 (ex, www/ftp/etc...)
6. 정보를 토대로 IP 주소를 얻어내서 클라이언트에 전달
7. 클라이언트는 IP 주소를 이용하여 서버와 통신

## DNS 관련 명령어
1. ipconfig/displaydns
    - DNS 캐시 정보 확인<br><br>
2. ipconfig/flushdns
    - DNS 캐시 정보 삭제
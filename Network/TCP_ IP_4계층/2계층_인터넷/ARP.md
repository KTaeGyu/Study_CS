## 1. MAC 주소
### MAC 주소란?
- MAC 주소는 데이터 링크 계층(Data Link Layer)에서사용되는 주소로, LAN(Local Address Network)에서 목적지와통신하기 위한 실질적인 주소이다.
- 48bit의 16진수를 사용한다. (ex, 1A-2F-BB-76-09-AD)
- IEEE(전기 전자 기술자 협회)에서 관리하고 할당하며, 모든 네트워크 장비 혹은 컴퓨터의 NIC(네트워크 인터페이스 카드)에 고유한 MAC 주소가 부여된다.
- 또한, MAC 주소는 특별한 프로그램을 통해 변경이 가능하다.<br><br>
### MAC 주소의 필요성
```
IP 주소(논리적 주소) = 배송지 주소
MAC 주소(물리적 주소) = 주민번호
```
- 같은 IP 주소더라도 MAC 주소가 다르다면 구별이 가능하다.
- 그러나, 라우팅 테이블의 과부하를 막기 위해 IP 주소를 함께 이용하는 것이 좋다.<br><br>

## 2. ARP 프로토콜
1. ARP가 하는 일
    - LAN 통신을 하기 위해 필요한 MAC 주소를 IP 주소를 이용해서 알아오는 프로토콜<br>
        <figure>
        <img src="../../imgsrc/ARP_MAC_IP.jpg" width = 300>
        </figure>
2. ARP 프로토콜의 구조<br>
        <figure>
        <img src="../../imgsrc/ARPProtocol.PNG" width="500">
        </figure>
    - Hardware Type, Address Length (2, 1): 2계층의 프로토콜 타입과 길이 (이더넷 : 0001, 06)
    - Protocol Type, Address Length (2, 1): 소스 프로토콜에서 사용하는 프로토콜 타입과 길이 (IPv4 : 0800, 04)
    - Opcode (2): 요청(01)인지 혹은 응답(02)인지를 나타내는 코드
    - Source/Destination Hardware/Protocol Address (6, 6, 4, 4): 출발지/목적지의 MAC/IP 주소

## 3. ARP 프로토콜의 통신 과정
1. 요청
    1. ARP 요청 : 모르는 목적지 MAC 주소를 0- 으로 작성
    2. Ethernet 캡슐화 : 모르는 목적지 MAC 주소를 F- 로 작성하여 브로드캐스트 유도<br><br>
2. 스위치
    1. 2계층 확인 후 브로드캐스팅
    2. 각 PC에서 3계층 확인 후 IP 주소가 맞지 않으면 버리고, 맞으면 응답<br><br>
3. 응답
    1. ARP 응답 : 자기 MAC 주소화 함께 Opcode=02 작성
    2. Ethernet 캡슐화 : 목적지 MAC (기존 소스 MAC) 작성<br><br>
4. 기존 PC에서 ARP 캐시 테이블에 저장<br><br>
        <figure>
        <img src="../../imgsrc/ARPComm.PNG" width="450">
        </figure>

## 4. ARP 테이블
- 나와 통신했던 컴퓨터들을 일정 기간동안 ARP 테이블에 주소를 저장한다.<br>
    <figure>
    <img src="../../imgsrc/ARPCashtable.PNG" width="300">
    </figure>

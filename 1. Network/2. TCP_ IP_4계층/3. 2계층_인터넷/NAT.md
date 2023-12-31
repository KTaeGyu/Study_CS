#### [전체 목차로 돌아가기](../../README.md)
## 1. NAT
### NAT란?
- 패킷이 라우팅 장치를 통해 전송되는 동안 패킷의 IP 주소 정보를 수정해 IP 주소를 다른 주소로 매핑하는 방법
- IP 패킷의 TCP/UDP 포트 숫자와 소스 및 목적지의 IP 주소 등을 재기록하면서 라우터를 통해 네트워크 트래픽을 주고 받는 기술을 말한다. 즉, **바뀐 정보를 기록하는 기술**<br><br>

### 장단점
- 보안 : 내부 네트워크에서 사용하는 IP 주소와 외부에 드러나는 IP 주소를 다르게 유지할 수 있기 때문에 내부 네트워크에 대한 어느 정도의 보안이 가능해진다
- 단점: 여러 명이 동시에 인터넷을 접속하게 되므로 실제로 접속하는 호스트 숫자에 따라서 접속 속도가 느려질 수 있다.

### 예시
- 사설IP 와 공인IP<br>
        <figure>
        <img src="../../imgsrc/NAT.png" width="400">
        </figure>
    - IPv4 주소 체계만으로는 많은 주소들은 감당하지 못하는 단점이 있고, 이를 해결하기 위해 NAT로 공인 IP와 사설 IP로 나눠서 많은 주소를 처리함
    - NAT를 쓰는 이유는 주로 여러 대의 호스트가 하나의 공인 IP 주소를 사용하여 인터넷에 접속하기 위함이다. 예를 들어 인터넷 회선 하나를 개통하고 인터넷 공유기를 달아서 여러 PC를 연결하여 사용할 수 있는데, 이것이 가능한 이유는 인터넷 공유기에 NAT 기능이 탑재되어 있기 때문이다. 
- NAT 관련 소프트웨어 : ICS, RRAS, Net filter

## 2. 포트포워딩
1. 포트포워딩이란?
    - 패킷이 라우터나 방화벽같은 네트워크 장비를 지나는 동안 **특정 IP주소와 포트 번호의 통신 요청을 특정 다른 IP와 포트 번호로 넘겨주는** 네트워크 주소 변환(NAT)의 응용이다.<br>
        <figure>
        <img src="../../imgsrc/Portforwarding.PNG" width="400">
        </figure>

#### [전체 목차로 돌아가기](../../README.md)
## 1. IP 주소 체계
- IPv4 : 32 비트를 8비트의 단위로 점을 찍어 표기
- IPv6 : 64 비트를 16비트의 단위로 점을 찍어 표기<br><br>
- IPv4로나타낼수있는IP 주소는약43억개이다. 인터넷의 보급에 따라 43억개로는 부족해지기시작했고, 그 해결책으로 생각해낸게 IPv6이다.
- 서서히 IPv6로 변모하는 추세이나, 현재까지는 IPv4가 더 많이 쓰이고 있다.

## 2. 일반적인 IP 주소
1. Classful IP 주소
    - 초기에는 클래스로 구분하는 클래스 기반 할당 방식(CIDR)을 사용했다.
    - 앞부분을 네트워크 주소, 뒷부분을 호스트 주소로 사용한다.<br>
        <figure>
        <img src="../../imgsrc/ClassfulIPAddress.PNG" width="500">
        </figure>
    - 클래스별로 네트워크 대역을 나눠 **낭비가 심하다.**
    - 이를 보완하기 위해 DHCP, IPv6, NAT 등이 등장했다.<br><br>
2. Classless IP 주소<br>
        <figure>
        <img src="../../imgsrc/ClasslessIPAddress.PNG" width="500">
        </figure>
    - 서브넷 마스크를 이용하여 네트워크 대역과 기기를 구분함<br><br>
3. 사설IP와 공인IP
    - 사설IP : 같은 네트워크 대역(LAN)에서 사용하는 IP
    - 공인IP : 외부 네트워크 대역(WAN)으로 나갈 때 사용하는 IP<br>
        <figure>
        <img src="../../imgsrc/PrivateIP_PublicIP.PNG" width="280">
        </figure>
    - NAT(Network Address Translation)가 필요

## 3. 특수한 IP 주소
1. 0.0.0.0 (Wildcard)
    - 나머지 모든 IP를 의미<br><br>
2. 127.0.0.X
    - 자기 자신을 나타내는 IP 주소<br><br>
3. 게이트웨이 주소
    - 일반적으로 공유기의 IP
    - LAN에서 WAN으로 나갈때 이용하는 IP
    - 사설IP 대역에서 가장 낮거나 가장 높은 IP 주소를 사용<br>
        <figure>
        <img src="../../imgsrc/Gateway.PNG" width="300">
        </figure>

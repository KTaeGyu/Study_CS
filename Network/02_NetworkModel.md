# 2. 네트워크 모델

## 2-1. 네트워크 모델의 종류
1. TCP/IP 모델
    - 현재의 인터넷에서 컴퓨터들이 주고받는데 쓰이는 통신 프로토콜의 모음<br>
        <figure>
        <img src="./imgsrc/TCP_IP_Model.PNG" height="200">
        </figure>
2. OSI 7계층
    - ISO에서 표준으로 지정한 모델<br>
        <figure>
        <img src="./imgsrc/OSI_7Layer_InDetail.PNG" height="200">
        </figure>

## 2-2. 두 모델 비교
1. 공통점
    - 계층적 네트워크 모델
    - 계층간 역할 정의
2. 차이점
    - 계층의 수 차이
    - OSI는 역할 기반, TCP/IP는 프로토콜 기반
    - OSI는 통신 전반에 대한 표준
    - TCP/IP는 데이터 전송기술 특화

## 2-3. 네트워크를 통해 전달되는 데이터, 패킷
1. 패킷이란?
    - 네트워크 상에서 전달되는 데이터를 통칭하는 말로, 네트워크에서 전달하는 데이터의 형식화된 블록이다.<br>
        <figure>
        <img src="./imgsrc/BasicPackit.PNG" width="350">
        </figure>
2. 캡슐화
    - 여러 프로토콜을 이용해서 최종적으로 **보낼 때** 패킷을 만드는 과정<br>
        <figure>
        <img src="./imgsrc/PackitEncapsulation.PNG" height="200">
        </figure>
3. 디캡슐화
    - 패킷을 **받았을 때** 프로토콜들을 하나씩 확인하면서 데이터를 확인하는 과정<br>
        <figure>
        <img src="./imgsrc/PackitDecapsulation.PNG" height="200">
        </figure>
4. 계층별 패킷의 이름 PDU(Protocol Data Unit)<br>
        <figure>
        <img src="./imgsrc/PDU.png" height="140">
        </figure>

<br>

<figure>
<img src="./imgsrc/02_NetworkModel.png" width="600">
</figure>
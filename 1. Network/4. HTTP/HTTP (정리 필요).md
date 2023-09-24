#### [전체 목차로 돌아가기](../README.md)
## 1. HTTP 프로토콜
### 웹을 만드는 기술들<br>
<figure>
<img src="../imgsrc/Stacks_for_Web.PNG" width="400">
</figure>

- HTTP : 웹 표준을 전송하는 프로토콜
- HTML, Javascript, CSS : 웹 표준, 웹 페이지의 내용, 기능, 디자인
- ASP/ASP.NET, JSP, PHP : 서버에서 실행되는 코드 (MS, Java, PHP 기반 언어)
- DB : 데이터 베이스<br><br>

### HTTP 프로토콜 이란?
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜이다. 웹에서 이루어지는 모든 데이터 교환의 기초이며, **클라이언트-서버 프로토콜**이기도 하다.
- TCP/IP 기반으로 되어있으며, 연결 상태를 유지하지 않는 비연결성 프로토콜이다. 따라서, 프로토콜이라**request**(요청) / **response**(응답) 방식으로 동작한다.
    - 클라이언트가 HTTP request를 서버에 보내면 서버는 HTTP response를 보내는 구조<br>
        <figure>
        <img src="../imgsrc/client server.png" width=350>
        </figure>

### HTTP의 특징
1. 간단함
    - 사람이 읽을 수 있게 간단하게 고안되었다.<br>
2. 확장 가능성
    - HTTP 헤더를 통해 새로운 기능 추가할 수 있음<br>
3. Stateless (상태가 없음)
    - HTTP는 상태를 저장하지 않는다. 즉, 동일한 연결에서 연속하여 전달된 두 개의 요청 사이에 연결고리가 없다.<br>
    - 쿠키와 세션:
        - HTTP의 핵심은 상태가 없는 것이지만 HTTP 쿠키는 상태가 있는 세션을 만들도록 해준다.
        - 헤더 확장성을 사용하여, 동일한 문맥 또는 동일한 상태를 공유하기 위해 각각의 요청들에 세션을 만들도록 HTTP 쿠키가 추가된다.<br>
4. HTTP의 연결
    - 연결은 전송 계층에서 제어되므로 근본적으로 HTTP 영역 밖이다. 다만, 그저 신뢰할 수 있거나 메시지 손실이 없는(최소한의 오류는 표시) 연결을 요구할 뿐이다.
    - HTTP는 연결이 필수는 아니지만 연결 기반인 TCP 표준에 의존한다. 즉, 클라이언트와 서버가 HTTP를 요청/응답으로 교환하기 전에 여러 왕복이 필요한 프로세스인 TCP 연결을 설정해야 한다.
    - 구체적인 연결 방식은 HTTP 버전에 따라 달라진다.<br>

### HTTP의 기능
1. 캐시
    - 캐시란, 데이터나 값을 미리 복사해 놓는 임시 장소를 가리킨다.
    - HTTP를 이용하면 문서가 캐시되는 방식을 제어할 수 있다.
    * 서버는 캐시 대상과 기간을 프록시와 클라이언트에 지시할 수 있고 클라이언트는 저장된 문서를 무시하라고 중간 캐시 프록시에게 지시할 수 있다.<br>
2. origin 제약사항 완화하기
   * 스누핑과 다른 프라이버시 침해를 막기 위해, 브라우저는 웹 사이트 간의 엄격한 분리를 강제하기 때문에 **동일한 origin**으로부터 온 페이지만이 웹 페이지의 전체 정보에 접근할 수 있다
   * 위와 같은 제약 사항은 서버에 부담이 되지만 HTTP 헤더를 통해 그것을 완화시킬 수 있다.<br>
3. 인증
   * 기본 인증은 HTTP를 통해 [`WWW-Authenticate` (en-US)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate "Currently only available in English (US)") 또는 유사한 헤더를 사용해 제공되거나, HTTP 쿠키를 사용해 특정 세션을 설정하여 이루어질 수도 있다.<br>
4. 프록시와 터널링
   * 서버 혹은 클라이언트 혹은 그 둘 모두는 종종 인트라넷에 위치하며 다른 개체들에게 그들의 실제 주소를 숨기기도 한다. HTTP 요청은 네트워크 장벽을 가로지르기 위해 프록시를 통해 나가게 된다.
   * *주의* : 모든 프록시가 HTTP 프록시는 아님<br>
5. 세션
   * HTTP가 기본적으로 상태없는 프로토콜임에도 세션을 만들어줌을 통해 쿠키 사용은 서버 상태를 요청과 연결하도록 해준다.<br>

### HTTP의 흐름
1. TCP 연결을 연다
2. HTTP 메시지를 request
3. 서버에 의해 전송된 response를 읽는다
4. 연결을 닫거나 다른 요청들을 위해 재사용된다<br>
    <figure>
    <img src="../imgsrc/HTTP_v1.1.PNG" width="300">
    </figure>

## 2. HTTP 요청 프로토콜
### HTTP 요청 프로토콜이란?
- 클라이언트가 서버에게 어떠한 동작을 요청하기 위해 보내는 정보
### HTTP 요청 프로토콜의 구조
- **Request Line (중요!!)**, 헤더, 공백, 바디로 구성된다.<br>
    <figure>
    <img src="../imgsrc/HTTP_Request.PNG" width="150">
    </figure>
- Request Line의 구조:<br>
    <figure>
    <img src="../imgsrc/HTTP_RequestLine.PNG" width="400"><br>
    <img src="../imgsrc/reqeust.png" width=400>
    </figure>

### 요청 타입 
- 요청 프로토콜의 가장 앞에 오는 Method type<br>
    <figure>
    <img src="../imgsrc/HTTP_RequestType.PNG" width="350">
    </figure>
- GET : 클라이언트가 서버에게 데이터를 요청, 전송도 가능
- POST : 클라이언트가 서버에 테이터를 전송, 요청도 가능
    - GET vs. POST : GET은 URI에 데이터를 포함시켜서 보내게 되고, POST는 BODY에 포함되어 되돌아온다. 즉, **데이터 보안**과 연관되어 있다.<br>
        <figure>
        <img src="../imgsrc/get post.png" width=500>
        </figure>

### URI (Uniform Resource Identifier)
- 인터넷 상에서 특정 자원을 나타내는 유일한 주소
- 형식:
    ```
    scheme://host[:port][/path][?query]

    1. scheme: 프로토콜
    2. host[:port] : IP[:port] or 도메인주소
    3. [/path] : 파일/폴더 경로
    4. [?query] : 파일에 전달할 변수들
    ```

## 3. HTTP 응답 프로토콜
### HTTP 응답 프로토콜의 구조
- **Status Line (중요!!)**, 헤더, 공백, 바디로 구성된다.<br>
    <figure>
    <img src="../imgsrc/HTTP_Response.PNG" width="150">
    </figure>
- Status Line의 구조:
    <figure>
    <img src="../imgsrc/HTTP_ResponseLine.PNG" width="300"><br>
    <img src="../imgsrc/response.png" width=400>
    </figure>

### 상태 코드
- Status Line 중간에 오는 상태를 표시하는 코드들로, 보통 서버에서 설정해놓는다.<br>
    <figure>
    <img src="../imgsrc/HTTP_ResponseStatus.PNG" width="350"><br>
    <img src="../imgsrc/HTTP_ResponseStatusInDetail.PNG" width="350">
    </figure>


## 4. HTTP 헤더 포멧
### HTTP의 요청 헤더 vs 응답 헤더 구조
- 일반, 요청, 응답, 항목 헤더로 나뉜다.<br>
    <figure>
    <img src="../imgsrc/HTTP_Header.PNG" width="400">
    </figure>
1. 일반 헤더<br>
    <figure>
    <img src="../imgsrc/HTTP_HeaderGeneral.PNG" width="400">
    </figure>
2. 요청 헤더<br>
    <figure>
    <img src="../imgsrc/HTTP_HeaderRequest.PNG" width="400">
    </figure>
3. 응답 헤더<br>
    <figure>
    <img src="../imgsrc/HTTP_HeaderResponse.PNG" width="400">
    </figure>

## 5. HTTP 기반 시스템의 구성요소
- 각각의 개별적인 요청들은 서버로 보내지며, 서버는 요청을 처리하고 *response*라고 불리는 응답을 제공한다. 이 요청과 응답 사이에는 여러 개체들이 있는데, 예를 들면 다양한 작업을 수행하는 게이트웨이 또는 캐시 역할을 하는 프록시등이 있다.
- 실제로는 브라우저와 요청을 처리하는 서버 사이에는 좀 더 많은 컴퓨터들이 존재한다. (ex. 라우터, 모뎀) 
- 웹의 계층적인 설계로 이들은 네트워크와 전송 계층 내로 숨겨진다. HTTP은 애플리케이션 계층의 최상위에 있다.<br>
    <figure>
    <img src="../imgsrc/client-server-chain.png" width=550>
    </figure>

### 구성요소
1. 클라이언트 : 사용자 에이전트 
    - 사용자 에이전트 : 사용자를 대신하여 동작하는 모든 도구 - 주로 브라우저에 의해 실행
    - 브라우자는 항상 요청을 보내는 개체
2. 웹 서버
    - 통신 채널의 반대편에는 클라이언트에 의한 요청에 대한 문서를 제공하는 서버가 존재
    - 서버는 논리적으로는 단일 기계이다
    - 그러나 로드(로드 밸런싱) 혹은 그때 그때 다른 컴퓨터(캐시, DB 서버, e-커머스 서버 등과 같은)들의 정보를 얻고 완전하게 혹은 부분적으로 문서를 생성하는 소프트웨어의 복잡한 부분을 공유하는 서버들의 집합일 수도 있다.
    - 서버는 반드시 단일 머신일 필요는 없지만, 여러 개의 서버를 동일한 머신 위에서 호스팅 할 수는 있다. 
        - HTTP/1.1과 Host 헤더를 이용하여, 동일한 IP 주소를 공유할 수도 있다
3. 프록시
   - 웹 브라우저와 서버 사이에서는 수많은 컴퓨터와 머신이 HTTP 메시지를 이어 받고 전달한다. 여러 계층으로 이루어진 웹 스택 구조에서 이러한 컴퓨터/머신들은 대부분은 전송, 네트워크 혹은 물리 계층에서 동작하며, 성능에 상당히 큰 영향을 주지만 HTTP 계층에서는 이들이 어떻게 동작하는지 눈에 보이지 않는다. 이러한 컴퓨터/머신 중에서도 애플리케이션 계층에서 동작하는 것들을 일반적으로 **프록시**라고 부른다.
    - 프록시 : 서버와 클라이언트 사이에서 대리러 통신을 수행해주는 것
    - 프록시 서버 : 위 기능을 하는 서버
    - 사용 목적 / 이유
        1. 캐싱
            - 프록시 서버 중 일부는 프록시 서버에 요청된 내용을 캐시를 사용해 저장해두는데, 캐시에 저장되어 있는 내용에 대한 재요청은 서버에 따로 접속할 필요가 없이 저장된 내용 그대로 돌려주면 되기 때문에 전송 시간 줄일 수 있고 외부 트래픽을 줄여서 네트워크 병목 현상을 방지할 수 있다.
        2. 보안 / 인증
            - 프록시 서버가 중간에 경유하게 되면 IP를 숨기는 것이 가능하기 때문에 프록시 서버를 방화벽으로 사용하기도 한다.
        3. 접속 우회
        4. 필터링 (바이러스 백신 스캔, 유해 컨텐츠 차단)
        5. 로드 밸런싱 (여러 서버들이 서로 다른 요청을 처리하도록 허용)
        6. 로깅 (이력 정보를 저장)

출처 : https://developer.mozilla.org/ko/docs/Web/HTTP/Overview\
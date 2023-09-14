## 목차

1. 운영체제란?
2. 운영체제의 목적
3. 운영체제의 기능
4. 운영체제의 분류
5. 운영체제 예시

# 1. 운영체제란?
- 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층<br>
    <figure>
    <img src="./images/OS.PNG" width=300>
    </figure>
- 사용자가 하드웨어에 대한 지식이 부족하더라도 편리하게 사용할 수 있도록 도와주는 역할을 한다.<br><br>

# 2. 운영체제의 목적
1. 컴퓨터 시스템을 **편리하게 사용할 수 있는 환경을 제공**
    - 컴퓨터 한대를 여러명의 사용자(or 프로그램)가 사용해도 불편함이 없도록 함
2. 컴퓨터 시스템의 **자원을 효율적으로 관리** (중요!)
    - 자원 : CPU, 메모리, I/O 장치
    - 고려사항 : 효율성, 형평성<br><br>

# 3. 운영체제의 기능
- 컴퓨터 시스템의 기본 구조<br>
        <figure>
        <img src="./images/PCSystem.PNG" width=500>
        </figure>
    - 구성 : CPU, 메모리, I/O 장치(디스크, 키보드, 마우스, 모니터 등)
1. CPU 스케줄링 : 각 프로그램에게 CPU 사용권한 부여 순서 결정
2. 메모리 관리 : 한정된 메모리의 할당을 결정
3. 디스크 스케줄링 : 디스크에서 들어온 요청의 처리순서 결정
    - CPU와 다르게 물리적인 헤드가 있기 때문에 스케줄링 방식이 다름
4. 인터럽트, 캐싱 : CPU와 I/O 장치 사이의 속도 차이를 극복하기 위한 기능<br><br>
- I/O 스캐줄링<br>
        <figure>
        <img src="./images/IOSchedule.PNG" width=600>
        </figure>
    - 입출력 큐에 순서대로 작업을 수행 (I/O 장비에서도 필요할 때 큐에 추가)
    - 사람과 상호작용하는 프로그램 / I/O 작업 없이 CPU를 오래 사용하는 프로그램으로 나눌 수 있음

### 3-1. CPU 스케줄링
1. FCFS(First-Come-First-Served)<br>
        <figure>
        <img src="./images/FCFSScheduling.PNG" width=600>
        </figure>
    - 먼저 요청한 프로그램 먼저 처리
    - 앞선 프로세스가 CPU 사용시간이 길다면 평균 대기시간이 늘어난다.
    - 공평할순 있으나, 효율적이진 않음
2. SJF(Shorted-Job-First)<br>
        <figure>
        <img src="./images/SJFScheduling.PNG" width=600>
        </figure>
    - 평균 대기시간이 가장 짧은 방법
    - 그러나 CPU를 할당받지 못하는 기아현상이 일어날 수 있음
    - 효율적일순 있으나, 형평성이 어긋남
3. RR(Round-Robin)<br>
        <figure>
        <img src="./images/RRScheduling.PNG" width=600>
        </figure>
    - 프로세스가 한번에 CPU를 사용할 수 있는 시간이 정해져있는 방식
    - 사용시간이 실수록 프로세스는 기다리는 시간이 길어지게 된다.
    - 현재 가장 많이 사용되는 방식

### 3-2. 메모리 관리
- 디스크의 **파일시스템**에서 각 실행파일이 메모리에 올라가서 프로세스가 된다.
- 이 때, **가상 메모리**를 형성하는 단계를 거쳐 올라가게 된다.<br>
        <figure>
        <img src="./images/MemorySchduling.PNG" width=600>
        </figure>
    - 메모리는 가상메모리에서 당장 필요한 부분만 가져와서 올려놓게 된다.
    - 이 때, 메모리가 다 차게되면 안되기 때문에 사용하지 않는 메모리는 디스크의 **스왑영역**에 저장된다.
        - 전원이 꺼질 경우, 파일시스템은 기존과 같은 역할이지만, 스왑영역은 데이터는 남아있으나 의미가 없는 데이터가 된다.<br><br>
- LRU vs. LFU<br>
        <figure>
        <img src="./images/MemorySchdulingEX.PNG" width=600>
        </figure>
    1. LRU (가장 오래 전에 참조한 페이지 삭제) : 1번 삭제
    2. LFU (참조 횟수가 가장 적은 페이지 삭제) : 4번 삭제
        - 최근에는 둘을 보완한 방법도 연구되고 있다.

### 3-3. 디스크 스케줄링
- 디스크의 구조와 디스크 큐<br>
        <figure>
        <img src="./images/DiskQueue.PNG" width=600>
        </figure>
    - 디스크에서 데이터를 읽을 때 가장 시간이 오래걸리는 부분은 헤드의 이동이다.
    - 따라서 헤드의 이동시간을 최소화 하는 방법이 필요하다.<br>
        <figure>
        <img src="./images/DiskScheduling.PNG" width=600>
        </figure>
    - 디스크 접근시간 구성요소 : 탐색시간(중요!), 회전지연, 전송시간
        - 탐색시간을 최소화하기 위해서는 탐색거리를 줄이는게 중요하다!
- FCFS(First-Come-First-Served)<br>
        <figure>
        <img src="./images/DiskFCFS.PNG" width=600>
        </figure>
    - 헤드의 이동거리 효율이 너무 낮음
- SSTF(Shortest-Seek-Time-First)<br>
        <figure>
        <img src="./images/DiskSSTF.PNG" width=600>
        </figure>
    - 헤드의 이동거리 효율은 좋으나, 기아현상이 발생할 수 있음
- SCAN<br>
        <figure>
        <img src="./images/DiskSCAN.PNG" width=600>
        </figure>
    - 헤드는 요청과 상관없이 일정한 스캔을 진행함

### 3-4. 저장장치 계층구조와 캐싱
- 저장장치 계층구조<br>
        <figure>
        <img src="./images/MemoryStructure.PNG" width=600>
        </figure>
    - CPU 내부에 아주 작은 메모리인 레지스터
    - 메인 메모리와 레지스터 차이의 속도 차이를 극복하기 위해 캐시메모리를 둔다.
    - 메인메모리 아래는 하드디스크와 같은 디스크가 존재함
        ```
        Primary     Secondary
        고속        저속
        고가        저가
        휘발성      비휘발성
        Read(사용)  Write(저장)
        ```
    - 캐싱은 중간에 저장할 곳을 두어 재사용성을 높인 기술을 말한다.<br><br>
- 플래시메모리<br>
        <figure>
        <img src="./images/FlashMemory.PNG" width=600>
        </figure>
    - 단점 : 쓰기 횟수 제한, 데이터 변질 등 하드웨어적 약점 (소프트웨어적으로 보완중)
    - 장점 : 속도, 휴대성, 견고함<br><br>

# 4. 운영체제의 분류


# 5. 운영체제 예시
- 서버용, PC용, 스마트디바이스용 운영체제가 나뉜다.
- 공개 소프트웨어 : 리눅스, 안드로이드<br>
    <figure>
    <img src="./images/OpenOS.PNG" width=500>
    </figure>
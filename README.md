# 환경 설정

### 가상 환경 생성
```
python -m venv venv
```

- venv : Python 가상 환경을 생성할 때 사용되는 디렉터리
    - 프로젝트별로 독립된 python 환경 제공
    - 서로 다른 프로젝트 들이 의존성이나 라이브러리 버전에 영향을 받지 않도록 함.

### 가상 환경 활성화
- Windows
```
venv\Scripts\activate
```

- macOS 및 Linux
```
source venv/bin/activate
```

- 프롬프트에 (venv)가 표시되어 현재 가상 환경이 활성화된 상태임을 알 수 있음.

![image](https://github.com/user-attachments/assets/e477cc0d-d021-49dc-9594-86e63194ba9b)

### 파이썬 패키지 관리자 최신 버전으로 업그레이드
```
pip install --upgrade pip
```

### FastAPI 설치
```
pip install fastapi
```

### Pydanctic과 starlette
![image](https://github.com/user-attachments/assets/4f65f7d5-0dff-41b2-8af9-e1becd1bba35)
- <b>pydantic</b>
    - 데이터 유효성을 검사하고 데이터 모델을 생성할 때 사용하는 라이브러리
    - 요청 본문 데이터나 쿼리 매개변수 등을 검증하는 데 사용
- <b>starlette</b>
    - 웹 애플리케이션의 기반을 제공하는 ASGI 프레임워크
    - 요청 라우팅과 처리를 수행

### uvicorn 설치
```
pip install "uvicorn[standard]"
```
- uvicorn과 함께 standard 옵션에 포함된 추가 패키지들이 설치
- <b>uvicorn</b>
    - FastAPI와 같은 비동기 웹 프레임워크의 애플리케이션을 실행하기 위해 사용되는 ASGI 서버
    - <b>ASGI(Asynchronous Server Gateway Interface)</b>: 비동기 웹 애플리케이션을 실행할 수 있도록 돕는 Python의 표준 인터페이스 

### VSCode Python 환경 설정
- Ctrl + Shift + P (macOS: Cmd + Shift + P)를 눌러 명령 팔레트 열기
- Python: Select Interpreter를 입력하여 선택
- 프로젝트 폴더에 있는 가상 환경(venv)의 파이썬 인터프리터 경로 선택
    - .\venv\Scripts\python.exe <i>(Windows)</i>
    - ./venv/bin/python <i>(macOS/Linux)</i>
![ezgif-4-d51a9387de](https://github.com/user-attachments/assets/e2e0344f-53a1-401d-a236-9017882e5db6)


---

### 참고 링크

- [Beginners FastAPI - 40 min](https://youtu.be/O05PucyQYBg?feature=shared)
- [공식 문서 - FastAPI](https://fastapi.tiangolo.com/#sponsors)
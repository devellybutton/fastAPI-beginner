> - Installation
> - A very simple endpoint
> - GET List Endpoint
> - GET Single Object Endpoint
> - Handling Errors
> - Query Parameters
> - Delete Endpoint
> - Create Endpoint & Pydantic Schema
> - Update Endpoint

-----

# Installation

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

<details>
<summary>venv 폴더와 gitignore 지정</summary>

![image](https://github.com/user-attachments/assets/e477cc0d-d021-49dc-9594-86e63194ba9b)

</details>

### 파이썬 패키지 관리자 최신 버전으로 업그레이드
```
pip install --upgrade pip
```

### FastAPI 설치
```
pip install fastapi
```

### Pydanctic과 starlette
- <b>pydantic</b>
    - 데이터 유효성을 검사하고 데이터 모델을 생성할 때 사용하는 라이브러리
    - 요청 본문 데이터나 쿼리 매개변수 등을 검증하는 데 사용
- <b>starlette</b>
    - 웹 애플리케이션의 기반을 제공하는 ASGI 프레임워크
    - 요청 라우팅과 처리를 수행
<details>
<summary>터미널에서 FastAPI 설치</summary>

![image](https://github.com/user-attachments/assets/4f65f7d5-0dff-41b2-8af9-e1becd1bba35)

</details>

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
<details>
<summary>VSCode Command Palatte</summary>

![ezgif-4-d51a9387de](https://github.com/user-attachments/assets/e2e0344f-53a1-401d-a236-9017882e5db6)

</details>

-----

# A very simple endpoint

### 서버 실행
```
uvicorn main:app --reload
```
- <b>`uvicorn`</b> : FastAPI는 ASGI 기반이기 때문에 uvicorn을 사용해 애플리케이션을 실행
- <b>`main.app`</b> : 경로, 특정 파일(main.py)에 정의된 객체(app)
- <b>`--reload`</b> : 개발 모드, Node.js의 nodemon과 비슷한 기능의 워치 모드

### API 명세서 자동 생성

- <b>Swagger UI</b> : `http://<서버주소>/docs`
- <b>ReDoc</b> : `http://<서버주소>/redoc`

<details>
<summary>ReDoc 브라우저상 화면</summary>

![image](https://github.com/user-attachments/assets/075703e9-bc19-44a2-83c2-9f3bd5b1af17)

</details>
<details>
<summary>Swagger 브라우저상 화면</summary>

![image](https://github.com/user-attachments/assets/98cf6f43-6e8f-4389-8318-74d9b8573b30)

</summary>

---

# GET List Endpoint

```
courses = {
	1: {
		"title": "Modern History",
		"teacher": "Ms.Doe",
		"students": ["Harry Potter", "Frodo Baggins"],
		"level": "advanced"
	},
	2: {
		"course": "Mathematics",
		"teacher": "Mr. Davies",
		"students": ["John Smith", "Bruce Lee"],
		"level": "beginner"
	},
	3: {
		"title": "Geography",
		"teacher": "Mr. Apple",
		"students": ["Michael Jordan", "Bruce Lee"],
		"level": "advanced"
	}
}

@app.get("/api/courses")
def get_courses():
    return courses
```

---

### 참고 링크

- [Beginners FastAPI - 40 min](https://youtu.be/O05PucyQYBg?feature=shared)
- [공식 문서 - FastAPI](https://fastapi.tiangolo.com/#sponsors)
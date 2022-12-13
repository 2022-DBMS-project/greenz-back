# Greenz

- 2022 데이터베이스 시스템 교과목에서 진행한 GREENZ 프로젝트입니다.
- 비건 제품을 판매하고, 비건 제품 관련 레시피와 레스토랑을 확인할 수 있습니다.

### Django 실행 방법
1. 데이터베이스 설정
    1) pip install mysqlclient
    - 라이브러리 설치하기
    2) touch my_settings
    - manage.py 파일이 있는 폴더(프로젝트 최상단)에 my_settings 파일 만들어주기
    3) my_settings 파일에 데이터베이스 정보 넣기
    ```
   DATABASES = {   
        'default': {   
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '데이터베이스 이름',
            'USER': '사용자',
            'PASSWORD': '비밀번호',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }
   ```
<br>

2. 모델 적용하기   
    1) python manage.py makemigrations   
    2) python manage.py migrate   
    

3. `python manage.py runserver` 로 Django 실행


4. 웹 브라우저에 `http://127.0.0.1:8000/greenz/` 입력하기

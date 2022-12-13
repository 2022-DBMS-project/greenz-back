# Greenz

- 2022 데이터베이스 시스템 교과목에서 진행한 GREENZ 프로젝트입니다.
- 비건 제품을 판매하고, 비건 제품 관련 레시피와 레스토랑을 확인할 수 있습니다.

### Django 실행 방법
1. 데이터베이스 설정
- manage.py 파일이 있는 폴더(프로젝트 최상단)에 my_settings 파일 넣어주기
- my_settings 파일에는 데이터베이스 정보 등 개인정보를 담기
   
2. 모델 적용
- python manage.py makemigrations
- python manage.py migrate

3. Django 실행
- python manage.py runserver

4. 웹페이지 띄우기
- 웹 브라우저에 http://127.0.0.1:8000/greenz/ 입력하기

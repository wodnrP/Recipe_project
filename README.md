# Recipe_project
![rdicon2](https://github.com/wodnrP/Recipe_project/assets/102155143/7d4bc5e3-0b14-4a54-8745-8cf1a3d1ed7a)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FwodnrP%2FRecipe_project&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## RD : RecipeProject APP v1.0
> 경상국립대 경영정보학과 박재욱 [@wodnrP](https://github.com/wodnrP)
> 
> 개발기간: 2023.02 ~ 2023.05

## 배포주소
> 백엔드 : https://rdproject.site (현재 서버 중단)
> 
> 프론트 : flutterflow apk file 배포

## 프로젝트 소개
RecipeProject(이하 [RD](https://github.com/wodnrP/Recipe_project))는 요리 애호가들을 위한 간편한 레시피 저장 및 공유 앱입니다.

요리가 취미일 정도로 다양한 요리 레시피에 많은 관심이 있었는데, 현재 레시피를 찾기 위해서는 여러 웹페이지를 찾아 다녀야하고 각종 광고와 기타 판매
물품도 함께 보이는 경우가 많아 다소 복잡하고 번잡하다는 점을 느꼈습니다. 그래서 음악 플레이리스트 처럼 간편한 레시피 저장소를 만들고자 개발하게 
되었습니다. 

*누구나 쉽게 참여하여 자신만의 레시피를 기록하고, 다양한 요리 아이디어를 발견할 수 있는 이 앱에서 요리의 재미를 더해보세요*

## Stacks
### Environment
<img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=flat-square&logo=VisualStudioCode&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>

### Development
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=ffffff"/> <img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=ffffff"/>
<img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=flat-square&logo=Amazon EC2&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat-square&logo=Amazon S3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=flat-square&logo=Amazon RDS&logoColor=ffffff"/> <img src="https://img.shields.io/badge/FlutterFlow-02569B?style=flat-square&logo=Flutter&logoColor=ffffff"/>

### Design & Document
<img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=Figma&logoColor=ffffff"/>

------------
## 🖥️ 화면 구성
|메인 페이지|로그인 후, 메인 페이지|조회 페이지|
|:---:|:---:|:---:|
|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 45 45" src="https://github.com/wodnrP/Recipe_project/assets/102155143/a12d6dcb-9caa-4845-99a4-8b3ab5e8f838">|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 52 31" src="https://github.com/wodnrP/Recipe_project/assets/102155143/6122e042-4476-42a7-b18f-59f5bebfbf0c">|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 47 24" src="https://github.com/wodnrP/Recipe_project/assets/102155143/45d9ed95-98ce-46a9-bcea-08ce5f130e17">|
|로그인 페이지|회원가입 페이지|마이 페이지|
|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 47 31" src="https://github.com/wodnrP/Recipe_project/assets/102155143/475d3c22-2bc6-40a8-b389-bdc56d144324">|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 47 48" src="https://github.com/wodnrP/Recipe_project/assets/102155143/b856263f-ec0b-4ca9-bb37-d15563cd9b07">|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 50 05" src="https://github.com/wodnrP/Recipe_project/assets/102155143/622a2658-d965-43b1-ab0e-93b02b7dc2ff">|
|레시피 작성 페이지|저장된 레시피 페이지|상세 조회 페이지|
|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 48 33" src="https://github.com/wodnrP/Recipe_project/assets/102155143/654e3933-41a5-4f4f-8bfd-947e7dcf85b6">|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 59 48" src="https://github.com/wodnrP/Recipe_project/assets/102155143/7c20ae1f-5a07-43e9-a355-64c9121ce1cf">|<img width="200" height="350" alt="스크린샷 2023-05-25 오후 9 51 16" src="https://github.com/wodnrP/Recipe_project/assets/102155143/6e9ca8aa-f854-4b5e-b0ab-b445d42c34e7">|
------------
## 📌 주요 기능
### ⭐️ 레시피 저장 기능
- 사용자가 원하는 레시피를 저장할 수 있는 기능
- 저장된 레시피는 카테고리별 Dropdown을 통해 필터링하여 조회가능 
### ⭐️ 상세 조회한 레시피 좋아요 기능
- 레시피 상세 페이지에서 사용자가 원하는 레시피의 좋아요 수 증가 기능 
- 레시피를 좋아요한 수와 저장한 수, 조회한 수를 계산하여 인기 레시피 TOP10선정
### ⭐️ 원하는 레시피 검색기능
- 레시피 제목을 기준으로 검색어가 포함되는 레시피를 모두 검색
- 검색된 레시피는 최신순으로 정렬되어 제공
------------
## 📋 API 명세
| API | HTTP Method | End Point | Query String | Description |
| -- | -- | -- | -- | -- | 
| SignupAPIView  | POST | /user/signup |   | 회원가입 |
| LoginAPIView | POST | /user/login |   | 로그인 |
| LogoutAPIView | POST | /user/logout |   | 로그아웃  | 
| UserAPIView | GET | /user/<int:id> or /user/ |   | 유저 정보 조회 | 
| UserAPIView | PATCH | /user/ |   | 유저 정보 수정 | 
| PopularRecipe | GET | /top |   | 인기TOP10 레시피 조회 | 
| AllRecipe | POST | / |   | 레시피 작성 | 
| AllRecipe | GET | / | ?search=title&items=  | 전체 레시피 조회 | 
| AllRecipe | PATCH | /recipe_id |   | 레시피 수정 | 
| AllRecipe | DELETE | /recipe_id |   | 레시피 삭제 | 
| MyRecipe | POST | /storage/recipe_id |   | 레시피 저장 | 
| MyRecipe | DELETE | /storage/recipe_id |   | 저장 레시피 삭제 |
| MyRecipe | GET | /storage/ | ?sort=category | 저장 레시피 조회 | 
| RecommendAPIView | POST | /like/recipe_id |   | 추천 수 증감 기능 | 
| detailGetAPIView | GET | /detail/recipe_id |   | 조회수 증감, 상세 레시피 조회 | 
------------
## 아키텍쳐
### 📂 디렉토리 구조
> #### Recipe_project
> - app
>   - config : settings.py 민감 정보 분리
>   - recipe : recipe 관련 api 작성
>   - storage : 저장한 레시피 관련 api 작성
>   - user : 유저 관련 api 작성
>   - staticfiles
>   - manage.py
> - db
>   - conf.d
>   - data
> - nginx
>   - Dockerfile : nginx dockerfile
>   - project.conf
> - Dockerfile : django app dockerfile
> - docker-compose.yml
> - requirements.txt
> - .gitignore
> - README.md  
------------
## ERD
<img width="589" alt="스크린샷 2023-05-30 오후 6 08 15" src="https://github.com/wodnrP/Recipe_project/assets/102155143/6386a013-7d20-4b16-9411-37551635f80a">

------------
## 배포 인프라
<img width="785" alt="배포인프라" src="https://github.com/wodnrP/Recipe_project/assets/102155143/ea8fa157-6474-49d9-9b6b-4e4dde71748f">

____________

## 📝 개선할 사항
1. 이번 프로젝트에서 front-end개발은 FlutterFlow라는 tool을 활용했습니다. 특성상 ios와 android 모두 호환이 가능하여 선택했으며 ios를 기준으로 개발을 진행했으나, android에서 검색 화면이 깨지는 오류가 발생하여 해결하지 못한 점이 아쉬웠습니다. 다음 버전 개발은 flutterflow가 아닌 flutter 혹은 다른 기술 스택을 활용하여 에러를 잡을 예정입니다. 
2. 레시피 데이터가 많이 쌓일 경우, 레시피 조회 API의 Latency가 늦어질 것으로 예상됩니다. 현재는 쿼리파라미터의 페이지네이션을 이용해 적용 전 보다 2배 가량 감소시켰지만, 조금 더 획기적으로 Latency를 줄일 수 있는 개선이 필요합니다.  

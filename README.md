# BlogProject

## 주제
- 현재는 별도로 정해진 것이 없음(~23.07.17)


## 이슈
- 23.07.18 AM 09:00 가상환경이 정상적으로 실행되지 않아 프로젝트를 처음부터 다시 구성
  - AM 10:50 기존 blog 기능 구현 및 정상 동작 확인
- 23.07.18 AM 11:03 createsuperuser의 로그인이 안 되는 현상
  - AM 11:24 Error의 원인을 확인하던 중 staff권한이 False로 된 것을 수정 후 models.py에서 createsuperuser의 param을 확인 후 수정
- 23.07.18 PM 15:16 Auth_view를 바탕으로 한 로그인&로그아웃을 구현하는 중 로그인의 경우 redirect되는 곳을 변경해야하고, 로그인 여부를 확인하여 로그아웃을 가능하게 해야하는데 로그아웃의 기능 구현이 미흡함. 로그아웃 버튼 클릭 시 403에러 발생(CSRF Token missing)

## 진행상황
- blog 기능 구현 : blog/post의 list, detail
- blog 기능 미구현 : 카테고리 설정, 검색, 수정(user 등록 후), comment와 hashtag출력 
- user 기능 구현 : auth_view 바탕의 로그인 로그아웃 일부 구현
- user 기능 미구현 : user관련 권한 및 views 구현중


## 파일 구조


## 기능 설명


##
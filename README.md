# flaskProj
## 기능
### 회원가입
- [x] 이메일 중복여부 체크
- [ ] 회원가입 후 로그인 바로 되야함
- [ ] error 떠도 form에 글 유지되어야함
### 로그인 
- [x] 이름과 비밀번호로 로그인
- [ ] login 데코레이터 생성
### 게시판 글목록
- [x] 게시판 글 목록 띄우기
- [x] 게시판 글 자세히 보기 링크 추가
- [ ] 페이징 기능 추가
- [ ] 정렬 기능 추가 
### 게시판 글자세히 보기
- [ ] 조회수
- [ ] 추천수
### 게시판 글올리기
- [x] 로그인 상태일때만 가능해야함
- [x] 유저 아이디가 게시판 글의 ForeignKey key로 설정
### 게시판 글 수정, 삭제
- [x] 게시판 글 수정은 글쓴이만 가능해야함
- [x] 글 수정 버튼은 글쓴이만 보여야함
- [x] 글 삭제는 글 수정 페이지에서 클릭가능해야함. 다만 다시 새션을 통해서 검증필요
### 댓글 올리기
- [x] 게시판 글 자세히 보기에 추가
### 댓글 삭제
- [x] 댓글 모델은 유저와 연결되어야 함
- [x] 댓글 쓴 사람만 삭제 버튼 보이고 삭제 가능
### 프론트앤드
- [x] 메뉴 바 스크롤따라 이동
## 설치
* requirements.txt 참고
* docker + mysql
## history
* 회원가입 기능 추가 20231204
* 로그인 기능 추가 20231204
* 게시판 목록 기능 추가 20231205
* 게시판 글 자세히보기 기능 추가 20231205
* 게시판 글 쓰기 기능 추가 20231205
* 게시판 글 수정, 삭제 기능 추가 20231206
* 댓글 쓰기, 삭제 기능 추가 20231207
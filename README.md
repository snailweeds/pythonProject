# 3주 회고록
* 가상환경과 패키지
가상환경: 프로젝트별로 패키지들을 담을 공구함(격리된 실행환경)으로 공구함1에 A, B', C를 담아두고, 공구함2에 B, C, D, E를 담아 쓸 수 있음
가상환경을 통해 재구성할 필요 없이 원하는 패키지를 담은 공구함을 따로 만들면 된다는 장점!
File/PyCharm>Settings>Project>Python Interpreter>(+)>Find Package and Install It!
* 주의사항
태그 안의 텍스트를 찍고 싶을 땐 → 태그.text
태그 안의 속성을 찍고 싶을 땐 → 태그['속성']
* 선택자를 사용하는 방법 (copy selector)
soup.select('태그명')
soup.select('.클래스명')
soup.select('#아이디명')
soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')
* 태그와 속성값으로 찾는 방법
soup.select('태그명[속성="값"]')
* 한 개만 가져오고 싶은 경우
soup.select_one('위와 동일')
* 주의사항
함수 안에 변수 입력할 때 '' 빼먹지 말기
.text가 통하지 않을 때에는 None이 있는지 확인하기
* MongoDB
DB 확인: Chrome>localhost:27017
robo3T: DB내부를 살펴보기 위한 프로그램(MongoDB는 GUI를 제공하지 않기 때문에 이를 통해 확인)
MongoDB 시작: Robo 3T>MongoDB Connections>Create
DB: 쌓아두기
RDBMS(SQL): 행/열의 생김새가 정해진 엑셀에 데이터를 저장하는 것과 유사, 정형화되어 있는 만큼, 데이터의 일관성이나 / 분석에 용이
No-SQL: 딕셔너리 형태로 데이터를 저장해두는 DB, 데이터 하나 마다 같은 값들을 가질 필요 X, 자유로운 형태의 데이터 적재에 유리한 대신 일관성 부족
MongoDB 사용법: Python Interpreter>(+)>Find pymongo and Install It
robo3T에서 View Table Mode를 누르면 편하게 볼 수 O
* 주의사항
Insert: 한번 실행시킬 때마다 삽입되어 쌓임

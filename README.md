# repo_node

## sequelize
* routes에 login/sign-in 삽입하여 jwt를 이용한 인증 진행 미비..

lecture, evaluation - db table 제작
CRUD 기능 예제 적용해 놓음

## crowling ( crowling_python3 / crowling.py )
* timestamp pytho3 에서 찍을 때 sequelize에서 설정한 데이터 모델과 자료형 설정 문제..

크롤링에서
lecture_id = GEB1111-001 ( 학수번호 + 분반 번호 )
lecture_code = GEB1111 (학수번호)
instructor = 홍길동

distinct_id = GEB1111홍길동 (lecture_code + instructor)

XXX1234-001 2016 - 1 OS - 송민석
XXX1234-002 2016 - 1 OS - 송민석
XXX1234-001 2017 - 1 OS - 송민석
XXX1234-002 2017 - 1 OS - 송민석
XXX1234-003 2017 - 1 OS - 김아무개

=> XXX1234 OS - 송민석
   XXX1234 OS - 김아무개

이런 식으로 unique하게 만들었습니다.


### TABLE LECTURE

lecture_id = 학수 번호 + 분반 번호 .. ex)GEB1111-001

lecture_title = 강의 이름 .. ex) 오퍼레이팅 시스템

   grade = 학년 .. ex) 1학년

   credit = 학점 .. ex) 3.0 학점

   class_type = 과목구분 ex) 전공선택 / 전공필수 / 교양필수..

   eval_method = 평가방법 ex) 절대평가 / 상대평가

   place = 장소.. sugang.inha.ac.kr 기준 시간 및 강의실 그대로 긁어 온 것 ...ex) 수20,21,22(60주년-207)

   instructor = 담당 교수  ex) 송민석..

   remarks = 비고  ex) 미래융합대학.. ?? 없어도 될 것 같기도?

   lecture_time = D1T1T2T3 ... 형태로 요일+교시로 강의 시간이 저장되어 있음



### TABLE EVALUATION

   lecture_code = 과목 코드 ex)GEB1111
   
   lecture_title = 강의 이름
   
   instructor = 담당 교수
   
   eval_method = 평가 방법
   
   class_type = 과목구분
   
   grade = 학년
   
   credit = 학점
   
   major = 전공 (고유 코드값으로 저장됨)
   
   predict_rating 
   
   rating
   
   MAE
   
   distinct_id = (lecture_code + instructor)
   
---------------------

+ 테이블 논의 필요
1. timestamp - sequelize 에서 선언한 변수형과 python3에서 테이블에 삽입하는 변수형이 달라 보류해두었습니다.
2. 년도와 학기에 대한 선언이 없는데, 학기에 대한 필요성은 없는 것 같아, 1번 문제가 해결되면 즉시 바로 삽입해버리면 될 것 같습니다.

  -------------------
아래는 mysql table create문 입니다.

   CREATE TABLE evaluation ( 
           id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
           lecture_code varchar(255) NOT NULL,
           lecture_title varchar(255) NOT NULL,
           instructor varchar(50) NOT NULL,
           eval_method varchar(50) NOT NULL,
           class_type varchar(50) NOT NULL,
           grade varchar(50) NOT NULL,
           credit varchar(10),
           major varchar(255) NOT NULL, 
           predict_rating double(255,0) NULL,
           rating  double(255,0) NULL,
           MAE  double(255,0) NULL,
           distinct_id varchar(50) NOT NULL,
           UNIQUE(distinct_id),
           PRIMARY KEY (`id`) 
           );


   ----------------------------------------—————

   CREATE TABLE lecture ( 
           id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
           lecture_id varchar(255) NOT NULL,
           lecture_title varchar(255) NOT NULL,
           grade varchar(50) NOT NULL,
           credit int(1) unsigned NOT NULL,
           class_type varchar(255), 
           place varchar(255), 
           instructor varchar(255) NOT NULL, 
           eval_method varchar(255) NOT NULL, 
           remarks varchar(255) NOT NULL, 
           lecture_time varchar(255) NOT NULL, 
           PRIMARY KEY (id)
           );

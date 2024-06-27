## 데이터베이스(DataBase)

- 중복을 없애고 자료를 구조화 하여 기억시켜 놓은 자료의 집합체

### 특징

- 실시간 접근성 : 사용자의 요구를 즉시 처리할 수 있다.
- 지속적인 변화 : 정확한 값을 유지하려고 삽입, 삭제, 수정 작업 등을 이용해 데이터를 지속적으로 갱신할 수 있다.
- 동시 공유 : 사용자마다 서로 다른 목적으로 사용하므로 동시에 여러 사람이 동일한 데이터에 접근하고 이용할 수 있다.
- 내용에 대한 참조 : 저장한 데이터 레코드의 위치나 주소가 아닌 사용자가 요구하는 데이터의 내용, 즉 데이터 값에 따라 참조할 수 있어야 한다.

# DBMS(DataBase Management System)

- 데이터베이스 내의 데이터를 접근할 수 있도록 해주는 소프트웨어
- 사용자 또는 다른 프로그램의 요구를 처리하고 응답하여 데이터를 사용할 수 있도록 함.
- 일반적으로 DB라고 부름
- DBS(Database Syetem) DB + DBMS 등의 전체 시스템

### 장점

1. 데이터 중복 최소화
2. 데이터 독립성이 확보
3. 데이터를 동시 공유
4. 데이터 보안이 향상
5. 데이터 무결성을 유지
6. 장애 발생 시 회복 가능

### 단점

1. 비용이 많이 발생
2. 백업과 회복 방법이 복잡
3. 중앙 집중 관리로 인한 취약점이 존재

### 기능

1. 정의 : 모든 응용 프로그램들이 요구하는 데이터 구조를 지원하기 위해 데이터베이스에 저장될 데이터의 형(Type)과 구조에 대한 정의, 이용 방식, 제약 조건 등을 명시하는 기능이다.
2. 조작 : 데이터 검색, 갱신, 삽입, 삭제 등을 체계적으로 처리하기 위해 사용자와 데이터베이스 사이의 인터페이스 수단을 제공하는 기능이다.
3. 제어 : 데이터베이스를 접근하는 갱신, 삽입, 삭제 작업이 정확하게 수행되어 데이터의 무결성이 유지되도록 제어해야한다.

### 종류

1. PostgreSQL : SQL 언어를 사용하는 오픈 소스 객체RDBMS
2. MySQL : 세계에서 가장 많이 쓰이는 오픈소스 RDBMS
3. SQLite : 서버가 아닌 응용프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스 시스템
4. Oracle : 대기업에서 주로 사용하며 점유울 1위인 유료 데이터베이스 시스템

# SQL(Structured Query Language, 구조적 질의 언어)

### DDL(Data Definition Language, 데이터 정의 언어)

- 각 릴레이션을 정의하기 위해 사용하는 언어
- CREATE, ALTER, DROP, ...

### DML(Data Manipulation Language, 데이터 조작 언어)

- 데이터를 추가, 수정, 삭제 하기 위한 데이터 관리를 위한 언어
- SELECT, INSERT, UPDATE

### DCL(Data Control Language, 데이터 제어언어)

- 사용자 관리 및 사용자별로 릴레이션 또는 대ㅔ이터를 관리하고 접근하는 권한을 다루기 위한 언어
- GRANT, REVOKE

# ORM(Object Relational Mapping)

- 객체 관계 매핑
- 객체 지향 프로그래밍에서, 객체와 관계형 데이터베이스를 연결해준다. ⇒ 객체답게 모델링을 하면 매핑 작업이 늘어난다.
- 객체와 관계형 데이터베이스의 차이
    1. 상속
    2. 연관관계
        1. 객체는 참조를 사용 (getter)
        2. table은 FK를 사용
    3. 데이터 타입
    4. 데이터 식별 방법
        1. SQL로 member 객체를 같은 id 값으로 조회해도, member1과 member2는 다르다.
        2. 자바 collection에서 조회하면 같다.
        3. 
    
    - 계층형 아키텍처
        - 진정한 의미의 계층분할이 어렵다.

### 장점

1. 생산성 향상, 비즈니스 로직 집중
2. 재사용 및 유지보수 용이
3. DBMS에 종속되지 않음.

### 단점

1. 프로젝트가 복잡한 경우 난이도 상승
2. Raw Query 보다 성능이 낮음.

# RDBMS

- Codd의 12가지 규칙을 최대한 따르는 DataBase
- Table(Relation)의 형태로 데이터를 저장한다.
- 관계형 연산자로 테이블 형태로 데이터를 반환
- Primary Key에 따라 데이터 성능이 달라진다.

관계형데이터베이스 서버(서버 소프트웨어, 물리서버) < = > 서버에 접속하기 위한 클라이언트 

```python
insert into post(title, content, writer)
values('Hello my sql', 'THis is first time', 'unan');

select * from post;

insert into post(title, content, writer)
values('Hello my rdb', 'I\' using my sql', 'unan');

select * from post where id = 1;

select * from post where writer like 'un%';

update post set title = 'Hello Update!' where id = 2;

delete from post where id = 2; 

truncate post;
# inner join
# outer join
```

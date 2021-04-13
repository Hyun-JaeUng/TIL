# AWS



## SQL (4/13)

* SQL (Structured Query Language) 

* CRUD -> Create, Read, Update, Delete 

  * C : insert into 테이블명 [(컬럼명리스트, ...)] values (데이터값 리스트, ...) 

  * U : update 테이블명 set 컬럼명=컬럼값, ... [where 조건식]

  * D : delete [from] 테이블명 [where 조건식]

    --------------------> commit, rollback

  * R : select 컬럼명,...

       [ from 테이블명

    ​     where 조건식 (없으면 무조건 모든 행)

    ​	 group by 그룹핑 기준컬럼, ...

    ​     having 그룹조건

    ​     order by 정렬기준컬럼[desc], ... ]

    *  [] 안에 아규먼트는 생략 가능. (DB에 따라 from절은 생략 불가능한 경우도 있음)

* ex)
  * select now(); --> 마리아 DB (from절 생략 가능)

  * select sysdate from dual; --> 오라클 DB (from절 필수)

  * select * from t where empno = 100

  * select * from t where empno != 100

  * select * from t where ename = 'King' --> 문자열 데이터 값을 표현 시 반드시 단일인용부호만 ('')

  * select * from t where ename = 'King' or ename = 'Kang' or ename = 'Kong'

  * select * from t where ename in ('King', 'Kang', 'Kong')

  * select * from t where ename like 'K%'

    * %: 0개 이상의 임의의 문자를 의미함.

    * _: 임의의 한 문자 뜻함.

       

* sql 학습 1 자료 공부함
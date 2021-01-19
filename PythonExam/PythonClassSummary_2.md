# 파이썬 수업

> 2주차 파이썬 수업 정리 및 요약



## Day 6 (0111)

> 딕셔너리, 세트 이론 공부 및 예제
>
> 함수 정리 + 실습 1개
>
> 객체 개념 등장

* 시퀀스형: 문자열, 튜플, 리스트 
  * len, max,min, count 사용 가능
  * for _ in `해당자리`: 갈 수 있음
* 리스트 함수: del 인덱스, remove, pop, append, insert, extend
* 튜플, 문자열은 `불변`, 리스트 `변경 가능`



### 딕셔너리

* 딕셔너리에 키 값은 중복되면 안됨!! 

* 값은 중복될수 있음

* 특정 값 호출 방법: `dic_name[key]`

* 딕셔너리의 내용을 얻기 위해서는 `items()`, `keys()`, `values() ` 메소드를 사용

* ```python
  dic = {키1: 값1, 키2: 값2, 키3: 값3}
  ```

* 재 할당(값 변경)과 데이터 추가 가능

  * `dic_name[key] = value` 하면 해당 키와 값 데이터 추가됨

* item() 는 딕셔너리의 모든 키와 값을 튜플로 묶어서 반환

* key는 변경이 불가능한 자료형들 => int, float, tuple, str로만 만들어짐



### 세트 (Set)

* **순서는 없고 중복되지 않는 여러 개의 데이터를 담는 상자**

* 변화 가능 (삭제나 변경 가능)
* 세트 = 집합 개념

* set 생성 
  * 빈 세트: `set()` (유일한 방법)
  * 하나 이상 값 있을 때: `{a,b}` + 위에 방법
  * 딕셔너리에 set() 를 사용하면 키만 사용함
* 합집합 -> 함수: union -> a|b
* 교집합 -> intersection -> a&b
* 차집합 -> difference -> a - b
* 합집합 - 교집합 (배타적인 원소) -> exclusive -> a^b
* set 추가 시에는 `set_name.add(값)` 으로 추가 (append가 아닌 add다.)
  *  이미 값이 있으면 추가 안되고 (중복 불허), 다만 오류나지는 않음
* `set_name.update([30 50 40])` : 이미 있는 것 빼고 여러 개 추가
* 삭제는 remove, 길이는 len

* 포함관계로 부등호 성립하기도 함 (집합 개념 가져왔다 생각)



### 함수 정리

* 지역변수: 함수 안에서만 사용, 전역변수: 프로그램 전체에서 사용 (`global x`)

* 가변인수는 인수 목록의 마지막에 와야 함. (`def intsum (s, *int)`)
* 파이썬은 인수의 활용방법에 따라서 3가지로 나뉨
  * 일반 인수
  * 가변 인수 (`*매개변수명`)
  * 키워드 가변 인수 (`**매개변수명`) , 별 2개 붙임
    * 키워드 자유롭게 설정 가능하다....! 
  * 일반 -> 가변 -> 키워드 인수 순서임

* 일반적인 포지션 아규먼트가 있고, 키워드 아규먼트도 있음
* 디폴트 매개변수 (매개변수에 기본값 지정)
* 재귀함수는 함수를 계속 호출하는거라 반복문으로 해결하는게 더 좋음



### functest 21 ~ 25

* 기본값을 가지는 기본인수(매개변수) 는 가변인수 뒤에 있어도 괜찮음
  
* 그 외에는 꼭 기본인수가 앞으로 가야한다.
  
* ```python
  def calcscore(name, *score, **option): # 이 인수 순서가 이상적
      print(name)
      sum = 0
      for s in score:
          sum += s
      print("총점 :", sum)
      if (option['avg'] == True ):
          print("평균 :", sum / len(score))
  
  calcscore("김상형", 88, 99, 77, avg = True)
  ```

* 가변 아규먼트는 값 형태가 튜플로 나오고, 키워드 아규먼트는 딕셔너리로 나옴 (키워드가 키, 값이 값)

* *arg -> 튜플 , **arg -> 딕셔너리



### 실습

* 반복문이 언제 끝날지 횟수가 명확하지 않을 때는 while을 사용하고, 멈추는 조건을 설정
* ans.sort() : 오름차순
* `hp = ["A","B","C","D"]   # 자주 까먹는 것: 문자를 넣을 때 꼭 따옴표 붙이기`

* chr(65) = A도 활용가능함

* ```python
  dic = {'월':(-12,-3),'화':(-4,2),'수':(-8,8),'목':(-3,5),
         '금':(-7,7),'토':(-13,-3),'일':(-6,-2)}
  
  day = input("요일명을 한글로 입력하세요: ")
  
  if day in dic.keys():
      print(day,"요일의 최저온도는", dic[day][0], "이고 최고 온도는", dic[day][1], "입니다." )
  else:
      print(day, "요일의 정보를 찾을 수 없습니다.")
  ```

  * dictionary 생성과 값이 여러 개 일때는 보이는 것처럼 튜플을 사용하기



### 객체 

* 파이썬은 객체지향 프로그래밍 언어
* 지금까지 학습한 문자열, 리스트, 튜플, 딕셔너리, 집합은 모두 콜렉션 객체들임
* 연산자를 사용하여 각 객체가 가지고 있는 함수(메서드) 호출이 가능하다.
* 객체 = 속성 + 기능
  * 객체 = 변수 + 함수
* `객체를 담고있는 변수. 멤버`
* 객체에 속한 함수를 메서드라고 함



## Day 7 (0112)

> 객체, 자료형의 컴프리헨션, 출력 (format), 패킹/언패킹, 문자열 메서드 공부했음. 
>
> 많은 양을 공부했고, format 부분 보충이 필요함! 

### 문자열 매서드

* len 함수: 메서드가 아닌 함수로 되어있음 
* `isalpha` 와 같이 is로 시작하는 메서드들은 리턴값이 bool 형임 (True, False)
* `lstrip`, `rstrip`,`strip` 메서드
  
* 왼쪽, 오른쪽, 양측 공백을 제거
  
* 메서드: 클래스에 소속된 함수

  * 객체에 대해 특화된 작업 수험

* in 구문: 특정 문자 유무 여부를 조사함 (있으면 True, 없으면 False) (`not in`도 있음)

* lower 메서드/ upper 메서드 (문자열 메서드임)

* 메서드는 사용 시 `객체.메서드()` , 함수의 경우 `함수(객체)` 임

  * s.lower() : 메서드
  * len(s) : 함수

* 문자열 메서드 - 분할: `split 메서드`

  * 구분자를 기준으로 문자열을 분할하여 리스트 생성함
  * 기본은 공백, 설정하려면 s2.split("->") 와 같이 설정 가능

* `splitlines 메서드`: 개행 문자나 파일 구분자 등 기준으로 문자열 잘라 리스트로 만듬

* `join 메서드` : 문자열의 각 문자 사이에 다른 문자열 끼워 넣음

  * ```python
    s = "._."
    print(s.join("대한민국"))
    
    # 대._.한._.민._.국
    ```

* `replace 메서드`: 특정 문자열을 찾아 다른 문자열로 대체

* find 메서드와 index 메서드의 차이

  * 해당 값을 못 찾을때 find는 `-1` 리턴하고, index는 에러남

* `startswith`, `endswith` 메서드

  * 김으로 시작하는 것 있으면 True
  * .jpg로 끝나는거 있으면 True

* ```python
  # =============== split 과 join  ===============
  s2 = "서울->대전->대구->부산"
  city = s2.split("->")
  print(" 찍고 ".join(city))
  ```


### 포맷팅 

> 방법이 몇 개 있음

* 문자열 사이사이에 다른 정보를 삽입하여 조립하는 기법

#### format % value

* | 표식 |   설명    |
  | :--: | :-------: |
  |  %d  |   정수    |
  |  %f  |   실수    |
  |  %s  |  문자열   |
  |  %c  | 문자 하나 |
  |  %h  |  16진수   |
  |  %o  |   8진수   |
  |  %%  |  % 문자   |

* 서식: `%[-]폭[.유효자리수]서식`

* 최근에는 **f - Strings** 방법 이용하는게 요즘 좋음

### formatTest 1 ~ 5

``` python
# ===== format  =====
price = 500
print("궁금하면 %d원!" % price)

# ===== format2  =====
month = 8
day = 15
anni = "광복절"
print("%d월 %d일은 %s이다." % (month, day, anni)) # 여러 개일때 튜플로
```

* **align**: `%5d`, `%-5d` 와 같이 폭을 나타낼 수 있다. 글자 남으면 공백이 생김 
  * -5는 5칸인데 글자를 왼쪽 붙임, 5는 5칸인데 오른쪽에 붙임
* `%10.8f` 와 같이 소수점 이하 표시 자리수 설정
  * 기본값은 6개 (float)

```python
name = "재웅"
age = 26
height = 180.99

print("이름:{}, 나이:{}, 키:{}".format(name,age,height))
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name,age,height)) # 튜플에 인덱스 표시한 것
print("이름:{0:10s}, 나이:{1:5d}, 키:{2:8.2f}".format(name,age,height))
print("이름:{0:^10s}, 나이:{1:>5d}, 키:{2:<8.2f}".format(name,age,height))
print("이름:{0:$^10s}, 나이:{1:>05d}, 키:{2:!<8.2f}".format(name,age,height))
```

### f-string (파이썬 3.6부터 가능)

  ```python
print(f"이름:{name}, 나이:{age}, 키:{height}") # 변수 직접 넣기, 뒤에는 변수 자료형
print(f"이름:{name:s}, 나이:{age:d}, 키:{height:f}")  
  ```

### 리스트 컴프리헨션

* 리스트에 소속되는 각각의 값을 **요소**라고 함

* 리스트, 딕셔너리, 셋만 컴프리헨션 구문 적용 가능 (튜플은 사용 불가)

* 대괄호 안에 for문과 if문을 적어서 우리가 원하는 리스트를 생성함

* 더 간결한 코드와 빠른 속도로 만들 수 있음

* [값에 대한 수식 for 변수 in 대상 if 조건]

```python
numlist4 = [ num for num in range(1, 6) ] # 리스트 컴프리헨션
print("list4 = {}".format(numlist4))
```

### 리스트 관리 (메서드)

* append는 끝에 추가, insert는 (삽입할 위치, 값)
* 삭제: remove, del, clear (리스트 모든요소 삭제), 빈 리스트 대입 (`score[1:4]= []`)
* 검색: index (위치 찾음), count(요소값의 개수), min, max, in, not in

* `list.sort()`: 리스트 직접 변화
  * list.reverse() : 요소 순서 반대로 정렬
* sorted(리스트) : 정렬된 리스트를 새롭게 하나 생성



### 튜플

* 여러개의 변수에 값을 한꺼번에 대입
  * `tu = "이순신", "김유신", "강감찬"`

* `d,m = divmod(7,3)`  (몫: 2 , 나머지 1)
  * 파이썬 내장함수로 나눅셈의 몫과 나머지를 튜플로 묶어 리턴



### 사전 (딕셔너리)

* `dic[key]` 로  빠른 검색 가능

* 딕셔니리에서 찾는 키가 없을 경우 예외 발생
  * 체크해서 찾기
  * 예외 처리 구문
  * get 메서드 사용

* 사전[키] 할 시 키의 존재여부에 따라 동작이 다름
  * 존재할 경우: 기존 값의 변경
  * 존재하지 않을 경우: 키를 추가 (값도 쌍으로)
* del 
  
  * 해당 키를 찾아 값과 함께 삭제
* 대표 메서드: keys , values, update(두 개 사전을 병합) 
* `dict 함수` : 빈 사전 만들거나 다른 자료형을 사전으로 변환함

* {키와 값에 대한 수식 for 변수 in 대상 if 조건}

  * ```python
    students = dict(둘리=90, 또치=85, 도우너=95, 희동이=75, 마이콜=80)
    
    pass_students = { k : v for k, v in students.items()}
    pass_students = { k : v for k, v in students.items() if v > 80}
    ```



### 집합

* `set 함수` : 빈 집합 만들거나 다른 컬렉션을 집합형으로 변환함

* 집합 컴프리헨션 
  * {값에 대한 수식 for 변수 in 대상 if 조건}
  * 딕셔너리처럼 중괄호임!
* add (append 없음), update(집합끼리 결합하여 합집함, 중복 불허)



### 실습 및 예제

* join시 리스트 안에 요소는 문자열이어야 함 (join은 문자열 객체의 메서드임)

* 지능형 리스트 개념은 많이 배웠으나, 스스로 실습해야 익숙해질 것. 시간이 필요함

* ```python
  def mydict(**n):
      d={}
      for k,v in n.items():
          d['my'+k] = v
      return d
  print(mydict())
  print(mydict(name = "Hyun", age = 26)) # 키워드 가변 아규먼트이므로 자동으로 딕셔너리가 되기 때문에 n.items()로 for문 돌려야함
  
  
  # 딕셔너리를 포문에 그냥 넣으면 key값이 포문 돈다.
  # 위처럼 해야 키 - 값으로 나누어져 돈다.
  # if 변수: 하면 변수가 비어있으면 false라 돌지 않음
  # 즉 len(변수)!=0 말고, if 변수 해도됨
  ```

* ```python
  def myprint (*a, **args):
     deco = '**'
      s = ','
      if 'deco' in args.keys():
          deco = args['deco'] # 딕셔너리[키] = 값
      if 'sep' in args.keys():
          s = args['sep']
      '''deco = args.get("deco", "**")
      s = args.get("sep", ",")'''
  
      result = ''
      if len(a) == 0:
          print("Hello Python")
      else:
          result += deco
          for i in range(len(a)):
              result += str(a[i])
              if i < (len(a)-1):
                  result += s
          result += deco
          print(result)
  
  myprint(10,20,30, deco = "@", sep ="-")
  myprint("python", "javascript", "R", deco = "$")
  myprint("가", "나", "다")
  myprint(100)
  myprint()
  ```

* ```python
  oldlist = [17,2,14,6,10,19,16,12,5]
  newlist1 = [ oldlist ]
  print(newlist1) # 요소가 1개인 이중 리스트 (1행, 10열)
  
  newlist2 = list( [1,2,3,4,5,6,7,8] )
  print(newlist2) # 이중리스트 아니고 일반 리스트
  
  newlist3 = list( (1,2,3,4,5,6,7,8) )
  print(newlist3) # 일반리스트
  
  newlist4 = list( {1,2,3,4,5,6,7,8} )
  print(newlist4)
  
  newlist5 = list( "ABC")
  print(newlist5) # -> ['A','B','C']
  
  newlist6 = [ x for x in range(1, 9) ]
  print(newlist6)
  
  newlist7 = [ x for x in oldlist if x % 2 ] # 2로 나눈 나머지가 0이면 조건식 false, True일 때만 조건성립
  print(newlist7)
  ```

* ```python
  list5 = [ d   if d % 2  else  '짝수' for d in range(1, 16)  ]
  print(list5)
  # else에 해당하는 애들은 "짝수"가 대신 들어감
  
  oldlist = [1, 2, 'A', False, 3]
  newlist = [i * i for i in oldlist if type(i) == int]
  ```

* ```python
  f = []
  print(type(f)) # list
  print(f.extend([1,2,3]))
  print(f.reverse()) # 리스트의 변화를 주는 메서드들인데 자체 리턴값은 None임
  print(f)
  ```

* ```python
  l1 = [1,2,3,4,5]
  l2 = l1  
  # 참조값을 그대로 가져온 것이라 하나의 리스트를 공유하고 있음
  # 즉 l1값 바꾸면 l2도 같이 바뀜. 
  ```

* ```python
  data = [1,2,3,4]
  
  print(data)
  print(*data) # 아규먼트에서도 *을 붙일 수 있음, 리스트 요소 값들을 쪼개서 야구먼트로 전달함!!
  print(data[0], data[1], data[2], data[3])
  
  x,*y,z = [10,20,30,40]
  print(x)
  print(y) # 처음, 마지막 뺴고 모두 y한테 할당
  print(z)
  ```

* ```python
  # 앞에 포문이 바깥 for문 , 중첩된 for문
  listv = [dan * num for dan in range(1, 10) for num in range(1, 10)]
  setv =  { dan * num for dan in range(1, 10) for num in range(1, 10)}
  ```

* 파이썬 강의교안 6에서 지능형 리스트 부분 기억할 것 추가하기 

* get함수 관련 내용도 조사 후 추가해보자! 



## Day 8 (0113)

> comprehension, packunpac, str 실습 제출 후 실습리뷰
>
> 이후 컬렉션 관리 함수, 람다 함수, 컬렉션의 사본 강의 교안 및 예제 리뷰

### 컬렉션 관리 함수

#### enumerate

* 순서값과 요소값을 한꺼번에 구하는 내장함수

* `for i,j in enumerate(리스트, 문자열, 튜플)`
  
  * 인덱스를 i, 값(요소)를 j에 저장함
  
* ```python
  score = [ 88, 95, 70, 100, 99 ]
  for no, s in enumerate(score, 1): # (객체, 숫자), 표시된 숫자부터 연산하며 기본값 0임
      print(str(no) + "번 학생의 성적 :", s)
  
  names = "둘리,고길동,희동이,마이콜,또치,도우너"
  namelist = names.split(",") # 리스트 생성
  print(namelist)
  namelist.sort()
  
  for num, name in enumerate(namelist) :
      print(f"이름순으로 {name}는 {num+1}번입니다.") # f string 사용
      
  for data in enumerate(namelist) :
      print(f"enumerate를 적용한 결과 : {data}") # for문 해당 변수 한개이기에 튜플로 들어옴 (언패킹 안된다 생각)
            
  for num, name in enumerate(namelist, 100) : # 인덱스 숫자 시작, 기본값 0
      print(f"이름순으로 {name}는 {num}번입니다.") 
  
      # {num} 100번부터 시작됨! 
  ```

#### zip

* 여러 개 컬렉션 합쳐서 하나로 만듬

* 두 리스트의 대응되는 요소끼리 짝지어 **튜플 zip 객체** 생성 (zip의 type =>  `zip`)
  * 대응되는 숫자까지만 한다. (뒤에 남는 건 사라짐)
  * 생성되는 튜플의 순서는 원본 리스트의 순서와 같음
  
* 1회성임!
  
  * zip을 한 번 호출하고 다음 번엔 사용이 안된다! (이후 값에 아무값도 없음)
  
* ```python
  zip2 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
  print(list(zip2))
  
  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
  # 출력시 list() 나 dict() 함수 사용해야 함 (아니면 값 말고 <zip object at 0x000001F365A520C0> 이런 값 출력)
  ```

* ```python
  alist = ['a1', 'a2', 'a3']
  blist = ['b1', 'b2', 'b3']
  for i, (a,b) in enumerate(zip(alist,blist)):
      print(i,a,b)
  """
  """
  0 a1 b1
  1 a2 b2
  2 a3 b3
  ```

### 파이썬의 함수는 일급 객체

* 파이썬의 함수는 변수에 저장할 수도 있고, 함수를 담고 있는 변수를 통해서 함수 호출도 됨

* 다른 함수 호출 시 아규먼트로 전달 가능

* 함수의 리턴값으로 전달 가능

* 일반적인 데이터처럼 사용 가능

* ```python
  # 함수 안에 함수 정의, exp는 함수 안에서만 호출가능
  def fct_fac(n) :
      def exp(x) :
          return x**n
      return exp
  
  rtnf1 = fct_fac(2) # 둘 다 함수가 들어온 것
  rtnf2 = fct_fac(3)
  
  print(type(rtnf1)) # function 타입이다.
  print(type(rtnf2))
  print(rtnf1(4))
  print(rtnf2(4))
  print(fct_fac(2)(5))
  print(fct_fac(5)(3)) # 먼저 오는 아규먼트가 처음 바깥쪽 함수 아규먼트, 뒤가 안에 함수 아규먼트
  
  """
  """
  <class 'function'>
  <class 'function'>
  16
  64
  25
  243
  ```

* ```python
  def func2() :
      print("func2 호출 - hello")
  
  print(func2)
  v = func2 # 함수 자체를 넣기위해서는 가로를 빼고 넣어야함. 그래야 리턴값이 아닌 함수가 변수에 저장
  print(v)
  v() # comment
  
  """"""
  <function func2 at 0x000001F365A31AF0>
  <function func2 at 0x000001F365A31AF0>
  func2 호출 - hello
  ```

  * 함수가 저장된 변수에 ()를 넣으니 함수가 호출됨! 그래서 함수 안 코드 실행된 것



### 람다 함수

> 강의 교안 내용 및 예제 코드 리뷰

#### filter 함수

* 아규먼트로 함수 줘야 함

* 리스트 요소 중 조건에 맞는 것만을 골라냄

* 첫 번째 인수: **조건 지정하는 함수**

* 두 번째 인수: 대상 리스트 

* ```python
  # =============== filter  ===============
  def flunk(s):
      return s < 60
  score = [ 45, 89, 72, 53, 94 ]
  for s in filter(flunk, score):
      print(s)
  45
  53
  ```

#### map 함수

* 모든 요소에 대한 변환함수 호출, 새 요소 값으로 구성된 리스트 생성 (기존 리스트값 변경됨!)

* 첫 번째 인수: **값을 변환하는 함수**

* 두 번째 인수: 대상 리스트

* ```python
  # =============== map  ===============
  def half(s):
      return s / 2
  
  score = [ 45, 89, 72, 53, 94 ]
  for s in map(half, score):
      print(s, end = ', ')
  """"""
  22.5, 44.5, 36.0, 26.5, 47.0, 
  
  def total(s, b):
      return s + b
  
  score = [ 45, 89, 72, 53, 94 ]
  bonus = [ 2, 3, 0, 0, 5 ]
  for s in map(total, score, bonus):
      print(s, end=", ")
  """"""
  47, 92, 72, 53, 99, 
  ```

#### 람다 함수

* 이름 없고 입력과 출력만으로 함수를 정의하는 축약된 방법

* **lambda 인수 : 식**
  
  * 인수는 여러 개 가질 수 있음
  * 리턴 값 주면 안됨
  * 람다 함수내에서는 변수 정의 불가
  * 람다 함수내에는 식만 정의 가능
  
* ```python
  score = [ 45, 89, 72, 53, 94 ]
  for s in filter(lambda x:x < 60, score):
      print(s)
  """"""
  45
  53
      
  for s in map(lambda x:x / 2, score):
      print(s, end=", ")
  """"""
  22.5, 44.5, 36.0, 26.5, 47.0, 
  ```

* ```python
  def calc():
      num  = 100
      return lambda : num + 1    # 람다 표현식을 반환
  # 리턴값에서 쓰인 함수의 지역변수는 계속 유지됨 - 클로저
  # 이것도 calc 함수안에 lambda 함수 있는 것임
  
  c1 = calc()
  print(calc()())
  print(c1(), c1(), c1())
  """"""
  101
  101 101 101
  ```

* ```python
  # 아우터 함수와 이너 함수(expr), 첫 소괄호가 바깥쪽 아규먼트, 두번째 소괄호가 이너함수 아규먼트!!!
  def calc():
      a = 3
      b = 5
      def expr(x) :
          return a * x + b
  
      return expr
  # 리턴값으로 쓰여서 이너함수가 계속 유지됨
  c3 = calc()
  print(c3(100), c3(200), c3(300), c3(400), c3(500))
  print(calc()(100))
  """"""
  305 605 905 1205 1505
  305
  ```

### 컬렉션의 사본

>메모리와 서로 변수들이 리스트나 값 공유하는 것에 대한 설명 

#### 리스트의 사본

* 기본형 변수는 대입 이후 둘 중 하나 바꾸어도 다른 쪽에 영향 없음
* 컬렉션의 경우, 같은 리스트를 두 변수가 가리키는 것이라 영향 있음 (리스트) 

#### copy 메서드

* 두 리스트를 완전히 독립 사본으로 만들 수 있음 (`list2 = list1.copy()`)

* ```python
  # =============== listcopy2  ===============
  list1 = [ 1, 2, 3 ]
  list2 = list1.copy()
  list2[1] = 100
  print(list1)
  print(list2)
  
  """"""
  [1, 2, 3]
  [1, 100, 3]
  ```

* 하지만, 리스트가 중첩 리스트라면 그 중첩된 리스트는 또 서로 공유함

  * 해결방법 : deepcopy 이용 (import  copy 후 `copy.deepcopy(list)`)

  * ```python
    # =============== deepcopy2  ===============
    import copy
    list0 = [ "a", "b" ]
    list1 = [ list0, 1, 2 ]
    list2 = copy.deepcopy(list1)
    list2[0][1] = "c"
    print(list1)
    print(list2)
    """"""
    [['a', 'b'], 1, 2] 
    [['a', 'c'], 1, 2] # 딥카피해서 밑에 것만 바뀜
    ```

#### is 연산자

* is 구문 통해 두 변수가 같은 객체 가르키는지 조사. (같은 값과 객체는 다르다! 공간, 메모리 개념)

  * 즉 동일한 id를 가지는가 알려준다고 생각

* 데이터의 값을 비교할 때는 `a is b` 말고 `a == b `써라!!

* ```python
  # =============== is  ===============
  list1 = [ 1, 2, 3 ]
  list2 = list1
  list3 = list1.copy()
  print("1 == 2" , list1 is list2)
  print("1 == 3" , list1 is list3)
  print("2 == 3" , list2 is list3)
  """"""
  1 == 2 True # = 로 같다고 했던 것은 서로 공유해서 true, 카피한 3은 그 둘과 id(메모리 주소) 다름
  1 == 3 False
  2 == 3 False
  ```

#### 리스트의 메모리 관리 방식

* 파이썬은 리스트를 저장할 떄 값 자체가 아니라, 값이 위치한 메모리 주소(reference)를 저장한다.
* == 은 값을 비교하는 연산이고, is는 메모리의 주소를 비교하는 연산이다.
  * 특이한 점: 파이썬은 -5부터 256까지의 정수값을 특정 메모리 주소에 저장한다. 
  * 그리고 해당 숫자를 할당하려고 하면 해당 변수는 그 숫자가 가진 메모리 주소로 연결
  * 즉, 저 범위 안에 값을 할당한 변수들은 같은 메모리 주소를 가진다는 말!
* 리스트는 기본적으로 값을 연속으로 저장하는 것이 아니라 값이 있는 주소를 저장하는 방식이다.
* 이런 방식이여서 중첩리스트도 사용 가능하고, 다양한 형태의 변수가 하나의 리스트에 들어갈 수 있음

 

### 모듈

* 파이썬 코드를 저장하는 기본 단위
* 파이썬에서 자주 사용하는 기능은 표준 모듈로 제공됨
* `import 모듈 [as 별칭]`
* `from 모듈 import 함수명 [as 별칭][,함수명 [ as 별칭]]`
  * 이 경우 import한 함수 외 모듈에 속한 다른 함수 사용 불가

#### math 모듈

#### time 모듈

* 이코테에서 실행 시간 구하는 것도 time 모듈에 의해 구하는 것

#### calendar 모듈

#### random 모듈

* `random.randint(begin, end)` 

	#### os 모듈

#### sys 모듈

* 파이썬 해석기가 실행되는 환경과 해석기의 여러 기능 조회 및 관ㄹ

#### 명령행 인수

* 파이썬에서 실행 파일 뒤에 인수를 전달할 수 있음
* **sys.argv** 읽어 명령행 인수의 값 읽을 수 있음
* `if (len(sys.argv) == 1):` 이렇게 시스템 아규먼트의 갯수에 따라 조건문 구현 가능
* 다만 인수보다는 질문을 하고 직접 입력받아 사용하는 것이 더 정확함



## Day 9 (0114)

> 강의교안 및 stmodule (1~9)
>
> 모듈 내에 대략 어떤 기능을 가진 함수들이 있는지 알기

```python
# =============== import  ===============
import math
print(math.sqrt(2))

# =============== from import  ===============
from math import sqrt
print(sqrt(2))

# =============== import as  ===============
import math as m
print(m.sqrt(2))

# =============== from as  ===============
from math import sqrt as sq
print(sq(2))
```

* import를 모듈단위까지 해도 되고, 더 나아가 함수까지 해도 됨

  * 다만 그에 맞춰서 사용할 때 문법이 조금 달라짐
  * as는 해당 그것을 별칭으로 부른다 생각하면 됨

* ```python
  time.sleep(1) # 해당 시간 만큼 잠깐 실행을 쉬어가는 명령
  ```

  * 크롤링할 때 필요한 경우 있음

* ```python
  import time
  
  start = time.time() # 시작 시간
  for a in range(1000):
      print(a)
  end = time.time() # 끝나는 시간
  print(end - start)
  ```

  * 경과 시간을 알아보는  코드 



## Day 10 (0118)

> 예외처리 구문



### 예외 처리 (Exception)

* 프로그램 코드는 이상이 없으나 실행 중에 불가피하게 발생하는 문제




### 문자셋 (characterset)

* 문자마다 분여한 코드값들을 모아 놓은 것으로 각 문자셋마다 고유 명칭이 있음
* 기억할만한 문자셋 명칭
  * ansi (euc-kr, ksc5601, cp949) - 영문 1바이트 (ASCII값), 한글 2바이트
  * unicode (코드값 통일화)
    * utf-16: 모든 나라의 언어에 코드값을 통일화 시키자, 2바이트로!
    * utf-8: 모든 나라의 언어에 코드값을 통일화 시키자. 1~4바이트로!



## Day 11 (0119)

실습 시간 + 리뷰

파이썬 강의교안 7 (객체, 클래스, 인스턴트화) (다시 다운 - 오타많음)

* 만들고자 하는 프로그램에서 어떤 객체가 필요하면 먼저 그 객체의 멤버들을 모델링(추상화)하여 클래스를 정의함
* p8 요약페이지 잘 정리
* 객체와 인스턴스 거의 똑같은 의미임
* 



### 클래스 정의와 객체 생성

```python
class Student:
    pass

st1 = Student()
st2 = Student()
st3 = Student()
```

* 클래스 내부 메서드의 경우 반드시 첫번째 아규먼트로 self 받아야함.



실습 1

member 클래스 먼저 생성

그 객체가 가지고 있는 멤버변수 사용해서 값 저장 및 꺼내기도 하는 실습 (. 연산자 사용)

실습 2

getbookinfo -> return 값은 str 의 정보, 매개변수 x



### 상속

* 실습은 하지 않는 부분, 가볍게 보고 이해하면 될듯
* 파이썬에서 만드는 모든 클래스의 최상위 부모는 object
* `class 이름 (부모 클래스1, 부모 클래스2)` 
  * 부모가 만든 멤버들이 다 상속됨 (구현 생산성 증가)
  * 


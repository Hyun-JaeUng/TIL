# Django 프로그래밍 수업 요약

> 01/26

### 웹의 기본 이해

* 서버: 정보 제공하는 보통의 웹사이트들이 이에 해당
* 클라이언트: 서버를 찾아 접속하는 컴퓨터가 이에 해당

#### 웹 프로그램의 구조 별 개념

* 프론트엔드: 프론트엔드는 보통 사용자들이 보는 화면의 모습을 결정함. **HTML, CSS, JavaScipt** 프로그래밍으로 보통 구성되고, 클라이언트의 웹 브라우저에서 코드가 실행되거나 그려짐
* 백엔드: 백엔드는 사용자가 접속하면 그에 맞는 데이터를 보내주기 위해 여러가지 처리를 하는 부분을 담당하는 로직을 구성함. 우리가 배울 **Django 기반의 Python 프로그래밍이나 데이터베이스** 등이 여기에 속함
  * (CGI, PHP, ASP, Servlet, NodeJS, **JSP, Spring MVC**) - 많이 쓰이는 핵심 백엔드 언어인듯
  * 장고는 조금 더 후발주자.

#### 서버- 클라이언트 간 통신 방향 별 개념

* ""요청 - 응답"" 통신
  * 클라이언트 요청 -> 서버 응답
* 응답 방식: 약 80% HTML, 이 외에 JSON, XML도 있음. 

### HTTP 프로토콜

* 웹의 기본 통신규약 (정의한 규칙)
* HTTP 프로토콜은 상태가 없는 프로토콜 -> 이전 데이터 요청과 다음 데이터 요청이 서로 관련이 없다는 말

#### URL

* URL은 서버에 자원을 요청하기 위해 입력하는 영문 주소
* Protocol + Host + Port + resource path + Query
  * resource path가 생략되면 기본파일을 달라는 의미로 해석 - 주로 index.html)
* 예시: `https://www.domain.com:1234/path/to/resource?a=b&x=y`

#### HTTP 요청 메서드

* URL을 이용하면 서버에 특정 데이터 요청 할 수 있음
* 여기서 요청하는 데이터에 특정 동작을 수행하고 싶으면 HTTP 요청 메서드를 이용함

* **get, post**, put, delete 
  * get이 기본 요청 방식

#### HTTP 상태 코드

* 2XX - 성공, 3XX - 리다이렉션, 4XX - 클라이언트 에러, 5XX - 서버 에러
  * 200은 요청 성공
  * 404는 요청한 자원 못 찾아서 실패
  * 500은 자원은 있지만 실행 에러



## Django (장고)

> 웹 서버 프로그래밍 중 하나
>
> 적은 코딩량으로 우리가 원하는 것을 구현 할 수 있으나 난이도가 있는 편

* 장고는 파이썬으로 작성된 오픈 소스 웹 어플리케이션 프레임워크. (MTV 패턴)

* 장고 개발환경 구축 (가상환경, 워드 파일) 

#### 라이브러리(API)란?

* **재사용이 필요한 기능으로 반복적인 코드 작성을 없애기 위해 언제든지 필요한 곳에서 호출하여 사용할 수 있도록 Class나 Function으로 만들어진 것**
* 미리 준비하여 제공한 느낌

#### 프레임워크란?

* 원하는 기능 구현에만 집중하여 빠르게 개발 할 수 있도록 기본적으로 필요한 기능을 갖추고 있는 것으로 라이브러리가 포함되어 있음
* **BUT, 프레임워크만으로는 실행되지 않으며 기능 추가를 해야 되고, 프레임워크에 의존하여 개발해야 되며 프레임워크가 정의한 규칙을 준수해야 함**
* "반제품 형식"으로 나와서 꼭 양식에 맞춰서 나머지를 채우면 됨
* 최근에는 프레임워크 활용 많아짐 -> 빠르고 규격화 되어있음, 또한 유지보수하기가 좋다!
  * Django도 프레임워크 기반
  * studyproject에 전역적인 소스들이 있음

### 장고 프로그램의 개발 패턴

* 장고 프레임 워크에서는 기존 MVC 패턴에서 View를 Template, Controller는 View라고 표현하며, **MTV**라고 함
* 클라이언트 요청받아서 기능을 수행하는 역할 - **View** -> Python으로 개발 (중간관리자)
* 응답하는 역할 (프레젠테이션 역할) - Template -> HTML로 개발
* Model은 파이썬으로 필요하면 만들고, 안만들기도 함. (DB 동작, 자동화 많이 되어있음)
* 핵심은 클라이언트가 요청해서 서비스하는 로직과 응답하는 로직을 나눠서 개발함!
* 강의교안 1 리뷰보고, 복습 필요!

### 장고의 처리 흐름

* 웹 클라이언트의 요청을 받아 장고에서 MTV 모델에 따라 처리하는 과정
  1. 클라이언트로부터 요청 받으면 URLconf 모듈을 이용하여 URL 분석
  2. URL 분석 결과를 통해 해당 URL에 매칭되는 뷰들 실행
  3. 뷰는 자신의 로직을 실행하고, 데이터베이스 처리가 필요하면 모델을 통해 처리하고 그 결과 반환
  4. 뷰는 자신의 로직처리가 끝나면!, 템플릿을 사용하여 클라이언트에 전송할 HTML 파일을 생성
  5. 뷰는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답한다. 



### 이 외 코멘트

* templates 사용하는 앱 생성, 추가 시  studyproject - setting.py에서 INSTALLED_APPS에 넣어주어야 함
* main의 urls.py: `path('secondapp/', include('secondapp.urls'))` 설명
* templates 파일은 templates 폴더를 만들어서 거기에 넣는게 약속임
* urls 파일들 mapping 하는 방법
* first.app: 맛보기로 view만 있는 간단한 예제

* static 폴더 : 이미지와 같은 정적인 파일 넣어두는 폴더, 클라이언트한테 작업없이 던져지는 파일
  *  `STATIC_URL = '/static/'` : settings에 디폴트값으로 있음

> 0127 수업 시작!

#### 장고 강의교안 1 (가상환경부터 리뷰하면서 설명)

* `127.0.0.1` : 모든 컴터에서 자기 컴터 도메인 의미함
  * 즉, localhost 의미함
* 장고 프로그래밍에서 가상환경 만드는건 필수는 아님.
  * 테마(데이터 분석, 웹 서버)에 맞게 가상환경을 만들고, 이에 맞춰 추가 API 설치하는 것이 일반적 
* 경로 탐색에서 `cd \` 처럼 백슬래쉬부터 시작하면 최상위부터 경로 탐색을 시작한다는 의미

* 장고 프로젝트 생성: `cd 명령어 두번` -> `activate` -> DJANGOexam으로 디렉토리 이동

 -> `django-admin startproject '프로젝트 이름'`

* `settings.py` : 장고 프로그래밍에서 일어나는 환경설정하는 파일
* `urls.py`: urlpatterns에서 path 설정

#### secondapp 코드 설명

* HttpRequest: HTTP 프로토콜 기반으로 요청이 왔을 때 요청 관련 정보를 제공하는 객체, **요청 처리**
  
  * 뷰함수가 호출될 때 아규먼트로 전달된다. (장고 서버가 객체를 생성)
* HttpResponse: HTTP 프로토콜기반으로 온 요청에 대한 응답시 사용하는 객체, **응답 처리**
* 응답 내용을 담는다. (HTML 태그문자열, 템플릿을 사용한 랜더 객체)
* 템플릿 변수: {{ 변수명 }} => 값 표현

  * 변수는 뷰가 넘겨준 딕셔너리의 key 이름임
  * 꼭 딕셔너리로 전달해야 함
* 템플릿 태그(로직): {% 로직 %} => 로직 구현 

  * 화면에 영향은 없으나 post일때는 토큰이 있어야됨. -> 보안때문에 
* `<a>` 태그로 요청하는건 무조건 get 방식임
* get 방식: URL 직접 입력할 때, 하이퍼링크 요청할 때,  form태그의 method 속성 get일 때
* post 방식: form태그의 method 속성 post일 때
  * 상대적으로 엄격한 보안, 뒤에 / 안붙이면 에러남

#### HttpRequest와 HttpResponse

* 장고는 request와 response 객체로 서버와 클라이언트가 정보를 주고 받음

  * 이를 위해 django.http 모듈에서 HttpRequest와 HttpResponse API를 제공함

* 서버 - 클라이언트 통신 시 아래와 같은 절차로 데이터가 오고감

  1. 특정 페이지가 요청(request)되면, 장고는 요청 시 메타데이터(여러 다양한 정보)를 포함하는 HttpRequest 객체를 생성

  2. 장고는 urls.py에서 정의한 특정 View 함수에 첫 번째 인자로 해당 객체(request)를 전달
  3. 해당 View는 결과값을 HttpResponse 혹은 JsonResponse 객체에 담아 전달

* 뒤에 `/` 안붙이면 `/` 붙여서 통신이 한번 더 일어남
  
  * 불필요한 요청이 추가되는 것이라 URL 끝에 `/` 붙여서 요청해야함!

#### secondapp - exam2_1

* get 함수 설명 
* hidden 내용 설명
* get 방식은 쿼리 문자열이 주석빌드에 보임
* post 방식은 서버에게 전달되는 쿼리 문자열이 브라우저에 보이지 않음. 
  * 로그인, 회원가입시에는 이 방식이 좋음

오늘의 핵심: get 방식 처리와 post 방식의 처리하는 방법과 차이점 아는 것

#### Query 문자열

* HTTP 클라이언트가 HTTP 서버 요청시 서버에서 요청하려는 대상의 URI가 전달되는데, 이 때 함께 전달될 수 있는 문자열
* name=value 형식으로 구성
* 여러 개의 name=value가 사용될 때는 & 기호로 구분해야 함
* 영문과 숫자는 그대로 전달되지만 한글과 특수문자들은 %기호와 16진수 코드값으로 전달됨 (UTF-)
* 공백문자는 + 기호 또는 %20로 전달된다. 
* Query 문자열을 가지고 HTTP 서버에게 정보를 요청할 때는 두 가지 요청 방식중에서 한 개를 선택할 수 있다.
  * GET: Query 문자열이 외부에 보여짐. 요청 URL 뒤에 ? 기호와 함께 전달되기 때문
  * POST: Query 문자열이 외부에 보여지지않고, 길이에 제한이 없다. 

#### secondapp.exam 

* exam3:  `선택한 번호 : {{ number }}` -> number라는 키를 가진 딕셔너리 값인 5가 출력

* exam4: 리스트를 view에서 templates로 전달함
  * 템플릿 태그 이용한 예시 (html 파일 안에서 파이썬 처럼 코딩함)
  * for 태그와 endfor 태그, contents로 구성
* 템플릿 태그 설명 - 강의교안 (csrf_token)

* exam5 : Django의 if문과 else, endif 예제

  * 쿼리에 내용 주는 것 배움. 

* exam6: 쿼리문자열에서는 숫자도 문자로 인식해서 넘어옴!

  * context = None이 넘어오면 form태그 출력

  * exam6.html의 "`<input>` 태그는 name 속성의 값"과 "쿼리에서 추출하고자 하는 이름"과 똑같아야한다. 

    * ```html
      <input type="number" name="number" placeholder="숫자를 입력하세요" required>
      ```

    * ```python
      def exam6(request) :
          if request.method == 'POST':
              num = int(request.POST['number'])
              context = { 'num' : num*num }
          else :
               context = None
          return render(request, 'exam6.html', context)
      ```

      + name = "**Number**"와 request.Post['**number**'] 가 같아야한다.  

> 강의교안 내일 다시 한번 정리 + exam6을 통해 실습 아침에 해결 
>
> 01/27 수업 끝. 

* 장고실습2(0127_2) + 실습 리뷰
* studyproject에 templates 폴더 만들어서 basesimple.html을 만들어 이용하기
  * 이 파일의 형식을 가져와서 사용함으로써 다른 html을 편리하게 만들 수 있음
  * `{% extends 'basesimple.html' %}` : 가져오는 형식 
  * 이후 `{% block mycontent %}`와 `{% endblock %}` 사이에 원하는 내용 집어넣어 양식을 이용하는 것 
* exam7: basesimple.html extend 하여 사용하는 예제
* exam8: get방식은 직접 쿼리를 주소에 줄 수 있음.
  * ex)  `~~~/secondapp/exam8/?q=현재웅`
  * 유의할 점은 /?를 하고 쿼리를 줘야함! (`?` 뺴먹지 않기)
  * 또한 view에서 쿼리문자열 추출할 때 쓰인 '문자' 그대로 줘야함!
* exam9: getlist는 value 개수가 여러개 일때 쓰임
  * 딕셔너리 값에 다시 딕셔너리 줬다. 
  * 하나의 키 안에 담아서 전달해야해서 info 키를 주고 값을 딕셔너리로 줬다.
  * get 방식과 getlist 방식 구분
* exam10: name이라는 매개변수가 하나 추가되어 2개
  * 그 후 urls.py에 path 설정 시 URL뒤에 `<name>` 추가. 
* exam11: path에 `<int:age>` 추가, 매개변수 총 3개
  * int를 써서 숫자형으로 요청받기 
  * 안쓰면 무조건 문자열 취급
* exam12: 거의 11과 유사, 연산결과도 함께 전달
* 장고 실습3 (0128_1)
  * 너무 어렵다... 나중에 리뷰 잘 듣고 이해하기. 
* exam13: 여러가지 기능이 있는 걸 가볍게 알아가는 예제
  * for 태그 사용 3개
  * if 태그
  * forloop는 장고 템플릿 파일에서 쓰는 내장변수
  * `{% if food|length > 2 %}` : 필터링 하는 것
    * `food의 길이가 2보다 크면` 이라는 의미
    * food|length의 활용 (필터링)
  * lorem도 내장변수
  * 글자 관련 필터 사용예제
  * cycle 관련 내용
  * 모든 템플릿 태그들을 외울 필요는 없지만,  확인하는 느낌
  * for - empty 태그 : for문 도는 시퀀스의  요소가 아예 없을 때 수행하고 싶은 내용을 empty 밑에 적음
  * https://docs.djangoproject.com/en/3.1/ (장고 템플릿 태그 관련 설명하는 페이지)
* exam14: `http://localhost:8000/secondapp/exam14/올라프1/10/3.87` 
  * 매개변수가 여러 개 이므로 URL 뒤에 아규먼트 준 것. 
  * class 속성에 card나 btn 같은 이름을 부여했을 때 자동으로 여러가지 설정이 됨
  * why?
  * base.html에 **부트스트랩이 제공하는 기능**을 빌려다 쓴 코드가 있기 때문에 가능
    * ex) https://www.w3schools.com/bootstrap4/bootstrap_buttons.asp
    * 해당되는 클래스 속성을 따라 쓴 것.
  * `{% load static %}` 
    * `<img class="card-img-top" src="{% static 'images/olaf1.png' %}" alt="Card image" style="width:100%">`
    * 평소 쓰던 하드 코딩이 아닌 static 태그를 사용한 이미지 경로 설정 예시
    * 어떤 서버에 배포하든 유연성이 있기 때문에 static 태그가 좋다.

>  01/28 수업 끝. 

* exam15,16,17,18: urls에 설정한 name을 form 태그에 주어 페이지 이동하는 예시 

  ```html
  <form action="{% url 'unico' %}" method="GET">
    <input type="text" name="message">
    <input type="submit">
  ```

* exam19: 날짜와 시간 정보 출력하는 예제

  * ```python
    dt = datetime.now()
    ```

* exam20: AJOX 소개하는 샘플
  
  * 웹클라이언트 강의교안에 있음

#### XML

* 규격화 시킨 문서를 만들고 싶을 때 사용
* 태그명을 용도에 맞게 직접 정의하여 사용 가능하다.
* <시작태그>로 시작해서 </종료태그>로 종료.

#### JSON

* JSON(JavaScript Object Notation) 은 인터넷에서 자료를 주고 받을 때 그 자료를 표현하는 방법이다.
* 형식은 자바스크립트의 구문 형식을 따름

* JSON 객체는 파이썬에서는 딕셔너리

 #### AJAX

* Asynchronous JavaScript and XML (비동기적인 자바스크립트와 XML)
  * 고전적인 웹의 통신 방법은 웹페이지의 일부분을 갱신하기 위해서는 페이지 전체를 다시 로드해야했다.
  * AJAX의 핵심은 **재로드하지 않고 웹페이지의 일부만을 갱신**하여 웹서버와 데이터를 교환하는 방식
  * 즉, 빠르게 동적 웹페이지를 생성하는 기술이다.

* 장점은 현재 페이지를 그대로 고정시킨 상태에서 서버의 응답을 받고 처리할 수 있다.
  * 전체 페이지를 다시 끌어오는 것이 아니라 필요한 만큼만 가져온다.
* jQuery의 AJAX 지원 API
  * 그 중 `$.ajax()` 와 `$.getJSON()` 을 이용하여 수업에서 다룰 예정

#### AJAX 프로그래밍 핵심 내용

(1)  JSON(XML) 형식으로 응답하는 뷰를 준비해야 한다.

* 템플릿을 거치지 않고, 뷰가 직접응답함

(2) - 1.  JavaScript만 사용해서 AJAX 요청을 구현하는 방법

* `var xhr = new XMLHttpRequest()`
* `xhr onload = 함수`
* `xhr open("GET", "대상URL", true)`
* `xhr.send()`

(2) - 2. jQuery API를 사용하여 AJAX 요청을 구현하는 방법

* `$.getJSON("대상URL", 함수)`
  * 이게 위보다 훨씬 간편함

#### view.py의 json1/2/3

* 3개 모두 템플릿 없이 뷰에서 직접 처리하는 예제

**JsonResponse**

* 첫번째 아규먼트는 딕셔너리 이어야 함
* 딕셔너리가 아닌 다른 자료형을 받을 경우, 두번째 아규먼트를 `safe =False`로 설정해야한다.
* `json_dumps_params` 는 `json.dumps()`에 전달할 딕셔너리의 keyword arguments임
* json1: JsonResponse 일반적인 예시, 두번째 아규먼트로 keyword arguments임
* json2: 첫번째 아규먼트로 리스트를 주었고, 두번째에 `safe =False`  주었음
* json3: `json_dumps_params={'ensure_ascii':False}`  의미 질문.

 #### second.app exam

* exam20: `$('p').click(function(e) ~~~ `  : e는 사건이 일어나는 이벤트 객체를 매개변수로 선언한 것
  * getJSON 이용하여 자바스크립트 객체로 data 변수에 가져옴
* exam21~24: 영화관 오픈 API를 AJAX 기술로 활용한 예시
* exam21: `$.ajax` 사용하여 json 객체로 가져옴
  * jsonviewer 사용하여 편하게 보는 방법도 소개함 (구글 검색하면 나옴)
  * 주석으로 막아놓은 코드는 `$.getJSON`으로 한 예제

* exam23: `targetDt` 를 이용하여 하드코딩이 아닌 소프트코딩한 예시
  * 날짜를 계속해서 변화하게 해줌. (URL 뒤에 targetDt 넣음)
* exam24: 영화 썸네일 포함시킴 (이미지)

#### Same Origin Policy (SOP)

* 브라우저에서 보안상의 이슈로 동일 사이트의 자원만 접근해야 한다는 제약 (서버 컨텐츠 보호를 위해)
* AJAX는 이 제약에 영향을 받으므로 Origin 서버가 아니면 AJAX로 요청한 컨텐츠를 수신할 수 없다.

#### Cross Origin Resource Sharing (CORS)

* Origin이 아닌 다른 사이트의 자원을 접근하여 사용한다는 의미
* Open API의 활성화와 공공 DB의 활용에 의해서 CORS의 중요성이 강조되고 있음
* HTTP Header에 CORS와 관련된 항목을 추가한다.
  * `response.addHeader("Access-Control-Allow-Origin","*");` 을 추가해야됨
  * exam 예제의 경우, CORS 추가하였기 때문에 사용가능하였음

#### 서울시 빅데이터 URL

http://openapi.seoul.go.kr:8088/796143536a756e69313134667752417a/json/LampScpgmtb/1/100/

#### product 1/2 review

* 실습 코드 보며 리뷰 - 파일에 정리

#### ggmap exam

* google.maps 사용하려면 스크립트 태그에 구글맵 URL과 키가 필요함
* `encodeURIcomponent()` 를 통해 쿼리문자열에 사용할 수 있도록 한글 맞춰서 인코딩해줌.

#### kkmap exam

* https://apis.map.kakao.com/
  * API 샘플과 코드들 정리 잘 되어있음.

> 01/29 수업 끝
## jQuery

* jQuery() => $()

* `$(documnet).xxxx()` 

* `$(CSS선택자).xxxx()`

* `$(함수)`: 로드 이벤트 발생시 호출될 함수 등록 
  * `== $(document).ready(함수)`

* `$.xxxx()` : jQuery 객체가 제공하는 클래스 메서드
* `$(CSS선택자, context).xxxx()`: context에 DOM 객체를 주면 그 해당 객체의 자손에서만 찾음

> domaccess exam 다. 

* exam 6 : 클래스는 여러 개 적용 가능 (공백으로 구분)
* exam 7 : 자손들 선택자로 설정하여 스타일 부여
* exam 8: `.val`  메서드 사용
  * 아규먼트 없을 때는 getter, 값을 읽는 용도 
  * 아규먼트 있을 때는 setter, 값을 설정하는 용도
  * 첫번째 아규먼트는 인덱스, 두번째는 값임

### jQuery의 API

* jQuery는 API 사용 방법이 일관성 있어서 API를 익히기 쉽다.  (API 5개 매우 중요)

1. `html()`: innerHTML과 유사
2. `text()`: textContent 과 유사
3. `val()` : value와 유사 

* 위에 3개는 아규먼트 없을떄에는 getter (값을 얻는다)
* html(함수), text(함수), val(함수), html("....")와 같이 아규먼트가 있을 때는 setter (값을 설정한다.)
* API들이 해당되는 태그가 여러개라면 반복문처럼 기능하면서 인덱스와 함께 실행됨!

4. `css()`

5. `attr()`

* `css("CSS속성명"), attr("HTML태그속성명")` : getter 
* `css("CSS속성명", "CSS속성값"), attr("HTML태그속성명","HTML태그속성값")` : setter
* `css("CSS속성명", 함수), attr("HTML태그속성명", 함수)`: setter 

* `css(자바스크립트객체), attr(자바스크립트객체)`: setter 



#### domedit exam

* exam1: `$('h1').addClass('item')` : h1 태그인 애들 모두 item 클래스 속성을 추가하는 역할

* exam2: 해당되는 태그가 여러개 일 때 index를 활용하여 다르게 적용한 예시 
* exam3: `$('h1').removeClass('item')`
* exam4: `$('img').attr('width', 200)` : image 태그인 객체들 너비 조정
* exam5: 해당되는 태그가 여러개 일 때 index를 활용하여 다르게 적용한 예시

* exam6: attr 메서드 안에 객체를 준 예시
* exam7: removeAttr 메서드, 존재하고 있는 속성 제거
* exam8: css 메서드는 **getter 시**에는 첫번째 해당되는 것에만 수행함
  * css, html,val는 모두 첫번째 것만 해당되고, text만 특이하게 모두 수행
  * each를 활용하여 모두에게 적용하는 해결방안 예시
* exam9: 
* exam10: 
* exam11: getter로 동작할 때 html 메서드는 한 개만 가져오는 예시 
  * each를 활용한 예시도 함께 있음
* exam12: 반면 text 메서드는 모두 가져오는 예시

* exam13: html 메서드와 text 메서드의 차이 => html 태그로 적용받기위해서는 html 메서드 사용해야 함
* exam14: 
* exam15: 첫번째 아규먼트는 무조건 인덱스 (사용하지 않더라도 받을 변수가 필요)임을 알려주는 예시
  * ready - click 이벤트를 text 메서드를 활용하여 설정
* exam16: `$('h1').first().remove();` , h1 태그의 첫번째를 제거 
* exam17:
* exam18: jQuery를 이용하여 새로운 태그를 만드는 예시

* exam19: `$('HTML태그문자열')` 예시, 새로운 태그 만들고 속성 부여
* exam20: 한 번에 동일한 내용 태그를 여러개 만드는 것. (?)

### jQuery의 이벤트 핸들러 구현

1. `$('...').on('이벤트이름', 함수)`, `$('...').on(자바스크립트객체)`
2. `$('...').이벤트이름(함수)`
3. `$('...').off()`: 이벤트 핸들러를 해제

#### event exam

* exam1: 위에 2가지 이벤트 핸들러 구현을 이용한 예시
* exam2: 1의 예제를 hover를 이용하여 구현한 예시
* exam3: 
* exam4: `<meta charset="UTF-8">` , 한글 작성시 meta 태그 있어야 함.
* exam5: `$('h1', this).text()` 를 통해 **클릭 이벤트가 발생한 div 태그의 자손에서만 찾음** 

* exam6: 조금 어려운 내용(가볍게), canvas API 사용.
* exam7: textarea에서의 이벤트 처리
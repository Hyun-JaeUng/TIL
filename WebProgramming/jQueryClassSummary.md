# jQuery

* HTML 문서 안의 스크립트 코드를 단순화하도록 설계된 자바스크립트 라이브러리

### jQuery 라이브러리 사용

* jQuery() => $()
* `$(documnet).xxxx()` 
* `$(CSS선택자).xxxx()`
* `$(함수)`: 로드 이벤트 발생시 호출될 함수 등록 
  * `== $(document).ready(함수)`
* `$.xxxx()` : jQuery 객체가 제공하는 클래스 메서드
* `$(CSS선택자, context).xxxx()`: context에 DOM 객체를 주면 그 해당 객체의 자손에서만 찾음

### DomAccess exam 

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



#### DomEdit exam

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
* exam9: css 메서드 setter 시에는 모두에게 적용되는 예시 
* exam10: css메서드 setter 사용, 아규먼트로 객체와 함수 주는 예시
* exam11: getter로 동작할 때 html 메서드는 한 개만 가져오는 예시 
  * each를 활용한 예시도 함께 있음
* exam12: 반면 text 메서드는 모두 가져오는 예시

* exam13: html 메서드와 text 메서드의 차이 => html 태그로 적용받기위해서는 html 메서드 사용해야 함
* exam14: html 메서드 setter로 사용한 예시, 태그 적용과 index 활용
* exam15: 첫번째 아규먼트는 무조건 인덱스 (사용하지 않더라도 받을 변수가 필요)임을 알려주는 예시
  * ready - click 이벤트를 text 메서드를 활용하여 설정
* exam16: `$('h1').first().remove();` , h1 태그의 첫번째를 제거 
* exam17: `$('div').empty();`, div 태그 내부 삭제하는 empty
* exam18: jQuery를 이용하여 새로운 태그를 만드는 예시

* exam19: `$('HTML태그문자열')` 예시, 새로운 태그 만들고 속성 부여
* exam20: append를 사용하여 한 번에 동일한 내용의 태그를 여러개 만드는 예시

### jQuery의 이벤트 핸들러 구현

1. `$('...').on('이벤트이름', 함수)`, `$('...').on(자바스크립트객체)`
2. `$('...').이벤트이름(함수)`
3. `$('...').off()`: 이벤트 핸들러를 해제

#### Event exam

* exam1: 위에 2가지 이벤트 핸들러 구현을 이용한 예시
* exam2: 1의 예제를 hover를 이용하여 구현한 예시
* exam3: this를 활용하여 이벤트 구현
* exam4: `<meta charset="UTF-8">` , 한글 작성시 meta 태그 있어야 함.
* exam5: `$('h1', this).text()` 를 통해 **클릭 이벤트가 발생한 div 태그의 자손에서만 찾음** 

* exam6: 조금 어려운 내용(가볍게), canvas API 사용.
* exam7: textarea에서의 이벤트 처리

* exam8: 아이디, 비밀번호 로그인 예제, `event.preventDefault()` 사용, `<input type ~~>`

#### Map exam

* geolocation: 현재 사용자의 위도, 경도 알아내는 예제
  * `navigator.geolocation.getCurrentPosition(showPosition,showError)`
  * 위치 정보를 잘 찾았을 때 실행되는 함수 showPosion
  * 에러났을 때 실행되는 함수 showError, 2개가 아규먼트임
* geocoding: 주소와 좌표 변환하는 프로그램 예제
  * 구글에서 받아온 키가 필요함
  *  json 형식으로 받아와서 코딩하였음
* ggmap1: 지도를 그리는 예제
  * 키를 이용하였음, 구글의 지도 API를 끌어오는 키가 필요함 
  * `new google.maps.Map(~~)` 사용
* ggmap2: 지도에 더하여 중심에 marker 그리는 예제
  * `new google.maps.Marker({position: latlng, map: map})` 사용
* ggmap3: marker에 이벤트 더하는 예제 (infoWindow를 설정함)
  * 마커 클릭시 이미지와 설명 더할 수 있음
  * `new google.maps.InfoWindow()` 사용
* ggmap4: 지금 나의 위치를 기준으로 지도를 그리는 예제
* ggmap5: 주소를 입력받아 지도를 출력하는 예제
  * 마커를 사용자가 지정한 이미지로 출력




## 카카오 API를 활용한 전기자동차 지도 만들기

<br>

출처:  [카카오 API로 코로나맵 만들기](https://www.youtube.com/watch?v=1JgpDcHEkFg)

<br>

1. 키 발급

* JavaScript 키
  
  * 57627380982567023fbc6b96f99ced70
  
  <br>

2. Wizard를 활용하여 설정하기

   * index 안에 코드 복사 후 넣기 -> 발급받은 키도 삽입.
   * 여기까지 하면 단순히 지도만 표시

   <br>

3. width, height 수정 (ex: 100%)

   <br>

4. `position: new kakao.maps.LatLng(37.56765, 126.97889), // 마커의 좌표`

   <br>

5. 마커에 인포 윈도우 표시하기 (sample에 해당 설명란 있음)

   * `var iwContent =`  옆에 `<div style="padding:5px">내용</div>` 사용하여 인포 윈도우 내용 수정
   * iwposition이 중복되는 경우는 중복되는 부분 제거

   <br>

6. 두번째 마커 생성

   * 좌표 정보 찾은 후 마커와 인포윈도우 관련 코드들 복사
   * 이 후 변수명 다르게 수정 (ex2 와 같이)
     * **But 이런 식의 복붙 코드는 다 수의 마커 추가 시 매우 번거로움**

   <br>

7. var 데이터 후 여러 개의 좌표 정보 `데이터 변수`에 담고, for문 수행

   * for문 내부에 마커 생성, 표시 코드 넣기

   <br>

8. 남은 문제: 지도 축소 시 마커 겹치는 문제 발생

   * "마커 클러스터러 사용하기" -> 데이터 다운받아서 사용, jQuery 라이브러리 추가해야 함
   * `// 마커 클러스터러를 생성합니다` 단락 var map 바로 아래에 붙여넣기 
   * var markers = []; 생성하여 마커들을 담을 변수 생성
     * `markers.push(marker);`: markers 라는 변수 안에 marker 라는 마커를 집어넣음
     * 모든 마커들이 들어간 markers를 `clusterer.addMarkers(markers); ` 코드를 통해 클러스터러에 마커를 추가함

   <br>

9. 남은 문제: 텍스트 겹치는 문제 (인포 윈도우 겹침)

   * 마우스가 올라갈 때만 인포윈도우 나오도록 설정해보자!
   * sample `여러 개 마커에 이벤트 등록하기 1` 참조
     *  동영상 보고 코드 위치 참고 -> 문제 해결

```javascript
    // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
    // 이벤트 리스너로는 클로저를 만들어 등록합니다 
    // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
    kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
    kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
}

// 인포윈도우를 표시하는 클로저를 만드는 함수입니다 
function makeOverListener(map, marker, infowindow) {
    return function() {
        infowindow.open(map, marker);
    };
}

// 인포윈도우를 닫는 클로저를 만드는 함수입니다 
function makeOutListener(infowindow) {
    return function() {
        infowindow.close();
    };
}
```

<br>

10. 웹 페이지에 표시하려면 카카오 - 내 어플리케이션 - 일반 - 플랫폼 추가 해야함!


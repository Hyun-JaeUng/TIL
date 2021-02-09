## SQLite를 이용하여 전기차 DB 구축하기

데이터 엑셀 - 1. 급속 - 완속 , 2. **급속 충전 타입**

충전소 웹사이트 중요 정보 - 1. 구분 (급속 or 완속) 2. 충전기 타입 3. 운전 상태

* 기존의 한전 전기차 모델 나타낸 페이지 잘못된 점 
  * [한전 전기차 현황 사이트](https://evc.kepco.co.kr/service/service03.do)
  * [관련 기사](https://www.evpost.co.kr/wp/%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EC%82%B4%ED%8E%B4%EB%B3%B8-%EC%A0%84%EA%B8%B0%EC%B0%A8-%EB%B3%B4%EA%B8%89-%ED%98%84%ED%99%A9%EA%B3%BC-%EC%A2%85%EB%A5%98/)
    * 위의 사이트 잘못된 점 언급
    * ex) 급속 충전시간, 완속 충전시간 오차 (조사한 기준도 언급X) , 코나 EV의 최고 속도



[전기차 보조금의 높은 영향력 기사](https://www.hankyung.com/car/article/202102032042g)

[2020 상반기 전기자동차 판매 순위](https://www.yeongnam.com/web/view.php?key=20200815010002006)

* 판매 순위

1. 테슬라 모델3
2. 현대차 코나 EV

3. 현대 포터2 일렉트릭
4. 기아 니로 EV
5. 기아 봉고3 EV 

추가적으로 `2021년 전기자동차 보조금 지원대상 현황` 을 기준으로 DB에 들어갈 모델을 결정하였음.

* 기본형 - 경제형 차이: 저용량 배터리 사용하면 경제형 -> 1회 충전 주행거리가 다름
* HP, PTC 차이: 히트펌프가 있으면 HP, 히트 펌프가 없으면 PTC
  * [블로그 글](https://blog.naver.com/PostView.nhn?blogId=dy_kweon&logNo=222057937062&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)

* 2021년 전기차 보조금 정리 영상
  * [유튜브](https://www.youtube.com/watch?v=pyJoMhxl1CM)
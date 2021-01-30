# Django 실습

> 장고 실습파일을 직접 구현하면서 요약하고, 유의할 점을 메모하는 파일

### exercise1

* 

### exercise2

Q) GET 방식 요청시에는 입력 폼 화면이 출력되고, POST 방식 요청시에는 Query 문자열로 전달되는 작성자명과 의견 정보를 추출하여 새로운 브라우저에 출력한다.

##### # views.py

```python
def exercise2(request):
    if request.method == 'POST':
        text1 = request.POST['text11']
        text2 = request.POST['text22']
        context ={'text1':text1, 'text2':text2} #key는 문자열 처리 해야 함! 
    else:
        context = None
    return render(request,'exercise2.html', context)
```

* 요청방법이 POST 방식인지 확인 후,  사용자로부터 input한 정보들을 가져오고, 그것을 또 전달해주기 위해 context 딕셔너리를 만들었다.
* 딕셔너리의 key 명칭은 html에서 사용 시에 그대로 쓰임. 
  * ex) {{text1}}, {text2}
* 반면 POST 방식으로 요청된 값을 가져올 때는 input시 입력한 `name = "~~"` 과 일치하는 명칭을 써야 한다. 
* render 함수를 이용해 request - 템플릿 파일 이름 - 전달할 context 순으로 아규먼트를 주어 return 하였다.   

##### # templates - exercise2.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Django 실습2</title>
</head>
<body>
<p>
    {% if text1 and text2 %}
        <h1><span style="color:green">{{text1}}</span>님이 남긴 글입니다.</h1>
        <hr>
        <h2>{{text2}}</h2>
    {% else %}
        <h1>의견을 남겨 주세요.</h1>
        <hr>
        <form method='POST' action="/workapp/exercise2/">
            {% csrf_token %}
            <input type="text" name="text11" placeholder="작성자 이름을 입력해주세요", required>
            <br>
            <br>
            <textarea name="text22" cols="40" rows="8" placeholder="자신의 의견을 간단히 적어주세요", required></textarea>
            <br>
            <br>
            <input type="submit" value="제출">
            <input type="reset" value="재작성">
        </form>
    {% endif %}
</p>
</body>
</html>
```

* `<form>` 태그
* 추가할 내용 완성시키기. 
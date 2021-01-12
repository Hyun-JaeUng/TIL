oddeven= { d : '홀수'   if d % 2  else  '짝수' for d in range(1, 16)  }
print(oddeven)
# 키는 중복안되지만 value는 중복되는 딕셔너리 괜찮음

scores = {'길동': 90, '순희': 60, '영희': 80, '철수': 50}
grades = { name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
print(grades)

member = { 'name'+str(i) : i*10 if i > 5 else  i + 100 for i in range(1,11) }
print(member)

fruits = ['apple', 'mango', 'banana','cherry']
dic_fruits = {f:len(f) for f in fruits}

print(dic_fruits)

print( {v : k for k, v in member.items()})

print( {v : k for k, v in dic_fruits.items()})
# 중복되는 키를 가진 것들 생성안됨

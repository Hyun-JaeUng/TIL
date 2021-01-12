a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a & b)

# 앞에 포문이 바깥 for문 , 중첩된 for문
listv = [dan * num for dan in range(1, 10) for num in range(1, 10)]
setv =  { dan * num for dan in range(1, 10) for num in range(1, 10)}

print(listv)
print(setv) # 셋은 순서가 의미없고 중복만 제거
data = [1,2,3,4]

print(data)
print(*data) # 아규먼트에서도 *을 붙일 수 있음, 리스트가 가지고있는 요소값들을 쪼개서 야구먼트로 전달함!!
print(data[0], data[1], data[2], data[3])

print("*"*30)
a,b,c,d = [10,20,30,40]
print(a)
print(b)
print(c)
print(d)

print("*"*30)
x,*y,z = [10,20,30,40]
print(x)
print(y) # 처음, 마지막 뺴고 모두 y한테 할당
print(z)

print("*"*30)
p = 100, 200, 300
print(p)

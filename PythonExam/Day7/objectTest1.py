a = 100
print(type(a)) #int
print(a.bit_length())
print(bin(a))
# a. 했을 떄 뜨는 것들은 코드 어시스턴트, 객체에 속한 메서드 알려주는 것

b = 3.14
print(type(b)) #float
print(b.real)
print(b.is_integer())

c = 3+4j
print(type(c)) #complex
print(c.real)
print(c.imag)

d = False
print(type(d)) # bool
print(d.bit_length())
print(bin(d))

e = " "
print(type(e)) # str
print(e.isspace())
print(e.join("ㅋㅋㅋ"))

f = []
print(type(f)) # list
print(f.extend([1,2,3]))
print(f.reverse()) # 리스트의 변화를 주는 메서드들인데 자체 리턴값은 None임
print(f)

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))


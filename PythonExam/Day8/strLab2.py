# 1번
s1 = "pythonjavascript"
print(len(s1))
# 2번
s2 = "010-7777-9999"
s2 = s2.split("-")
print(s2[0], s2[1], s2[2], sep ="") # join 활용해도 됨
# 3번
s3 ="PYTHON"
print(s3[::-1])
# 4번
print(s3.lower())
# 5번
s5 = "https://www.python.org/"
print(s5[s5.index("/")+2:s5.rfind("/")])
# 6번
s6 = "891022-2473837"
sd = s6.index("-")
if int(s6[sd+1]) == 1 or int(s6[sd+1]) == 3:
    print("남성")
elif int(s6[sd+1]) == 2 or int(s6[sd+1]) == 4:
    print("여성")
# 7번
s7 = "100"
print(int(s7))
print(float(s7))
# 8번
s8 = 'The Zen of Python'
print(s8.count("n"))
# 9번
print(s8.find("Z"))
# 10번
news8 = s8.upper()
print(news8.split())
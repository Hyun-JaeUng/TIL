
name = "재웅"
age = 26
height = 180.99

print("이름:{}, 나이:{}, 키:{}".format(name,age,height))
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name,age,height))
print("이름:{0:10s}, 나이:{1:5d}, 키:{2:8.2f}".format(name,age,height))
print("이름:{0:^10s}, 나이:{1:>5d}, 키:{2:<8.2f}".format(name,age,height))
print("이름:{0:$^10s}, 나이:{1:>05d}, 키:{2:!<8.2f}".format(name,age,height))

# f-string
print(f"이름:{name}, 나이:{age}, 키:{height}")
print(f"이름:{name:s}, 나이:{age:d}, 키:{height:f}")
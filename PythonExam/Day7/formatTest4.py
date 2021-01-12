# 파이썬 3.6부터 사용 가능
# ===== newnewformat  =====
name = "한결"
age = 16
height = 162.5
print(f"이름:{name}, 나이:{age}, 키:{height}")

# ===== newnewformat2  =====
name = "한결"
age = 16
height = 162.5
print(f"이름:{name:s}, 나이:{age:d}, 키:{height:f}")

# ===== newnewformat3  =====
name = "한결"
age = 16
height = 162.5
print(f"이름:{name:10s}, 나이:{age:5d}, 키:{height:8.2f}")
# 문자는 기본 왼쪽, 숫자는 오른쪽 기본값인듯.

# ===== newnewformat4  =====
name = "한결"
age = 16
height = 162.5
print(f"이름:{name:^10s}, 나이:{age:>5d}, 키:{height:<8.2f}")
# 가운데 정렬, 오른쪽 정렬, 왼쪽 정렬

# ===== newnewformat5  =====
name = "한결"
age = 16
height = 162.5
print(f"이름:{name:$^10s}, 나이:{age:>05d}, 키:{height:!<8.2f}")
# 나머지 문자로 채움

#===== 1000단위 , 사용 =====
num = 1000000
print(f'{num:,}')


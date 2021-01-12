# =====width  =====
value = 123
print("###%d###" % value)
print("###%5d###" % value)
print("###%10d###" % value)
print("###%1d###" % value)

# =====align  ===== 정렬 : align
price = [30, 13500, 2000]
for p in price:
    print("가격:%d원" % p)
for p in price:
    print("가격:%7d원" % p)
print("%d - %d - %d" % tuple(price)) #여러 개 일시 튜플로 해야해서 리스트를 튜플로 함

# =====numalign  =====
price = [30, 13500, 2000]
for p in price:
    print("가격:%-7d원" % p) # 7칸인데 왼쪽에 붙는게 -7
    print("가격:%7d원" % p) # 7칸인데 오른쪽에 붙는게 +7

# =====precision  =====
pie = 3.14159265
print("%10f" % pie)
print("%10.8f" % pie)
print("%10.5f" % pie)
print("%10.2f" % pie)

#===== 1000단위 , 사용 =====
num = 1000000
print('%s' % format(num, ','))


sum = 0

for i in range(1,51):
    if i%3 ==0:
        if i%5 ==0:
            continue
        sum += i

print("결과 = ", sum)

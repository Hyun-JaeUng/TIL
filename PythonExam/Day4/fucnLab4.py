def print_triangle(n):
    if 1<= n <= 10:
        for i in range(1,n+1):
            print("*" * i)
    else:
        pass
    # else 절은 생략 가능함!

print_triangle(5)
print_triangle(7)
print_triangle(3)
print_triangle(12)
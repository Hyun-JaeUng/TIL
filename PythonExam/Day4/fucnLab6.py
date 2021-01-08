def print_gugudan(n):
    if type(n) == int:
        if 1<=n<=9:
            for i in range(1,10):
                print(n,"*",i,"=",n*i)
        else:
            pass
    else:
        pass

print_gugudan(3)
print_gugudan(5)
print_gugudan(8)
print_gugudan(10)
print_gugudan("x")

# else - pass 없어도 됨. 가독성 필요할 떄만 쓰기

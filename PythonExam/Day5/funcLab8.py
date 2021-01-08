def print_triangle_withdeco(n,s="%"):
    if 1<=n<=10:
        for i in range(1,n+1):
            print(" " * (n-i) + s * i)
    else:
        pass

print_triangle_withdeco(2)
print_triangle_withdeco(5,"*")
print_triangle_withdeco(8,"$")
print_triangle_withdeco(11,"r")

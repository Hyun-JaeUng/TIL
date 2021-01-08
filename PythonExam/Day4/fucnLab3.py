def expr(num1,num2,x):
    ans = 0
    if x == "+":
        ans = num1 + num2
    elif x == "-":
        ans = num1 - num2
    elif x == '*':
        ans = num1 * num2
    elif x == '/':
        ans = num1 / num2
    else:
        ans = None
    if ans != None:
        print("연산 결과 :", ans)
        return ans
    else:
        print("수행 불가")
        return None

expr(3,5,"+")
expr(3,5,5)
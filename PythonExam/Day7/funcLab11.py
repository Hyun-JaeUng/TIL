def mydict(**n):
    d={}
    for k,v in n.items():
        d['my'+k] = v
    return d
print(mydict())
print(mydict(name = "Hyun", age = 26))


# 딕셔너리를 포문에 그냥 넣으면 key값이 포문 돈다.
# 위처럼 해야 키 - 값으로 나누어져 돈다.
# if 변수: 하면 변수가 비어있으면 false라 돌지 않음
# 즉 len(변수)!=0 말고, if 변수 해도됨



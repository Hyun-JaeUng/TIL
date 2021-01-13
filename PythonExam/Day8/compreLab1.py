def createList (type = 1, *lt):
    ans = []
    if len(lt) == 0:
        if type == 1:
            ans = [i for i in range(1,31)]
        elif type == 2:
            ans = [i for i in range(1, 31) if not i%2 ]
        elif type == 3:
            ans = [i for i in range(1, 31) if i%2 ]
        elif type == 4:
            ans = [i for i in range(1, 31) if i>10]
    else:
        if type == 1:
            ans = [i for i in lt]
        elif type == 2:
            ans = [i for i in lt if not i%2 ]
        elif type == 3:
            ans = [i for i in lt if i%2 ]
        elif type == 4:
            ans = [i for i in lt if i>10]
    return ans

print(createList(1,5,2,1))
print(createList())


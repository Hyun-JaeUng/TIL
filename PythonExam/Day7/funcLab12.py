def myprint (*a, **args):
   deco = '**'
    s = ','
    if 'deco' in args.keys():
        deco = args['deco']
    if 'sep' in args.keys():
        s = args['sep']
    '''deco = args.get("deco", "**")
    s = args.get("sep", ",")'''

    result = ''
    if len(a) == 0:
        print("Hello Python")
    else:
        result += deco
        for i in range(len(a)):
            result += str(a[i])
            if i < (len(a)-1):
                result += s
        result += deco
        print(result)

myprint(10,20,30, deco = "@", sep ="-")
myprint("python", "javascript", "R", deco = "$")
myprint("가", "나", "다")
myprint(100)
myprint()

import random
anslist = [ random.randint(0,100) for i in range(10)]
print(anslist)
ansdic = { i+1 : "pass" if anslist[i] >= 60 else "nopass" for i in range(10)}
print(ansdic)

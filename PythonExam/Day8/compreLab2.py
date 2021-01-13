def mycompredict (**n):
    d = {'my'+ k : v for k, v in n.items()}
    return d

print(mycompredict())
print(mycompredict(name="Hyun", age=26))


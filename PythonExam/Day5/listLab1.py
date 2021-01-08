listnum = [10,5,7,21,4,8,18]
max_num = 0

for i in range(len(listnum)):
    if i == 0:
        max_num = listnum[0]
    else:
        if max_num >= listnum[i]:
            pass
        else:
            max_num = listnum[i]

print("최댓값 :", max_num)



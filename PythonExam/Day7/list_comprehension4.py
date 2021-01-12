list1 = [ chr(d)  for d in range(ord('A'), ord('Z')+1) ]
print(list1)
# ord('A') = 65 나옴, 알파벳에 따른 십진수 리턴

list2 = [ d  for d in range(1, 16) ]
print(list2)

list3 = [ d  for d in range(1, 16) if not d % 2 ] # 반대로하는 not 활용
print(list3)

list4 = [ d  for d in range(1, 16) if not d % 3 ]
print(list4)

list5 = [ d   if d % 2  else  '짝수' for d in range(1, 16)  ]
print(list5)
# else에 해당하는 애들은 "짝수"가 대신 들어감

list6 = [ '홀수'   if d % 2  else  '짝수' for d in range(1, 16)  ]
print(list6)

list7 = [ 'pass_'+str(d)   if d % 2  else   'fail_'+str(d) for d in range(1, 16)  ]
print(list7)

oldlist = [1, 2, 'A', False, 3]
newlist = [i * i for i in oldlist if type(i) == int]

print(newlist)




oldlist = [17,2,14,6,10,19,16,12,5]
newlist1 = [ oldlist ]
print(newlist1) # 요소가 1개인 이중 리스트 (1행, 10열)

newlist2 = list( [1,2,3,4,5,6,7,8] )
print(newlist2) # 이중리스트 아니고 일반 리스트

newlist3 = list( (1,2,3,4,5,6,7,8) )
print(newlist3) # 일반리스트

newlist4 = list( {1,2,3,4,5,6,7,8} )
print(newlist4)

newlist5 = list( "ABC")
print(newlist5) # -> ['A','B','C']

newlist6 = [ x for x in range(1, 9) ]
print(newlist6)

newlist7 = [ x for x in oldlist if x % 2 ] # 2로 나눈 나머지가 0이면 조건식 false, True일 때만 조건성립
print(newlist7)

newlist8 = [ x for x in oldlist if x > 10 ]
print(newlist8)

newlist9 = [ x*10 for x in oldlist if x < 10 ]
print(newlist9)

flowernames = ['rose', 'sunflower', 'tulip', 'magnolia', 'goldenbell', 'lily']
newlist10 = [i for i in flowernames if len(i) == 4]
print(newlist10)

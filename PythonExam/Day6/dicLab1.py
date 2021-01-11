dic = {'red':'#ff0000', 'blue':'#0000ff', 'yellow':'#ffff00', 'orange':'#ffa500',
'black':'#000000', 'white':'#ffffff', 'violet':'#ee82ee', 'pink':'#ffc0cb','lime':'#00ff00'}

rep = input("칼라명을 영문으로 입력하세요. : ")

if rep in dic:
    print(rep, "칼라의 RGB 값은", dic[rep], "입니다.")
else:
    print(rep, "칼라의 RGB 값을 찾을 수 없습니다.")


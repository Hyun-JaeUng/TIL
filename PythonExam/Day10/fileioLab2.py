try:
    f = open("sample.txt", "rt", encoding= "UTF-8")
    new = open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")
    rows = f.readlines()
    for row in rows:
        new.write(row)
    new.write("\n\n") # 다음번 내용 추가 때 겹치지 않게 개행처리함
    print("저장이 완료되었습니다.")
    f.close()
    new.close()

except FileNotFoundError:
    print("파일이 없습니다. 다시 확인해주세요.")

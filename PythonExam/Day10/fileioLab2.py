# 예외처리 try - except
try:
    # 파일 오른, 읽기 (read) 모드
    f = open("sample.txt", "rt", encoding= "UTF-8")

    # 현재 경로에 새로운 txt 파일 생성 및 열기 (append 모드)
    new = open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")

    # f 파일을 한 행씩 추가하는 코드 + 개행처리
    rows = f.readlines()

    for row in rows:
        new.write(row)

    new.write("\n\n")
    print("저장이 완료되었습니다.")

    # 파일닫기
    f.close()
    new.close()

except FileNotFoundError:
    print("파일이 없습니다. 다시 확인해주세요.")





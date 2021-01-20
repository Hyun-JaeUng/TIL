import time

now = time.localtime()
try:
    fr = open("sample.txt", "rt", encoding="UTF-8")

    file_name = f"sample_{now.tm_year}_{now.tm_mon:02d}_{now.tm_mday:02d}.txt"
    fw = open(file_name, "at", encoding="UTF-8")

    for line in fr:  # _io.TextIOWrapper 객체도 리터러블함
        fw.write(line)

    fr.close()
    fw.close()
except FileNotFoundError as e:
    print(e)

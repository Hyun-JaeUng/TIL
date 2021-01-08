
def print_book_title():
    print("파이썬 정복")

def print_book_publisher():
    print("한빛미디어")

for i in range(1,6):
    if i <= 3:
        print_book_title()
        print_book_publisher()
    else:
        print_book_publisher()



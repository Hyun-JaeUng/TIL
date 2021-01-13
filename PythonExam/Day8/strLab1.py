def myemail_info (s):
    if s.find("@") != -1:
        anslist = s.split("@")
        ans = tuple(anslist)
    else:
        ans = None
    return ans

print(myemail_info("ys9633@naver.com"))
print(myemail_info("squeaky@riot.com"))
print(myemail_info("kipers@naver.com"))

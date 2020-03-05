def abc(str):
    "打印任何传入的字符串"
    print(str)
    return
abc("1")
abc("2")


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print(
    "Name: ",name)
    print(
    "Age ",age)
    return



printinfo(age=50, name="miki")
printinfo(name="miki")


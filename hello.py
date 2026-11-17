# import keyword
from fileinput import close
from functools import reduce

# print("Hello World!")
#
# age = 25
# print(age)
#
# 姓名 = "张三"
# 姓名 = "李四"
# print(姓名)
#
# print("Class".isidentifier() and keyword.iskeyword("Class"))
#
# input("请输入：")

names = ["aa","bb","cc"]
newName = [name for name in names if name == "aa"]
print(newName)

newName = {name: name.upper() for name in names}
print(newName)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]

def cal(numbers) :
    print(reduce(lambda x, y: x + y, numbers))

cal(numbers)
cal(even_numbers)
cal(names)

with open("demo.py", 'a+') as hello:
    lines = hello.readlines()
    for line in lines:
        print(line)

    hello.write("\n\n")

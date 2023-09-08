"""
try:
    pass
except <Exception,ex:> --> 报错的提示名称（python3 语法 Exception as ex:)
    pass
"""

while True:
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        print(result)

    except Exception as e:  # python3 语法
        print("请输入数字！！！")

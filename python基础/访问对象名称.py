class Foo(object):

    def __init__(self):
        self.name = 'alex'

    def func(self):
        return 'func'


obj = Foo()

# 访问字段
print(obj.name)
# 执行方法
obj.func()

class Foo(object):
    """ 检查是否obj是否是类 cls 的对象 """
    pass


obj = Foo()

print(isinstance(obj, Foo))


class Foo(object):
    """ 检查sub类是否是 super 类的派生类 """
    pass


class Bar(Foo):
    pass


print(issubclass(Bar, Foo))  #

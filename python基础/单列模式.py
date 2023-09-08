class Foo(object):
    """ 创建单列模式 """

    __instance = None

    @staticmethod
    def singleton():
        if Foo.__instance:
            return Foo.__instance
        else:
            Foo.__instance = Foo()
            return Foo.__instance


# ########### 获取实例 ###########
obj = Foo.singleton()  # 单列模式的调用不能直接 obj.Foo(), 而是特殊方法 obj = Foo.singleton()

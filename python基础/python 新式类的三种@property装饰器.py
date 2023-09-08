# ############### 定义 ###############
class Goods(object):
    """ 新式类中的属性有三种访问方式，并分别对应了三个被@property、
    @方法名.setter、@方法名.deleter修饰的方法 """

    def __init__(self):
        self.num = 0

    @property
    def price(self):
        return '@property'

    @price.setter
    def price(self, value):
        self.num = value
        print(value)

    @price.deleter
    def price(self):
        print('@price.deleter')


# ############### 调用 ###############
obj = Goods()

print(obj.price)  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 123  # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price  # 自动执行 @price.deleter 修饰的 price 方法

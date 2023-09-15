import time

user_list = {
    "username": '',
}


def authentication(func):
    """ 对字典进行验证 """

    def foo(*args, **kwargs):
        if user_list["username"]:
            print("已登录。")
            result = func(*args, **kwargs)
            return result

        global name  # 对 name 进行全局变量定义
        name = input("未登录，请输入用户名：")
        pwd = int(input("请输入密码："))

        if name == 'dingyang' and pwd == 123:
            user_list["username"] = name  # 将 name 保存到字典
            result = func(*args, **kwargs)
            return result

        else:
            print("用户名或密码错误！！！")

    return foo


global name


def run_time(func):
    def time_user(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Run time is %s:" % (end_time - start_time))
        return result

    return time_user


@authentication
@run_time
def index_1():
    print("Welcome, %s" % name)
    time.sleep(1)
    return 123


@authentication
def index_2(user):
    print("Welcome, %s" % user)


a = index_1()
print(a)

index_2('dingyang')


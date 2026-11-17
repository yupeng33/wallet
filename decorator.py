def log_class(cls):
    """类装饰器，在调用方法前后打印日志"""

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)  # 实例化原始类

        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")

    return Wrapper  # 返回包装后的类


@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")


obj = MyClass()
obj.display()


class SingletonDecorator:
    """类装饰器，使目标类变成单例模式"""

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        """拦截实例化过程，确保只创建一个实例"""
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Database:
    def __init__(self):
        print("Database 初始化")


db1 = Database()
db2 = Database()
print(db1 is db2)  # True，说明是同一个实例
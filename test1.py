import time


# for i in range(101): # 添加进度条图形和百分比
#     bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
#     print(f"\r{bar} {i:3}%", end='', flush=True)
#     time.sleep(0.05)
# print()

a, b = 0, 1
while b < 10:
    a, b = b, a + b
    print(b, end=' ')

with open('test.txt', 'w') as f:
    f.write('Hello World!')

with open('test.txt', 'r') as f:
    f.read(100)
    print(f.read())

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False

# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))

from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

# 使用示例
with tag("h1"):
    print("这是一个标题")

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)

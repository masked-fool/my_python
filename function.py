"""
Python 函数(Function)基础知识

1. 函数定义与调用:
   - 定义: def function_name(parameters): body
   - 调用: function_name(arguments)
   - 返回值: return statement (可选，无return则返回None)

2. 参数类型:
   - 位置参数: 基于位置传递的参数
   - 关键字参数: 基于名称传递的参数 func(name='value')
   - 默认参数: 在定义时指定默认值 def func(param=default_value)
   - 可变位置参数: 接收任意数量的位置参数 def func(*args)
   - 可变关键字参数: 接收任意数量的关键字参数 def func(**kwargs)
   - 仅位置参数(Python 3.8+): 使用 / 分隔，之前的参数只能按位置传递
   - 仅关键字参数: 使用 * 分隔，之后的参数只能按关键字传递

3. 作用域与命名空间:
   - 局部作用域: 函数内部定义的变量
   - 全局作用域: 模块级别定义的变量
   - global关键字: 在函数内部使用全局变量
   - nonlocal关键字: 在嵌套函数中使用外层函数的变量

4. 函数特性:
   - 函数是一等公民: 可作为参数传递、作为返回值、赋值给变量
   - 嵌套函数: 函数内部定义的函数
   - 闭包: 捕获并记住创建它的环境中变量的函数
   - 递归: 函数调用自身
   - 匿名函数: lambda表达式 lambda params: expression

5. 函数文档:
   - 文档字符串(docstring): 定义在函数开头的多行字符串，描述函数用途
   - 注释: 使用#添加单行注释
   - 类型注解(Python 3.5+): 参数和返回值的类型提示 def func(param: type) -> return_type

6. 高级函数概念:
   - 纯函数: 相同输入总是产生相同输出，无副作用
   - 高阶函数: 接受函数作为参数或返回函数的函数
   - 函数装饰器: 修改或增强函数行为 @decorator
   - 生成器函数: 使用yield语句的函数，返回生成器对象
   - 协程函数(Python 3.5+): 使用async/await的异步函数
"""


def add(a, b):
    """
    将两个数相加并返回结果

    参数:
        a: 第一个加数
        b: 第二个加数

    返回:
        两个参数的和
    """
    return a + b


print(add(1, 2))  # 输出: 3

# 其他函数示例

# 带默认参数的函数


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("世界"))  # 输出: Hello, 世界!
print(greet("朋友", "你好"))  # 输出: 你好, 朋友!

# 可变参数函数


def sum_all(*numbers):
    return sum(numbers)


print(sum_all(1, 2, 3, 4, 5))  # 输出: 15

# 关键字可变参数


def print_person_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print_person_info(name="张三", age=30, city="北京")

# 闭包示例


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment


my_counter = counter()
print(my_counter())  # 输出: 1
print(my_counter())  # 输出: 2

# lambda表达式


def square(x): return x ** 2


print(square(5))  # 输出: 25

# 高阶函数


def apply_twice(func, value):
    return func(func(value))


print(apply_twice(square, 3))  # 输出: 81 (3² = 9, 9² = 81)

# 装饰器


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def multiply(a, b):
    return a * b


print(multiply(3, 4))  # 输出: 调用函数: multiply 然后是 12

# 生成器函数


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)  # 输出: 1 2 3 4 5

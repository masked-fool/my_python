"""
Python 类(Class)基础知识

1. 类定义与实例化:
   - 定义: class ClassName: body
   - 实例化: instance = ClassName(arguments)
   - 构造函数: __init__(self, ...) - 初始化实例
   - self: 表示实例本身的引用

2. 类特性:
   - 属性: 实例变量(self.attribute)和类变量(在类中直接定义)
   - 方法: 实例方法(第一个参数是self)、类方法(@classmethod)、静态方法(@staticmethod)
   - 访问控制: 
     * 公开属性/方法: 直接定义
     * 私有属性/方法: 以双下划线开头(__private)
     * 保护属性/方法: 以单下划线开头(_protected)
   - 属性装饰器: @property, @attribute.setter, @attribute.deleter

3. 继承与多态:
   - 单继承: class Child(Parent): ...
   - 多继承: class Child(Parent1, Parent2): ...
   - 方法重写: 在子类中定义同名方法
   - super(): 调用父类方法
   - 抽象基类: 使用abc模块定义接口
   - 多态: 不同类对同一方法的不同实现

4. 特殊方法(魔术方法):
   - __init__: 构造函数
   - __del__: 析构函数
   - __str__: 字符串表示
   - __repr__: 开发者字符串表示
   - __len__: 长度
   - __getitem__: 索引访问
   - __setitem__: 索引赋值
   - __call__: 使实例可调用
   - __add__: 加法操作
   - __eq__: 相等比较
   - __lt__: 小于比较
   - __iter__: 迭代器协议
   - __next__: 迭代器协议

5. 类装饰器:
   - @dataclass: 自动生成特殊方法
   - @property: 将方法转换为属性
   - @classmethod: 定义类方法
   - @staticmethod: 定义静态方法
   - @abstractmethod: 定义抽象方法

6. 元类:
   - 类的类，用于创建类
   - 默认元类: type
   - 自定义元类: class MetaClass(type): ...
   - 使用元类: class MyClass(metaclass=MetaClass): ...

7. 类设计原则:
   - 单一职责原则: 一个类只做一件事
   - 开放封闭原则: 对扩展开放，对修改封闭
   - 里氏替换原则: 子类必须能替换父类
   - 接口隔离原则: 使用多个专门的接口
   - 依赖倒置原则: 依赖抽象而非具体实现

8. 类的高级特性:
   - 描述符: 控制属性访问
   - 上下文管理器: __enter__, __exit__
   - 迭代器: __iter__, __next__
   - 生成器: yield语句
   - 协程: async/await
"""

from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


dog = Dog("旺财", 3)
dog.eat("骨头")
dog.bark()

# 更多类示例

# 类变量与实例变量


class Person:
    # 类变量
    species = "人类"

    def __init__(self, name):
        # 实例变量
        self.name = name

# 属性装饰器


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius ** 2

# 特殊方法


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# 抽象基类


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 描述符


class ValidatedProperty:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"值不能小于{self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"值不能大于{self.max_value}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    age = ValidatedProperty(min_value=0, max_value=150)
    score = ValidatedProperty(min_value=0, max_value=100)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

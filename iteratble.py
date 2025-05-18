"""
Python 可迭代对象(Iterables)操作指南

可迭代对象(Iterables)是Python中一类可以逐个返回其成员的对象。主要包括：

1. 内置可迭代类型：
   - 列表(list)、元组(tuple)、字符串(str)
   - 字典(dict) - 迭代键
   - 集合(set)、冻结集合(frozenset)
   - 范围(range)
   - 文件对象(file)

2. 迭代基本操作：
   - for循环: for item in iterable
   - list/set/tuple构建: list(iterable)
   - 推导式: [x for x in iterable]
   - 解包: a, b, c = iterable
   - 成员检查: x in iterable

3. while循环与迭代：
   - 基本语法: while condition: block
   - 迭代器手动迭代: 
     * iterator = iter(iterable)
     * while True: try: item = next(iterator) except StopIteration: break
   - 索引迭代: 
     * i = 0
     * while i < len(sequence): item = sequence[i]; i += 1
   - 条件迭代: while condition_based_on(item): item = next_item()
   - 无限循环: while True: ... (需要有break条件)
   - 控制语句: 
     * break - 完全跳出循环
     * continue - 跳过当前迭代，继续下一次迭代
   - else子句: while condition: block else: no_break_block

4. 迭代器函数与工具：
   - iter(obj) - 获取迭代器
   - next(iterator) - 获取下一个元素
   - enumerate(iterable, start=0) - 返回索引和元素对
   - zip(*iterables) - 并行迭代多个可迭代对象
   - map(function, iterable) - 对每个元素应用函数
   - filter(function, iterable) - 过滤元素
   - sorted(iterable, key=None, reverse=False) - 排序
   - reversed(sequence) - 反向迭代
   - any(iterable) - 如果任一元素为True则返回True
   - all(iterable) - 如果所有元素为True则返回True
   - sum(iterable, start=0) - 求和
   - max(iterable, key=None) - 最大值
   - min(iterable, key=None) - 最小值

5. itertools模块中的迭代器工具：
   - itertools.count(start, step) - 无限计数
   - itertools.cycle(iterable) - 循环迭代
   - itertools.repeat(elem, n=None) - 重复元素
   - itertools.chain(*iterables) - 连接多个迭代器
   - itertools.islice(iterable, start, stop, step) - 切片
   - itertools.tee(iterable, n=2) - 复制迭代器
   - itertools.product(*iterables) - 笛卡尔积
   - itertools.permutations(iterable, r=None) - 排列
   - itertools.combinations(iterable, r) - 组合

6. range对象参数说明：
   - range(stop) - 生成0到stop-1的序列
   - range(start, stop) - 生成start到stop-1的序列
   - range(start, stop, step) - 生成从start开始，步长为step的序列（直到stop-1）
"""

# 使用range的示例
for item in range(1, 10, 2):  # 参数: 起始值1，结束值10(不包含)，步长2
    print(item)  # 输出: 1, 3, 5, 7, 9

# while循环示例
print("\nwhile循环基本示例:")
count = 1
while count < 5:
    print(count)
    count += 1

# 使用while循环手动迭代列表
print("\nwhile循环手动迭代列表:")
fruits = ['apple', 'banana', 'cherry']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# 使用while和迭代器
print("\nwhile循环与迭代器:")
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break

# while循环与break
print("\nwhile循环与break:")
num = 0
while True:
    print(num)
    num += 1
    if num >= 5:
        break

# while循环与continue
print("\nwhile循环与continue:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # 跳过偶数
        continue
    print(num)  # 只打印奇数

# while循环与else
print("\nwhile循环与else:")
count = 1
while count < 5:
    print(count)
    count += 1
else:
    print("循环正常完成，没有break")

# while循环处理用户输入
print("\nwhile循环处理用户输入示例:")
"""
answer = ''
while answer.lower() != 'quit':
    answer = input("输入'quit'退出: ")
    if answer.lower() != 'quit':
        print(f"你输入了: {answer}")
"""

# 列表迭代
print("\n列表迭代示例:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 字典迭代
print("\n字典迭代示例:")
person = {'name': '张三', 'age': 30, 'city': '北京'}
# 迭代键
for key in person:
    print(key, ':', person[key])
# 迭代键值对
for key, value in person.items():
    print(key, ':', value)
# 只迭代值
for value in person.values():
    print(value)

# 字符串迭代
print("\n字符串迭代示例:")
for char in "Python":
    print(char)

# enumerate示例 - 获取索引和值
print("\nenumerate示例:")
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# zip示例 - 并行迭代
print("\nzip示例:")
names = ['张三', '李四', '王五']
ages = [20, 25, 30]
for name, age in zip(names, ages):
    print(f"{name} 今年 {age} 岁")

# 列表推导式
print("\n列表推导式:")
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 字典推导式
print("\n字典推导式:")
name_to_age = {name: age for name, age in zip(names, ages)}
print(name_to_age)

# 集合推导式
print("\n集合推导式:")
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# filter示例
print("\nfilter示例:")
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print(even_numbers)  # [0, 2, 4, 6, 8]

# map示例
print("\nmap示例:")
doubled = list(map(lambda x: x * 2, range(1, 6)))
print(doubled)  # [2, 4, 6, 8, 10]

# sorted示例
print("\nsorted示例:")
print(sorted(fruits))  # 按字母排序
print(sorted(fruits, key=len))  # 按长度排序

# any和all示例  
print("\nany和all示例:")  
print(any([False, False, True]))  # True
print(all([True, True, False]))   # False

# 无限迭代器示例(小心使用)
import itertools
print("\nitertools示例:")
# 生成10个连续的奇数
odd_numbers = list(itertools.islice(itertools.count(1, 2), 10))
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 组合和排列
print("\n组合和排列:")
print(list(itertools.combinations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.permutations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


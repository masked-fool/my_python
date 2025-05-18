"""
Python List 常用方法:

1. append(x) - 在列表末尾添加一个元素
2. extend(iterable) - 将可迭代对象的所有元素添加到列表末尾
3. insert(i, x) - 在指定位置插入元素
4. remove(x) - 删除列表中第一个值为x的元素
5. pop([i]) - 删除并返回指定位置的元素，默认为最后一个
6. clear() - 删除列表中的所有元素
7. index(x[, start[, end]]) - 返回列表中第一个值为x的元素的索引
8. count(x) - 返回元素x在列表中出现的次数
9. sort(*, key=None, reverse=False) - 对列表元素进行排序
10. reverse() - 反转列表中的元素
11. copy() - 返回列表的浅拷贝

其他常用的列表操作:
- len(list) - 获取列表长度
- max(list) - 获取列表中的最大值
- min(list) - 获取列表中的最小值
- list(seq) - 将序列转换为列表
- in - 检查元素是否在列表中 成员运算符
- + - 连接列表 连接运算符
- * - 重复列表 解包运算符
- [start:end:step] - 切片操作
"""

# 创建一个包含数字1到5的列表
num_list = [1, 2, 3, 4, 5]

# 打印整个列表
print(num_list)  # 输出: [1, 2, 3, 4, 5]

# 在列表末尾添加数字6
num_list.append(6)

# 打印添加元素后的列表
print(num_list)  # 输出: [1, 2, 3, 4, 5, 6]

# 打印列表的第一个元素（索引0）
print(num_list[0])  # 输出: 1

# 在列表的开头（索引0位置）插入数字0
num_list.insert(0, 0)

# 打印插入元素后的列表
print(num_list)  # 输出: [0, 1, 2, 3, 4, 5, 6]

# 查找列表中的最大值
max_num = max(num_list)

# 打印最大值
print(max_num)  # 输出: 6

# 查找列表中的最小值
min_num = min(num_list)

# 打印最小值
print(min_num)  # 输出: 0

# 从列表中移除数字6
num_list.remove(6)

# 打印移除元素后的列表
print(num_list)  # 输出: [0, 1, 2, 3, 4, 5]

# 移除并返回列表最后一个元素
num_list.pop()

# 打印移除末尾元素后的列表
print(num_list)  # 输出: [0, 1, 2, 3, 4]

# 清空列表中的所有元素
num_list.clear()

# 打印清空后的列表
print(num_list)  # 输出: []

# 对列表进行排序（但列表为空，没有实际效果）
num_list.sort()

# 打印排序后的列表
print(num_list)  # 输出: []

# 反转列表（但列表为空，没有实际效果）
num_list.reverse()

# 打印反转后的列表
print(num_list)  # 输出: []

# 将另一个列表[7, 8, 9]的所有元素添加到当前列表
num_list.extend([7, 8, 9])

# 打印扩展后的列表
print(num_list)  # 输出: [7, 8, 9]

# 计算数字1在列表中出现的次数（此处没有保存返回值）
num_list.count(1)  # 应该是：count_1 = num_list.count(1)

# 打印列表（count方法不会改变列表）
print(num_list)  # 输出: [7, 8, 9]

# 查找数字1在列表中的索引位置（此处会抛出ValueError，因为列表中没有1）
# 应该使用try-except处理可能的异常
try:
   index_1 = num_list.index(1)
except ValueError:
   print("1 not in list")

# 打印列表
print(num_list)  # 输出: [7, 8, 9]

# 复制列表（此处没有保存返回值）
num_list_copy = num_list.copy()  # 正确用法

# 打印列表（copy方法不会改变原始列表）
print(num_list)  # 输出: [7, 8, 9]

# 移除并返回列表中索引为0的元素
num_list.pop(0)

# 打印移除索引0元素后的列表
print(num_list)  # 输出: [8, 9]

# 从列表中移除数字1（会抛出ValueError，因为列表中没有1）
# 应该使用try-except处理可能的异常
try:
    num_list.remove(1)
except ValueError:
    print("1 not in list")

# 打印列表
print(num_list)  # 输出: [8, 9]

# Python列表没有push方法，应该使用append
# num_list.push(1)  # 错误
num_list.append(1)  # 正确

# 打印列表
print(num_list)  # 输出: [8, 9, 1]

# 移除并返回列表的最后一个元素
num_list.pop()

# 打印移除末尾元素后的列表
print(num_list)  # 输出: [8, 9]

list_3 = [*num_list, *num_list_copy] # 解包 num_list 和 num_list_copy, 合并成一个列表
print(list_3) # 输出: [8, 9, 7, 8, 9]
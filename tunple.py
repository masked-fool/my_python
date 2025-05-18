"""
Python 元组(tuple)常用方法和操作:

1. count(x) - 返回元素x在元组中出现的次数
2. index(x[, start[, end]]) - 返回元组中第一个值为x的元素的索引，可选择起始和结束位置

函数签名解读说明:
- 没有中括号[]的参数是必选参数，如 x
- 被中括号[]包围的参数是可选参数，如 [start] 和 [end]
- 嵌套的中括号表示内层参数依赖于外层参数，如 [, start[, end]] 表示只有提供了start才能提供end
- 逗号表示参数之间的分隔，[, start] 中的逗号表示start跟在前面的参数后面

具体调用形式:
- tuple.index(x) - 只提供要查找的值
- tuple.index(x, start) - 提供要查找的值和起始搜索位置
- tuple.index(x, start, end) - 提供要查找的值、起始位置和结束位置

其他常用的元组操作:
- len(tuple) - 获取元组的长度
- max(tuple) - 获取元组中的最大值
- min(tuple) - 获取元组中的最小值
- tuple(seq) - 将序列转换为元组
- in - 检查元素是否在元组中
- + - 连接元组
- * - 重复元组
- [index] - 索引访问
- [start:end:step] - 切片操作
- 解包 - 将元组中的值分配给多个变量

注意: 元组是不可变的数据类型，所以没有像列表那样的修改方法(如append、remove、pop等)
"""

tunple = (1, 2, 3, 4, 5)
print(tunple)  # 输出: (1, 2, 3, 4, 5)

# 解包
a, b, c, d, e = tunple
print(a, b, c, d, e)  # 输出: 1 2 3 4 5

# 示例：元组方法的使用
print("\n元组方法示例:")

# 计数
print("3出现的次数:", tunple.count(3))  # 输出: 1

# 查找索引 - 演示不同的调用形式
print("元素4的索引:", tunple.index(4))  # 基本形式
# print("从索引2开始查找3:", tunple.index(3, 2))  # 指定起始位置
# print("在索引1到4之间查找5:", tunple.index(5, 1, 5))  # 指定范围

# 长度
print("元组长度:", len(tunple))  # 输出: 5

# 连接
tunple2 = (6, 7, 8)
combined = tunple + tunple2
print("连接后的元组:", combined)  # 输出: (1, 2, 3, 4, 5, 6, 7, 8)

# 重复
repeated = tunple * 2
print("重复后的元组:", repeated)  # 输出: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 切片
print("部分切片:", tunple[1:4])  # 输出: (2, 3, 4)

# 检查成员
print("5在元组中:", 5 in tunple)  # 输出: True
print("6在元组中:", 6 in tunple)  # 输出: False

# 最大值和最小值
print("最大值:", max(tunple))  # 输出: 5
print("最小值:", min(tunple))  # 输出: 1

# 部分解包（Python 3.x）
first, *middle, last = tunple
print("部分解包:", first, middle, last)  # 输出: 1 [2, 3, 4] 5

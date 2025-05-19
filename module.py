"""
Python 模块(Module)基础知识

1. 模块定义与导入:
   - 模块: 包含Python代码的文件(.py)
   - 包: 包含__init__.py文件的目录，可以包含多个模块
   - 导入方式:
     * import module_name - 导入整个模块
     * from module_name import item - 导入特定项
     * from module_name import * - 导入所有项(不推荐)
     * import module_name as alias - 使用别名导入
     * from module_name import item as alias - 导入特定项并使用别名

2. 标准库模块:
   - math: 数学函数和常量
   - random: 随机数生成
   - datetime: 日期和时间处理
   - os: 操作系统接口
   - sys: 系统特定参数和函数
   - json: JSON数据处理
   - re: 正则表达式
   - collections: 容器数据类型
   - itertools: 迭代器函数
   - functools: 高阶函数和可调用对象操作

3. 模块搜索路径:
   - 当前目录
   - PYTHONPATH环境变量中的目录
   - 标准库目录
   - 第三方包目录(site-packages)
   - 可以通过sys.path查看和修改搜索路径

4. 模块特性:
   - __name__: 模块名称，当作为主程序运行时为'__main__'
   - __file__: 模块文件的路径
   - __doc__: 模块的文档字符串
   - __all__: 定义使用from module import *时导入的名称列表

5. 包的组织:
   - 包是包含多个模块的目录
   - 必须包含__init__.py文件(可以是空文件)
   - 可以嵌套形成子包
   - 相对导入: 使用.和..表示当前包和父包

6. 模块使用最佳实践:
   - 避免循环导入
   - 使用if __name__ == '__main__'区分模块和脚本
   - 明确导入所需内容，避免使用*
   - 使用有意义的模块和包名
   - 保持模块的单一职责
   - 使用__all__控制导出内容

7. 虚拟环境与依赖管理:
   - venv: 创建隔离的Python环境
   - pip: 包管理器
   - requirements.txt: 依赖列表
   - setup.py: 包安装配置
   - pyproject.toml: 现代Python项目配置
"""

import sys
from random import randint, choice
import datetime as dt
import math
from math import sqrt

print(sqrt(16))  # 输出: 4.0

# 其他模块导入示例

# 导入整个模块
print(math.pi)  # 输出: 3.141592653589793

# 使用别名
now = dt.datetime.now()
print(now)  # 输出当前日期和时间

# 导入多个项
print(randint(1, 10))  # 输出1到10之间的随机整数
print(choice(['apple', 'banana', 'cherry']))  # 随机选择一个元素

# 条件导入
try:
    import numpy as np
    print("NumPy已安装")
except ImportError:
    print("NumPy未安装")

# 模块作为脚本运行
if __name__ == '__main__':
    print("这个模块被直接运行")
else:
    print("这个模块被导入")

# 查看模块路径
print(sys.path)  # 显示Python搜索模块的路径

# 包导入示例
# 假设有一个名为my_package的包，包含module1和module2
# from my_package import module1
# from my_package.module2 import some_function

# 相对导入示例(在包内部)
# from . import sibling_module
# from .. import parent_module
# from ..sibling_package import sibling_module

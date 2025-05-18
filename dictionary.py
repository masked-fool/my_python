"""
Python Dictionary 常用方法:

1. clear() - 删除字典中的所有元素
2. copy() - 返回字典的浅拷贝
3. fromkeys(seq[, value]) - 创建一个新字典，以序列seq中的元素为键，value为值
4. get(key[, default]) - 返回指定键的值，如果键不在字典中返回默认值
5. items() - 返回由键值对组成的视图对象
6. keys() - 返回由字典键组成的视图对象
7. pop(key[, default]) - 删除指定键并返回对应的值
8. popitem() - 删除并返回最后插入的键值对
9. setdefault(key[, default]) - 如果键存在，返回其值；如果不存在，插入键并设为默认值
10. update([other]) - 用其他字典或键值对更新当前字典
11. values() - 返回由字典值组成的视图对象

其他常用的字典操作:
- len(dict) - 获取字典中键值对的数量
- in - 检查键是否在字典中
- del dict[key] - 删除特定键值对
- dict[key] = value - 添加或更新键值对
- dict1 | dict2 (Python 3.9+) - 合并两个字典
- dict |= {a: 1} - 就地更新，合并字典
- new_dict = {
    **dict1, # 展开dict1
    a: 1 # 添加a: 1
}
"""

# 创建一个包含用户信息的字典
user = {
    "name": "张三",
    "age": 20,
    "gender": "男",
    "city": "北京",
    "email": "zhangsan@163.com",
    "phone": "13800138000"
}

# 将用户字典放入一个列表中
user_list = [user]
print(user_list)  # 输出: [{'name': '张三', 'age': 20, 'gender': '男', 'city': '北京', 'email': 'zhangsan@163.com', 'phone': '13800138000'}]

# 示例：字典方法的使用
print("\n字典方法示例:")

# 获取所有键
print("所有键:", user.keys())

# 获取所有值
print("所有值:", user.values())

# 获取所有键值对
print("所有键值对:", user.items())

# 使用get方法获取值（提供默认值）
print("获取职业(不存在):", user.get("occupation", "未知"))

# 更新字典
user.update({"occupation": "工程师", "salary": 10000})
print("更新后的字典:", user)

# 删除并返回指定键的值
removed_age = user.pop("age")
print(f"删除的年龄: {removed_age}, 删除后的字典: {user}")

# 设置默认值（键不存在时）
user.setdefault("education", "本科")
print("设置默认教育程度后:", user)

# 删除并返回最后一个键值对
last_item = user.popitem()
print(f"删除的最后一项: {last_item}, 删除后的字典: {user}")

# 创建字典的浅拷贝
user_copy = user.copy()
print("字典的浅拷贝:", user_copy)

# 使用fromkeys创建新字典
new_dict = dict.fromkeys(["name", "age", "gender"], "未知")
print("使用fromkeys创建的新字典:", new_dict)

# 清空字典
user_copy.clear()
print("清空后的字典:", user_copy)
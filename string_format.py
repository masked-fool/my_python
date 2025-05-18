name = "张三"
age = 20
gender = "男"
city = "北京"
email = "zhangsan@163.com"
phone = "13800138000"

formatted_string = f"""
{name}
{age}
{gender}
{city}
{email}
{phone}
"""

print(1, formatted_string)

formatted_string = """
{name}
{age}
{gender}
{city}
{email}
{phone}
""".format(name=name, age=age, gender=gender, city=city, email=email, phone=phone)

print(2, formatted_string)

formatted_string = """
{0}
{1}
{2}
{3}
{4}
{5}
""".format(name, age, gender, city, email, phone)

print(3, formatted_string)

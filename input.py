# 获取用户输入
user_weight = input("Enter your weight (kg): ")
user_height = input("Enter your height (m): ")

# 将输入转换为浮点数
weight = float(user_weight)
height = float(user_height)

# 计算 BMI: 体重(kg) / 身高(m)的平方
bmi = weight / (height ** 2)

# 显示结果
print(f"Your BMI is: {bmi:.2f}")

# 分析 BMI 结果
if bmi < 18.5:
    print("分类：体重过轻")
elif bmi < 24.0:
    print("分类：正常范围")
elif bmi < 28.0:
    print("分类：超重")
elif bmi < 30.0:
    print("分类：轻度肥胖")
elif bmi < 40.0:
    print("分类：中度肥胖")
else:
    print("分类：重度肥胖")










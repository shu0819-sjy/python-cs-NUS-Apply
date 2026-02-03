print("====简易计算器====")
num1 = int(input("请输入第一个数字:"))
num2 = int(input("请输入第二个数字:"))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "除数不能为0"


print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {sub_result}")
print(f"{num1} * {num2} = {mul_result}")
print(f"{num1} / {num2} = {div_result}")

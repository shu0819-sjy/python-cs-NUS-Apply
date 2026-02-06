# 写法1：while循环（入门理解）
sum1 = 0
x = 1
while x <= 100:
    sum1 += x
    x += 1
print(f"1-100求和（while）：{sum1}")

# 写法2：for循环（常规推荐）
sum2 = 0
for num in range(1, 101):
    sum2 += num
print(f"1-100求和（for）：{sum2}")

# 写法3：for+range步长（简洁版，可选）
sum3 = sum(range(1, 101))  # sum()直接求和可迭代对象
print(f"1-100求和（sum+range）：{sum3}")

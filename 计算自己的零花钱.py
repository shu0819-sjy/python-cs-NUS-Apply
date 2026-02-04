total = 0
for day in range (1,8):
    amount = float ( input (f"请输入你第{day}天的零花钱"))
    total += amount
print (f"七天一共得了{total}块的零花钱")


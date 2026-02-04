
total = 0
for i in range (1,6):
  money = input (f"输入你第{i}件商品的价格")
  total += float( money )
if total > 100:
    print (f"一共是{total - 10 }元")

else:
    print (f" 一共是{total}元")

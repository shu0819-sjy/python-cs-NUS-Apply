count = 0
while count < 8:
    msg = input("喝了一杯请输入 打卡 ：")
    if msg == "打卡":
        count += 1
        print(f"已喝{count}杯，还差{8-count}杯")
print("今日喝水达标！")

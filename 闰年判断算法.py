while True:

    year_input = input("请输入要判断的年份（正整数）：")
    if not year_input.isdigit():
        print("❌ 输入错误！请输入正整数年份，重新输入～")
        continue
    year = int(year_input)
    if year <= 0:
        print("❌ 年份错误！请输入大于0的正整数，重新输入～")
        continue
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年 → 是闰年")
    else:
        print(f"{year}年 → 不是闰年")
    break

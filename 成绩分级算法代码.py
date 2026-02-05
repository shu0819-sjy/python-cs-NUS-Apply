
score_input = input("请输入成绩（0-100）：")
assert score_input.isdigit(), "输入错误！请输入纯整数"
score = int(score_input)
assert 0 <= score <= 100, "分数错误！请输入0-100的整数"

if 90 <= score <= 100:
    grade = "优秀"
elif 80 <= score <= 89:
    grade = "良好"
elif 60 <= score <= 79:
    grade = "合格"
else:
    grade = "补考"
print(f"成绩：{score}分 → 等级：{grade}")

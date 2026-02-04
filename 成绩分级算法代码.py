temp = input("请输入你的成绩")
grade = int(temp)
if grade < 0 or grade > 100:
    print("出错了")
elif grade > 90:
    print("优秀")
elif grade > 80:
    print ("良好")
elif grade > 60 :
     print( " 及格")
else:
    print("不及格")

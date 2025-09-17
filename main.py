 num = int(input("请输入一个五位数："))
 ten_thousand = num // 10000
 thousand = (num % 10000) // 1000
 hundred = (num % 1000) // 100
 ten = (num % 100) // 10
 unit = num % 10
 # 判断是否为回文数：万位和个位相等，且千位和十位相等
 if ten_thousand == unit and thousand == ten:
     print("是回文数")
 else:
     print("不是回文数")

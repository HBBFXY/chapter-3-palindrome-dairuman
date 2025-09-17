 num = int(input("请输入一个五位数："))
 # 获取万位数字：将数字除以 10000 取整
 ten_thousand = num // 10000
 # 获取千位数字：先将数字对 10000 取余，再除以 1000 取整
 thousand = (num % 10000) // 1000
 # 获取百位数字：先将数字对 1000 取余，再除以 100 取整
 hundred = (num % 1000) // 100
 # 获取十位数字：先将数字对 100 取余，再除以 10 取整
 ten = (num % 100) // 10
 # 获取个位数字：将数字对 10 取余
 unit = num % 10
 # 判断是否为回文数：万位和个位相等，且千位和十位相等
 if ten_thousand == unit and thousand == ten:
     print(f"{num} 是回文数")
 else:
     print(f"{num} 不是回文数")

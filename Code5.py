# รับค่าตัวเลขจากผู้ใช้
num1 = float(input("ป้อนตัวเลขตัวแรก: "))
num2 = float(input("ป้อนตัวเลขตัวที่สอง: "))

# บวก
sum_result = num1 + num2
print("ผลบวก:", sum_result)

# ลบ
difference = num1 - num2
print("ผลลบ:", difference)

# คูณ
product = num1 * num2
print("ผลคูณ:", product)

# หาร (พร้อมตรวจสอบว่าไม่หารด้วยศูนย์)
if num2 != 0:
    quotient = num1 / num2
    print("ผลหาร:", quotient)
else:
    print("ไม่สามารถหารด้วยศูนย์ได้ครับ")
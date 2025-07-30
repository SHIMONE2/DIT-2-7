numbers = []
for i in range(5);
while True:
    try:
 num = int(input("ป้อนจำนวนเต็ม: "))
            numbers.append(num)
            break
        except ValueError:
            print("กรุณาป้อนเฉพาะจำนวนเต็ม")
            numbers.sort()
            print("ข้อมูลที่เรียงลำดับแล้ว:", numbers)
columns = int(input("Please enter your Columns : "))

for nums in range(0, 101, 1):       #นับเลข 0 - 100 ทีละ 1
    if nums % columns == 0:         #ถ้า nums หาร columns ลงตัว
        print("\n", end="")         #ขึ้นบรรทัดใหม่
    print(nums, end=" ")            #แสดงตัวเลข

columns = int(input("Please enter your Columns : "))

for nums in range(0, 101, 1):
    for count in range(0, 100, columns):
        if nums == count:
            print("\n")
    
    print(nums, end=" ")
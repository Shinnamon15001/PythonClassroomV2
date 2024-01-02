columns = int(input("Enter the number of columns : "))
count = 0

for i in range(1, 101):
    num = str(i)
    print(num.ljust(2), end=" ")
    count += 1
    if count % columns == 0:
        print("\n")
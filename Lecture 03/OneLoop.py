columns = int(input("Please enter your Columns : "))

for nums in range(1, 101, 1):
    if nums % columns == 0:
        print("\n", end="")
    print(nums, end=" ")
print("Please select your operation \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")

operation = float(input("Input your operation : "))

if operation == 1:
    first_number, secound_number = int(input("Enter your first number : ")), int(input("Enter your secound number : "))
    print(first_number, "+", secound_number, "=", first_number + secound_number)
elif operation == 2:
    first_number, secound_number = int(input("Enter your first number : ")), int(input("Enter your secound number : "))
    print(first_number, "-", secound_number, "=", first_number - secound_number)
elif operation == 3:
    first_number, secound_number = int(input("Enter your first number : ")), int(input("Enter your secound number : "))
    print(first_number, "*", secound_number, "=", first_number * secound_number)
elif operation == 4:
    first_number, secound_number = int(input("Enter your first number : ")), int(input("Enter your secound number : "))
    print(first_number, "/", secound_number, "=", first_number / secound_number)
else:
    print("Error")

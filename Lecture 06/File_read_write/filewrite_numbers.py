def main():
    outfile = open("numbers.txt", "w")
    
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    num3 = int(input("Enter Third Number : "))
    
    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")
    
    outfile.close()
    print("Data written to numbers.txt")

main()
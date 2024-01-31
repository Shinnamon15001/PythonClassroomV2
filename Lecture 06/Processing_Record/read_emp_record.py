def main():
    infile = open("employees.txt" , "r")

    while True:
        line1 = infile.readline()
        line2 = infile.readline()
        line3 = infile.readline()

        line1 = line1.rstrip("\n")
        line2 = line2.rstrip("\n")
        line3 = line3.rstrip("\n")
        
        if line1 == "":
            break
        
        for j in range(1):
            print("Name :", line1)
            print("ID :", line2)
            print("Dept : ", line3)
            print()

    infile.close()
main()
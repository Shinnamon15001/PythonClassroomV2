repeat = "y"

while repeat == "y":
    first_name = "Holly"        #input("Enter your first name : ")
    last_name =  "Gaddis"       #input("Enter your last name : ")
    id_number = "CSC34899"      #input("Enter your id number : ")
    print("\n","Your system login name is :", first_name[0: 3: 1], last_name[0: 3: 1], id_number[5:],"\n",sep="")
    
    repeat = input("Do you want to try again? : ")
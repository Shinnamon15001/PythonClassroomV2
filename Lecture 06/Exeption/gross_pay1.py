def main():
    try:
        hours = int(input("How many hours you want to work : "))

        pay_rate = float(input("Enter your hourly pay rate : "))

        gross_pay = hours * pay_rate

        print("Gross pay : ", format(gross_pay, ",.2f") , sep=" ")
    
    except ValueError:
        print("Error : Hours worked and hourly pay rate must be valid integer.")
main()
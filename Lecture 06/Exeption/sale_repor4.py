def main():
    a, b = map(int, input("Input 2 integer values : ").split())

    divide(a, b)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("Result is", result)
    finally:
        print("Executing finall clause")
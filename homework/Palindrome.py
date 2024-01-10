def palindrome(check_palindrome):
    
    check_palindrome = ''.join(filter(str.isalnum, check_palindrome.lower()))

    return check_palindrome == check_palindrome[::-1]

repeat = "y"

while repeat == "y":
    word = input("Input your word to check palindrome : ")

    result = palindrome(word)
    if result:
        print("Palindrome")
    else:
        print("Not Palindrome")

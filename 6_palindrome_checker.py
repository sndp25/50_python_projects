num = int(input("Enter number:"))

# Check if the number is negative
if num < 0:
    print("Given Number is Not Palindrome (Negative numbers can't be palindromes)")
else:
    rev_num = int(str(num)[::-1])

    if num == rev_num:
        print("Given Number is Palindrome")
    else:
        print("Given Number is Not Palindrome")

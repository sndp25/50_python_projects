#   Write a program that prints numbers from 1 to 100 but replaces multiples of 3 with “Fizz” and multiples of 5 with “Buzz.”

for i in range(1,100):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

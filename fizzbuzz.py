#ask user for a number
num = int(input("Enter a Number? "))

#Is the number divisible by both 3 and 5?
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz!!")

#Is it divisible by 3?
elif num % 3 == 0:
    print("Fizz")

#Is it divisible by 5?
elif num % 5 == 0:
    print("Buzz")

#If none of the above are true, print the number itself
else:
    print(num)
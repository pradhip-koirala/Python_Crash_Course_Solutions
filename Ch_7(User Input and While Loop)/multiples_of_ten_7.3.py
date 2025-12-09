
#combine int() and input() to reduce code lines.
num = int(input("Enter a number you like to check: "))

result = "multiple of ten." if num % 10 == 0 else "not a multiple of ten."


print("The number is",result,num)

f_num = input("Enter first number: ")
s_num = input("Enter second number: ")

try:
    if int(f_num) and int(s_num):
        add = int(f_num) + int(s_num)
        print(f"Addition is {add}")
except ValueError:
    print("You should type in numbers(nothing else)")

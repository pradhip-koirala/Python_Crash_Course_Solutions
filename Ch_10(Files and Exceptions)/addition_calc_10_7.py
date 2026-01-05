

while True:
    f_num = input("Enter first number: ")
    s_num = input("Enter second number: ")
    if f_num or s_num == 'q':
        break
    else:
        try:
            if int(f_num) and int(s_num):
                add = int(f_num) + int(s_num)
                print(f"Addition is {add}")
        except ValueError:
            print("You should type in numbers(nothing else)")

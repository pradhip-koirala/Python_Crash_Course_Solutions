# with open ('learning_python.txt') as file:
#     # lines = file.readlines()
#     content = file.read()



# print(content)
# print("this is the end")
# with open ('learning_python.txt') as file:
#     lines = file.readlines()
    

# for line in lines:
#     print(line.strip())

string_lists = []
with open ('learning_python.txt')as file:
    lists = file.readlines()
    string_lists.append(lists)

for lists in string_lists:
    print(lists)
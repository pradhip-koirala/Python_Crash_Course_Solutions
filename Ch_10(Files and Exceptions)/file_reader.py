# from pathlib import Path

# file_name = Path(__file__).parent / 'pi.txt'
# with open (file_name) as file:
#     lines = file.readlines()

# # for line in lines:
# #     print(line.rstrip())

# pi_string = ""
# for line in lines:
#     pi_string += line.rstrip()

# print(pi_string)
# print(len(pi_string))


# filename = 'pi_digits.txt'

# with open (filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

from pathlib import Path

file_path = Path(__file__).parent / 'pi.txt'

# with open(file_path) as file:
#     for lines in file.readlines():
#         print(lines.rstrip())

# file_name = 'pi_million_digits.txt'

# with open(filename) as file:
#     lines =file.readlines()

# pi_string = ""
# for line lines:
#     pi_string += line.strip()

# print(pi_string[:52]+ "....")
# print(len(pi_string))

birthday = input('enter your birthday, in the form mmddyy')
if birthday in pi_sitring:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first digits of pi")
    
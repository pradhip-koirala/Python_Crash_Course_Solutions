# filename = 'alice.txt'

# try: 
#     with open (filename) as file:
#         contents = file.read()
# except FileNotFoundError:
#     msg = 'Sorry, the file '+filename + ' does not exit.'
#     print(msg)
# else:
#     words = contents.split()
#     num_words = len(words)
#     print('the file '+filename + ' has about '+str(num_words)+ " words.")

def count_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        # msg = 'Sorry, the file '+filename+' does not exit.'
        # print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename + " has about " + str(num_words) + " words." )

# filename = 'alice.txt'
count_words('alice.txt')
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
with open('programming_poll', 'a') as file:
    while True:
        reason =input("Why you like programming (q to quit): ")
        if reason != 'q':
            file.write(reason+'\n')
        else:
            break


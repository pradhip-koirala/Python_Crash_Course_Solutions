from pathlib import Path

file_path = Path(__file__).parent / 'learning_python.txt'

with open (file_path) as file:
    for line in file.readlines():
        message = line.replace('python', 'c')
        print(message)
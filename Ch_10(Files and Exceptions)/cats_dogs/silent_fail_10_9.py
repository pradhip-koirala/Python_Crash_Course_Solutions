from pathlib import Path

file_path = Path(__file__).parent

filename = file_path / 'dog.txt' #or cat.txt

try:
    with open(filename) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    pass
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['edward','phillips','kelvin','phil','sofia']

for k,v in favorite_languages.items():
    if k in people:
        print("Thank you for the polling.",k.title())
    else:
        print("Please take the poll.",k.title())


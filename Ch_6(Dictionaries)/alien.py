# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])


# new_point = alien_0['points']
# print("New point is",new_point)

# alien_0['x_position'] = 0
# alien_0['y_position'] =25

# print(alien_0)
# alien_0['color']='green'
# print(alien_0['color'])

# del alien_0['x_position']

# print(alien_0)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +
".")

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)

    print("Value: " + value)

for key in sorted(user_0.keys()):
    print(key)

for v in user_0.values():
    print(v)

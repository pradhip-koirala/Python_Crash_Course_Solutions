age = 45

#the best way to implement if /elif / else.
if age <2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age <65:
    print("You are an adult.")
else:
    print("You are elder.")

#OR

if age <2:
    print("You are a baby.")
elif age > 2 and age <4:
    print("You are a toddler.")
elif age > 4 and age < 13:
    print("You are a kid.")
elif age > 13 and age <65:
    print("You are an adult.")
else:
    print("You are elder.")
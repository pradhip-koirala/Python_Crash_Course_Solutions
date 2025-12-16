# def greet_user(name):
#     "display simmple message."
#     print("hello",name)

# greet_user('Michel')



# # positional aruguments
# def describe_pet(animal_type, pet_name):

#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')
# describe_pet('dog','willie')#multiple function call.

# #keyword arguments
# describe_pet(pet_name='mew',animal_type='cat')

# # default values
# def describe_pet( pet_name,animal_type='dog'):

#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(pet_name='willie')
# describe_pet('willie')


# def get_formatted_name(first,last,middle =''):
#     if middle:
#         full_name =first+' '+middle+' '+last
        
#     else:
#         full_name = first+' ' + last

#     return {'first_name':first,'last_name':last}

    
    

# print(get_formatted_name('jimi','hendrix'))


# def build_person(first_name,last_name,age=''):
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['person'] = age
#         return person
    
# musician =build_person('jimi','hendrix',age=27)
# print(musician)

# while True:
#     print("\nPlease tell me your name: ")
#     print("Enter 'q' to quit.")

#     f_name =input("First name: ")
#     if f_name =='q':
#         break
#     if l_name == 'q':
#         break
#     l_name = input('Last name: ')
#     formatted_name = get_formatted_name(f_name,l_name)
#     print("\nHello,",formatted_name)


# def greet_users(names):

#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models =[]

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: "+current_design)
#     completed_models.append(current_design)

# print('\nthe following models have been printed.')
# for completed_model in completed_models:
#     print(completed_model)


# passing an arbitrary  number of arguments
def make_pizza(*toppings):
    print("\nMaking pizza with the following toppings: ")
    for topping in toppings:
        print("_ "+ topping)


make_pizza('peppeoni')
make_pizza('mushrooms','green peppers','extra cheese')


# mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    print("\nMaking a " + str(size)+"-inch pizza with the following toppings:")

    for topping in toppings:
        print("_ "+ topping)


make_pizza(16,'peppeoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


# using arbitrary keyword arguments
def build_profile(first,last, **user_info):
    profile ={}
    profile['first_name']=first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             field = 'physics')

print(user_profile)
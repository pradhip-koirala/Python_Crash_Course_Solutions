def greet_user(name):
    "display simmple message."
    print("hello",name)

greet_user('Michel')



# positional aruguments
def describe_pet(animal_type, pet_name):

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog','willie')#multiple function call.

#keyword arguments
describe_pet(pet_name='mew',animal_type='cat')

# default values
def describe_pet( pet_name,animal_type='dog'):

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
describe_pet('willie')


def get_formatted_name(first,last,middle =''):
    if middle:
        full_name =first+' '+middle+' '+last
        
    else:
        full_name = first+' ' + last

    return {'first_name':first,'last_name':last}

    
    

print(get_formatted_name('jimi','hendrix'))


def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['person'] = age
        return person
    
musician =build_person('jimi','hendrix',age=27)
print(musician)

while True:
    print("\nPlease tell me your name: ")
    print("Enter 'q' to quit.")

    f_name =input("First name: ")
    if f_name =='q':
        break
    if l_name == 'q':
        break
    l_name = input('Last name: ')
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello,",formatted_name)
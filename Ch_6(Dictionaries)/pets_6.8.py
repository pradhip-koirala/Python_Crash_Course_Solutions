# Individual pet dictionaries (named after each pet)
buddy = {
    "animal": "dog",
    "owner": "John"
}

whiskers = {
    "animal": "cat",
    "owner": "Emily"
}

tweety = {
    "animal": "bird",
    "owner": "Michael"
}

snowy = {
    "animal": "rabbit",
    "owner": "Sarah"
}

max = {
    "animal": "hamster",
    "owner": "David"
}

# Store all pet dictionaries in a list called pets
pets = [buddy, whiskers, tweety, snowy, max]


for pet in pets:   
    animal = pet['animal']    
    owner = pet['owner'] 
    print("\nAnimal", animal.title(),"\nOwner",owner)
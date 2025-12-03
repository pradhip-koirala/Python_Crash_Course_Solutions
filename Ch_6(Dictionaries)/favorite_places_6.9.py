favorite_places = {
    "John": ["Paris", "New York", "Tokyo"],
    "Emily": ["London", "Rome"],
    "Michael": ["Sydney","Istanbul"]
}

for key,places in favorite_places.items():
    print("\n"+key.title()+"'s favorite places are")
    for v in places:
        print(v)
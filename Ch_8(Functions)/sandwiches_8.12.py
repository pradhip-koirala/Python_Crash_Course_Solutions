toppings = ['avocado mash','hummus','mustard','jam','turkey','grilled chicken','pickles']


def make_sandwishes(*recepies):
    print("\nMaking sandwiches with the following toppings: ")
    print(recepies)
    for recepie in recepies:
        print(recepie)


make_sandwishes('avocado','jam','grilled chicken')
make_sandwishes('hummus','mustard','turkey')
make_sandwishes(toppings)

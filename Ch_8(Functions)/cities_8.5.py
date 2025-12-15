def descirbe_city(city,country):
    print(city.title(),"is in",country.title()+".")

descirbe_city('yangon','myanmar')
descirbe_city('new delhi','india')
descirbe_city('reykjavik','iceland')

#default country. 
def descirbe_city(city,country='America'):
    print(city.title(),"is in",country.title()+".")


descirbe_city('new york')
descirbe_city('los angeles')
descirbe_city('bangkok','thailand')

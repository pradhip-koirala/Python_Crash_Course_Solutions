# def make_album(name,title,no_of_track =''):
#     album = {'artist name':name,'title': title}
#     return album


# print(make_album('timberlake','rockie'))



def make_album(name,title,no_of_track =''):
    if no_of_track:
        album = {'artist name':name,'title': title,'no_of_track':no_of_track}

    else:
        album = {'artist name':name,'title': title}
        
    return album


print(make_album('timberlake','rockie',39))
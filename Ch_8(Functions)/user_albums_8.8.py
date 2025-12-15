def make_album(name,title,no_of_track =''):
    if no_of_track:
        album = {'artist name':name,'title': title,'no_of_track':no_of_track}

    else:
        album = {'artist name':name,'title': title}
        
    return album

while True:
    print("Please enter artist detail.")
    print("Entr 'q' to quit.\n")
    
    n=input("Enter name: ")
    if n=='q':
        break
    t=input("Enter title: ")
    if t =='q':
        break
    artist = make_album(name=n,title=t)

    print("\nArtist Name: ",artist['artist name'],"\n"+"Title: ",artist['title']+"\n")

print(make_album('timber','90s collection',29))



    


    




#
#
#
#
songs = {"Tinariwen": "sastanaqam",
         "Thievery Corporation" : "All that we percieve",
        "Kiwunaka" : " Cold little heart",
        "Phil Collins" : "Against all odds",
        "Fontaines DC" : "Televised mind"
        }

print(songs)

songs2 = {"radiohead": "daydreaming", "Muse" : "Starlight"}

songs.update(songs2)

print(songs)

## to loop through keys

for x in songs:
    print(x)


## to loop through values
    
for x in songs:
    print(songs[x])

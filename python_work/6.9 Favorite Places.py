# Favorite Places dictionary
favorite_places = { 'Myra': ['california', 'mexico', 'new york'],
'Patricia': ['mexico', 'puerto rico', 'california'],
'Marvin': ['greece', 'puerto rico', 'california'] }

# Looping the dictionary and printing of each person name and favorite place
for person, places in favorite_places.items():
        print(f"{person}'s favorite places are:")
        for place in places:
                print(f"-{place}")
                print()
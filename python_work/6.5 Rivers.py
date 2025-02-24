# Creating dictionaries with 3 major rivers and their respective countries 
rivers = {'nile': 'egypt', 'mississippi': 'united states', 'rio grande': 'mexico'}

# Loop for each rivers sentence "runs through"
for river, country in rivers.items(): 
    print(f"The {river.title()} runs through {country.title()}.")

# Loop for each rivers name
print("\nRivers included in the dictionary:")
for river in rivers.keys():
        print(river.title())
# Loop for each country name
print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())
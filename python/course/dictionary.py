# Functions


def print_separator():
    print()


rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china", "indus": "india"}

# Building a sentence with dictionaries
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# Building the names of whether 'contries', and 'rivers'
print_separator()
print("Printing the names of rivers")

for river_name in rivers.keys():
    print(river_name.title())

print_separator()
print("Printing the country in where the rivers pass through")

for country_name in rivers.values():
    print(country_name.title())

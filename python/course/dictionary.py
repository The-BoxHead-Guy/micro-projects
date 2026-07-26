rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china", "indus": "india"}

# Building a sentence with dictionaries
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")


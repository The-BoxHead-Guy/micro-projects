people = [
    {"first_name": "Bill", "last_name": "Gates", "mantra": "Pivot to profit"},
    {"first_name": "Steve", "last_name": "Jobs"},
    {"first_name": "Tim", "last_name": "Cook"}
]

name = input("Name: ")

# for n in names:
#     if name == n:
#         print("Found")
#         break

# else:
#     print("Not found")

for person in people:
    if person["first_name"] == name:
        last_name = person["last_name"]
        mantra = person["mantra"] if "mantra" in person else None

        if mantra is None:
            print(f"Found {name} {last_name}")
        else:
            print(f"Found {name} {last_name}: {mantra}")

        break
else:
    print("Not found")

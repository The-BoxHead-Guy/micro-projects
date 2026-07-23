age = 18
has_id = True

if age >= 18 and has_id:
    print("You're legal")

# OR

has_discount = True
is_student = False

if is_student or has_discount:
    print("Applies discount")

# Not

avenger = False

if not avenger:
    print("You haven't trained enough to become an Avenger")

# Belonging

number_list = [1, 2, 3, 4, 5]

if 3 in number_list:
    print("It's within the list")


if 8 not in number_list:
    print("Remember to add the last number")

print("End of program")


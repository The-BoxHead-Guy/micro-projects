def print_cat():
    print("cat")


def print_header(type):
    print(f"Printing using '{type}' loop")


def ask_user_for_times():
    try:
        return int(input('How many times should the cat say "Meow"? \n'))
    except ValueError:
        print("Please enter a number")
        return ask_user_for_times()


def loop_using_while(times):
    i = 0
    while i < (times):
        print_cat()
        i += 1


def loop_using_for(times):
    for _ in range((times)):
        print_cat()

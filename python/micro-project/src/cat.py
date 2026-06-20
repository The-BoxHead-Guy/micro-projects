def main():
    # Implementations

    # Ask the user how many times the cat shall be printed
    times = ask_user_for_times()

    print_header("while")
    loop_using_while(times)

    print_header("for")
    loop_using_for(times)

# Functions
def print_cat():
    print("cat")


def print_header(type):
    print(f"Printing using '{type}' loop")


def ask_user_for_times():
    return int(input("How many times should the cat say \"Meow\"? \n"))


def loop_using_while(times: int):
    i = 0
    while i < (times):
        print_cat()
        i += 1

def loop_using_for(times):
    for _ in range((times)):
        print_cat()

# Callers
if __name__ == "__main__":
    main()

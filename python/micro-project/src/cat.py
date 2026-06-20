def main():
    # Implementations
    print_header("while")

    i = 0
    while i < 3:
        print_cat()
        i += 1

    print()
    print_header("for")

    for _ in range(3):
        print_cat()

    print()

# Functions
def print_cat():
    print("cat")


def print_header(type):
    print(f"Printing using '{type}' loop")


# Callers
if __name__ == "__main__":
    main()

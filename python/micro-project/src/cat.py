from cat_helpers import print_cat, print_header, ask_user_for_times, loop_using_while, loop_using_for


def main():
    times = ask_user_for_times()

    print_header("while")
    loop_using_while(times)

    print_header("for")
    loop_using_for(times)


if __name__ == "__main__":
    main()

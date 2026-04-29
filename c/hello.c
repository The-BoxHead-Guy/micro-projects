#include <stdio.h>
#include <cs50.h>

string ask_user_name() {
  return get_string("What is your name? ");
}

int print_greeting(char *name) {
  char *greeting = "Hello, ";

  return printf("%s%s!\nHow is your day going?\n", greeting, name);
}

int main() {
  char *name = ask_user_name();
  print_greeting(name);
}

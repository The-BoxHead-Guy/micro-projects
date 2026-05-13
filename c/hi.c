#include <cs50.h>
#include <stdio.h>

int main(void) {
  string s = "HI!";
  string t = "BYE!";

  printf("%s\n", s);
  printf("%s\n", t);

  string words[2];
  words[0] = "TOTALLY!";
  words[1] = "DEFINITELY!";

  printf("%s\n", words[0]);
  printf("%s\n", words[1]);

  // Strings are array of characters essentially
  printf("%c%c%c%c\n", s[0], s[1], s[2], s[3]);
}

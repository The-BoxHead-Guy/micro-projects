#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int main(void) {
  /**
   * When you want to compare single characters, it's used 'char' type
   *  In addition, tolower is used to convert the input to lowercase, this
   * avoids using manual logical operators
   */
  char c = tolower(get_char("Do you agree? (y/n): "));
  char affirmation = 'y';
  char negation = 'n';

  if (c == affirmation) {
    printf("You agreed.\n");
  }

  else if (c == negation) {
    printf("You did not agree.\n");
  }

  else {
    printf("Invalid input.\n");
  }
}

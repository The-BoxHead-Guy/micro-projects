#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void transform_to_uppercase(string s);

int main(void) {
  string s = get_string("Input: ");
  printf("Output: ");

  transform_to_uppercase(s);
  printf("\n");
}

void transform_to_uppercase(string s) {
  for (int i = 0, n = strlen(s); i < n; i++) {
    printf("%c", toupper(s[i]));
  }
}

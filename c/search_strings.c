#include <cs50.h>
#include <stdio.h>
#include <string.h>

void apply_search(string strings[], string s);

int main(void) {
  string strings[] = {"Battleship", "Boot",    "Cannon",
                      "Iron",       "Thimble", "Top hat"};
  string s = get_string("String: ");

  apply_search(strings, s);
}

void apply_search(string strings[], string s) {
  for (int i = 0; i < 6; i++) {
    if (strcmp(strings[i], s) == 0) {
      printf("Found\n");
      return;
    }
  }

  printf("Not found\n");
  return;
}

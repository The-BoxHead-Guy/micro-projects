#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void) {
  string names[] = {"Bryan", "Vladimir", "Matias", "Javier", "Jorge"};
  string numbers[] = {
      "+58-412-1234567", "+58-412-9876543", "+58-412-1234567",
      "+58-412-9876543", "+58-412-1234567",
  };
  string s = get_string("String: ");

  for (int i = 0; i < 5; i++) {
    if (strcmp(names[i], s) == 0) {
      printf("Found %s\n", numbers[i]);
      return 0;
    }
  }
  printf("Not found\n");
  return 1;
}

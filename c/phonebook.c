#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct {
  string name;
  string number;
} person;

int main(void) {
  person people[5] = {
      {"Bryan", "+58-412-1234567"},  {"Vladimir", "+58-412-9876543"},
      {"Matias", "+58-412-1234567"}, {"Javier", "+58-412-9876543"},
      {"Jorge", "+58-412-1234567"},
  };
  string s = get_string("String: ");

  for (int i = 0; i < 5; i++) {
    if (strcmp(people[i].name, s) == 0) {
      printf("Found %s\n", people[i].number);
      return 0;
    }
  }
  printf("Not found\n");
  return 1;
}

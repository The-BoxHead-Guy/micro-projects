#include <cs50.h>
#include <stdio.h>

void apply_search(int numbers[], int n);

int main(void) {
  int numbers[] = {20, 500, 10, 5, 100, 1, 50};
  int n = get_int("Number: ");

  apply_search(numbers, n);
}

void apply_search(int numbers[], int n) {
  for (int i = 0; i < 7; i++) {
    if (numbers[i] == n) {
      printf("Found\n");
      return;
    }
  }

  printf("Not found\n");
  return;
}

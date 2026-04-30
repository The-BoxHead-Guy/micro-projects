#include <stdio.h>

int main() {
  int x = 5;
  int y = 10;

  if (x > 0) {
    printf("x is positive\n");
  } else {
    printf("x is non-positive\n");
  }

  if (x > y) {
    printf("x is greater than y\n");
  } else if (x < y) {
    printf("x is less than y\n");
  } else {
    printf("x is equal to y\n");
  }
}

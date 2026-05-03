#include <cs50.h>
#include <stdio.h>

void build_wall(int n);

int main(void) {
  // We use constants when we require the value to remain the same
  const int n = 3;

  build_wall(n);
}

void build_wall(int n) {
  for (int row = 0; row < n; row++) {
    for (int col = 0; col < n; col++) {
      printf("#");
    }
    printf("\n");
  }
}

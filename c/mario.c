#include <cs50.h>
#include <stdio.h>

void build_wall(int n);
void build_rows(int n, void (*function)(int));
void build_columns(int n);

int main(void) {
  // We use constants when we require the value to remain the same
  const int n = 3;

  build_wall(n);
}

void build_wall(int n) { build_rows(n, build_columns); }

void build_rows(int n, void (*callback)(int)) {
  for (int row = 0; row < n; row++) {
    callback(n);
    printf("\n");
  }
}

// Callback to build 'n' amount of columns
void build_columns(int n) {
  for (int col = 0; col < n; col++) {
    printf("#");
  }
}

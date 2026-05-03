#include <cs50.h>
#include <stdio.h>

// Prototypes
void meow(void);
int get_how_many_times_to_meow(void);
void meow_n_times(int n);

// Implementation
int main(void) {

  // You want to perform the operation once and then ask the questions the
  // system need for the program to continue working

  int n = get_how_many_times_to_meow();
  meow_n_times(n);
}

// Functions
void meow(void) { printf("meow\n"); }

int get_how_many_times_to_meow(void) {
  int n = 0;

  do {
    n = get_int("What's n: ");
  } while (n < 0);

  return n;
}

void meow_n_times(int n) {
  for (int i = 0; i < n; i++) {
    meow();
  }
}

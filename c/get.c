#include <cs50.h>
#include <stdio.h>

int main(void) {
  int n;

  printf("n: ");
  scanf("%d", &n); // We pass the reference of the variable
  printf("n: %i\n", n);
}

#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int *list = malloc(3 * sizeof(int));

  // Check if there was an error
  if (list == NULL) {
    return 1;
  }

  list[0] = 1;
  list[1] = 2;
  list[2] = 3;

  // list =
  //     malloc(4 * sizeof(int)); // Bad solution, it forgets the previous
  //     memory

  // tmp is used in order to avoid mutations, and also to lose track of the old
  // list memory allocated
  int *tmp = realloc(list, 4 * sizeof(int));

  if (tmp == NULL) {
    free(list);
    return 1;
  }

  // Copy old list into new list (Not necessary when you use realloc)
  // for (int i = 0; i < 3; i++) {
  //   tmp[i] = list[i];
  // }

  tmp[3] = 4;

  list = tmp;

  for (int i = 0; i < 4; i++) {
    printf("%d\n", list[i]);
  }

  free(list);
}

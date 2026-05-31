#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void) {
  char DIRECTORY_BASE[] = "../csv/";
  char FILE_NAME[] = "phonebook.csv";

  size_t remainder = sizeof(DIRECTORY_BASE) - strlen(FILE_NAME) - 1;

  FILE *file = fopen(strncat(DIRECTORY_BASE, FILE_NAME, remainder), "a");

  if (file == NULL) {
    return 1;
  }

  char *name = get_string("Name: ");
  char *number = get_string("Number: ");

  fprintf(file, "%s,%s\n", name, number);

  fclose(file);
}

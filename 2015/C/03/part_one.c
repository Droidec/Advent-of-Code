/*
 * Advent of Code 2015 day 03 part one
 */

#include <stdio.h> // fopen, fclose, fgets, fprintf, printf
#include <stdlib.h> // exit

#define INPUT_FILE "../inputs/03-input.txt"
#define BUFFER_SIZE 8192

int main()
{
    unsigned int houses = 1;
    char buffer[BUFFER_SIZE + 1] = {0};
    FILE *file = fopen(INPUT_FILE, "r");

    if (file == NULL)
    {
        fprintf(stderr, "Failed to open file '%s'\n", INPUT_FILE);
        exit(EXIT_FAILURE);
    }

    fgets(buffer, BUFFER_SIZE + 1, file);
    printf("%s\n", buffer);

    fclose(file);
    exit(EXIT_SUCCESS);
}

/*
 * Advent of Code 2015 day 01 part one
 */

#include <stdio.h> // fopen, fclose, fgetc, fprintf, printf
#include <stdlib.h> // exit

#define INPUT_FILE "../inputs/01-input.txt"

int main()
{
    int floor = 0;
    unsigned int index = 0;
    char ch = '\0';
    FILE *file = fopen(INPUT_FILE, "r");

    if (file == NULL)
    {
        fprintf(stderr, "Failed to open file '%s'\n", INPUT_FILE);
        exit(EXIT_FAILURE);
    }

    while ((ch = fgetc(file)) != EOF)
    {
        switch (ch)
        {
            case '(':
                floor++;
                break;

            case ')':
                floor--;
                break;

            default:
                fprintf(stderr, "Invalid character found at position '%u'\n", index + 1);
                fclose(file);
                exit(EXIT_FAILURE);
        }
        index++;
    }

    printf("The right floor is '%d'\n", floor);

    fclose(file);
    exit(EXIT_SUCCESS);
}

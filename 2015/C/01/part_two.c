/******************************************************************************
 * Advent of Code 2015 day 01 part two
 *****************************************************************************/

#include <stdio.h> // fopen, fclose, fgetc, printf, fprintf
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

        if (floor == -1)
        {
            printf("Basement is reached at position '%u'\n", index + 1);
            fclose(file);
            exit(EXIT_SUCCESS);
        }

        index++;
    }

    fprintf(stderr, "The basement was never reached?\n");
    fclose(file);
    exit(EXIT_FAILURE);
}

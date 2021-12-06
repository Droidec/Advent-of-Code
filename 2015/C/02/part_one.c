/*
 * Advent of Code 2015 day 02 part one
 */

#include <stdio.h> // fopen, fclose, fgets, fprintf, printf
#include <stdlib.h> // exit, strtoul
#include <string.h> // strtok

#define INPUT_FILE "../inputs/02-input.txt"
#define BUFFER_SIZE 32
#define NUM_DIM 3
#define SEPARATORS "x\n"

#define MIN(x, y) ((x) < (y) ? (x) : (y))

int main()
{
    unsigned int total = 0;
    unsigned int line = 1;
    char buffer[BUFFER_SIZE + 1] = {0};
    FILE *file = fopen(INPUT_FILE, "r");

    if (file == NULL)
    {
        fprintf(stderr, "Failed to open file '%s'\n", INPUT_FILE);
        exit(EXIT_FAILURE);
    }

    while (fgets(buffer, BUFFER_SIZE + 1, file) != NULL)
    {
        char *endptr;
        unsigned int index = 0;
        unsigned int extra = 0;
        unsigned int dims[NUM_DIM] = {0};
        unsigned int areas[NUM_DIM] = {0};

        char *token = strtok(buffer, SEPARATORS);
        while (token != NULL)
        {
            dims[index] = strtoul(token, &endptr, 10);
            if (dims[index] == 0 && endptr == token)
            {
                fprintf(stderr, "Failed to interpret integral number at line %u\n", line);
                fclose(file);
                exit(EXIT_FAILURE);
            }

            token = strtok(NULL, SEPARATORS);
            index++;
        }

        areas[0] = dims[0] * dims[1];
        areas[1] = dims[0] * dims[2];
        areas[2] = dims[1] * dims[2];
        extra = MIN(areas[0], MIN(areas[1], areas[2]));
        total += 2*areas[0] + 2*areas[1] + 2*areas[2] + extra;
        line++;
    }

    printf("They should order '%u' square feet in total\n", total);

    fclose(file);
    exit(EXIT_SUCCESS);
}

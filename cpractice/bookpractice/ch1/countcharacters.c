#include <stdio.h>

/* This program will count the number of characters in the input */

int main()
{
    long nc;

    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);
}

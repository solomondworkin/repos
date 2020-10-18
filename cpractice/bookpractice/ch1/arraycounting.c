#include <stdio.h>

/* count digits, white space, others */

int main() {

    int c, i, nwhite, nother;
    // declares ndigit to be an array of 10 integers. Array subsripts
    // always start at 0 in C. 
    int ndigit[10];

    nwhite = nother = 0;
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0;

    while ((c=getchar()) != EOF) {
        // determines whether c is a digit
        if (c >= '0' && c <= '9') {
            // conveniently, char variables are identical to int variables
            // in arithmetic expressions
            ++ndigit[c-'0'];
        }
        else if (c == ' ' || c == '\n' || c == '\t') {
            ++nwhite;
        }
        else {
            ++nother;
        }
    }
    printf("digits =");

    for (i=0; i < 10; ++i)
        printf(" %d", ndigit[i]);
    printf(", white space = %d, other = %d\n", nwhite, nother);
}

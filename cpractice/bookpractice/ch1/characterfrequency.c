#include <stdio.h>

#define CHARACTERS 36

int main() {

    int c, i, j;

    int ncharacters[CHARACTERS];
    for (i=0; i < CHARACTERS; ++i) {
        ncharacters[i]=0;
    }

    while ((c=getchar()) != EOF) {
        ncharacters[c] = ncharacters[c] + 1;
    }


    for (i=0; i < CHARACTERS; ++i) {
        putchar(i);
        for (j=0; j < ncharacters[i]; ++j)
            putchar('#');
        putchar('\n');
    }
    return 0;
}

#include <stdio.h>
#include <ctype.h>

#define CHARACTERS 128
#define NOTALNUM 0


int main() {

    FILE  * f = fopen("filename.txt", "r");

    int c, i, j;

    int ncharacters[CHARACTERS];
    for (i=0; i < CHARACTERS; ++i) {
        ncharacters[i]=0;
    }

    while ((c=fgetc(f)) != EOF) {
        if (isalnum(c) != NOTALNUM)
            ncharacters[c] = ncharacters[c] + 1;
    }

    for (i=0; i < 128; ++i) {
        putchar(i);
        for (j=0; j < ncharacters[i]; ++j)
            putchar('#');
        putchar('\n');
    }
    return 0;
}

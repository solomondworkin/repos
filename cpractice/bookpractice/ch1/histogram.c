#include <stdio.h>

#define INWORD 0
#define OUTWORD 1

int main() {

    int c, i, j, state, wordlength;
    int ndigit[50];

    for (i=0; i < 50; ++i) {
        ndigit[i] = 0;
    }

    state = OUTWORD;
    wordlength = 0;
    while ((c=getchar()) != EOF) {
        if (c != ' ' && c != '\t' && c != '\n') {
            ++wordlength;
            state = INWORD;
        }
        if ((c == ' ' || c == '\t' || c == '\n') && state == INWORD) {
            state=OUTWORD;
            ++ndigit[wordlength];
            wordlength=0;
        }
        else if ((c == ' ' || c == '\t' || c == '\n') && state == OUTWORD) {
            state=OUTWORD;
        }
    }
    printf("Histogram: \n");
    for (i = 0; i < 50; ++i) {
        printf("%d: ", i);
        for (j = 0; j < ndigit[i]; ++j)
            putchar('-');
        putchar('\n');
    }
}

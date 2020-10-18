#include <stdio.h>

#define EXTRA 1
#define NOTEXTRA 0

int main () {

    int c, state;

    state = NOTEXTRA;
    while ((c = getchar()) != EOF) {
        if (c== ' ' && state == NOTEXTRA) {
            putchar('\n');
            state = EXTRA;
        }
        if (c== ' ' && state == EXTRA) {
            putchar('\0');
        }
        else {
            putchar(c);
            state = NOTEXTRA;
        }
    }
}

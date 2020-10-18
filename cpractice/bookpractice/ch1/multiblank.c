#include <stdio.h>

#define EXTRA 1
#define NOTEXTRA 0

int main() {

    int c, state;

    state = NOTEXTRA;
    while ((c = getchar()) != EOF) {
        // records first blank, changes state
        if (c == ' ' && state == NOTEXTRA) {
            state = EXTRA;
            putchar(c);
        }
        // records other characters
        else if (state == NOTEXTRA) {
            putchar(c);
        }
        // deletes extra spaces
        else if (c == ' ' && state==EXTRA) {
            putchar('\0');
        }
        // changes state back to normal for other characters
        else if (state == EXTRA) {
            state = NOTEXTRA;
            putchar(c);
        }
    }
}

#include <stdio.h>

int main() {
    /* read a character */
    int c;
    c = getchar();
    while (c != EOF) {
        /* output the character just read */
        putchar(c);
        /* read a character */
        c = getchar(); 
    }
}





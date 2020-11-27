#include <stdlib.h>
#include <stdio.h>

int f() {
    static int x = 0;
    ++x;
    return x;
}

int main(int argc, char ** args) {
    printf("The Result is: %i\n", f() + f()*2);
    return EXIT_SUCCESS;
}

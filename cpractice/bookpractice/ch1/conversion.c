#include <stdio.h>

// Temperature conversion with functions

int convert (int fahr);

int main () {
    int lower, upper, step, fahr;

    lower = 0;
    upper = 300;
    step = 20;
    fahr = lower;

    while (fahr<=upper) {
        printf("%d\t%d\n", fahr, convert(fahr));
        fahr = fahr+step;
    }

}

int convert (int fahr) {
    int celsius;

    celsius = 5 * (fahr-32) / 9;
    return celsius;
}


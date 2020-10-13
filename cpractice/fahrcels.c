#include <stdio.h>

/*print Fahrenheit-Celsius table
    for fahr = 0, 20, ..., 300 */

int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;    /* the lower limit of the temperature table */
    upper = 300;  /* the upper limit of the temperature table */
    step = 20;    /* the step size */

    fahr = lower;
    printf("Fahrenheit Celsius \n");
    while (fahr <= upper) {
        celsius = 5.0 * (fahr-32.0)/9.0;
        printf("%10.0f%8.1f \n", fahr, celsius);
        fahr = fahr + step;
    }
}

#include <stdio.h>

int power (int m, int n);              // says that power is a function and it expects two int arguments, and returns an int.

// test opwer function
int main() {
    int i;

    for (i=0; i<10; ++i)
        printf("%d %d %d \n", i, power(2,i), power(-3,i));    // calling the power function
    return 0;                         // this return statement indicates normal termination, don't use the 0 though for Dries.
}

int power (int base, int n) {         // declares the parameter types and names, and the type of result that the function returns
    int i, p;
    p = 1;
    for (i=1; i<=n; ++i)
        p = p * base;
    return p;
}

#include <stdio.h>

int main()
{
    int n1, c;

    n1 = 0;
    while ((c=getchar()) != EOF) {
        if (c==' ' || c=='\n' || c=='\t')
            ++n1;
    }
    printf("\n%d\n", n1);
}

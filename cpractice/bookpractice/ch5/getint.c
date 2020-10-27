#include <stdio.h>
#include <ctype.h>

int getchar(void);
void ungetch(int);

/*getint: get the next integer from input into *pn */

int getint(int * pn) {
    int c, sign;

    while (isspace(c=getchar()));   // skips white space

    if (!isdigit(c) && c !=EOF && c!= '+' && c!= '-') {
        ungetch(c);
        return 0;
    }
    sign = (c =='-') ? -1 : 1;
    if (c == '+' || c == '-')
        c = getchar();
    for (*pn = 0; isdigit(c); c=getchar())
        *pn = 10 * *pn + (c-'0');
    *pn *= sign;
    if (c != EOF)
        ungetch(c);
    return c;
}

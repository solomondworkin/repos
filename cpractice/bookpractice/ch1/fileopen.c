#include <stdio.h>

int main ()
{
    FILE * f =
      fopen ("filename.txt", "r");
    char c;
    while ((c=fgetc(f)) != EOF)
    {
        putchar(c);
    }
    fclose (f);
}

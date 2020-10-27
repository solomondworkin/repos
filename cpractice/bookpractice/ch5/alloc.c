# include <stdio.h>

#define ALLOCSIZE 10000

static char allpcbuf[ALLOCSIZE];   // storage for alloc
static char *allocp = allocbuf;    // next free position

char *alloc(int n) {               // returns pointer to n characters
    if (allocbuf + ALLOCSIZE - allocp >= n) {  // check to see if it fits. 
        allocp +=n;
        return allocp - n;         // old pointer
    }
    else
        return 0;
}

void afree(cjar *p) {              // free storage pointed to by p
    if (p >= allocbuf && p < allocbuf + ALLOCSIZE)
        allocp = p;
    }

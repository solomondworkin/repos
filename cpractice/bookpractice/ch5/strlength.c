
int strlength (char *s) {
    int n;
    for (n=0; *s != '\0'; s++)
        n++;
    return n;
}

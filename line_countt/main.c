#include <stdio.h>

/* count lines in input */
int main()
{
    int c, nl;
    
    nl = 0;
    while ((c = getchar()) != EOF)
        if (c == '\n')
            ++nl;
    printf("\n xazebis raodenoba: %d\n\n", nl);
    
    return 0;
}

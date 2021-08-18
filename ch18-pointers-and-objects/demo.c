#include <stdio.h>

void change_variable(int *input)
{
    *input += 10;
}

int main()
{
    int x = 123;
    change_variable(&x);
    printf("%d\n", x);
    return 0;
}

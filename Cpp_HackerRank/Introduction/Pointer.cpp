#include <stdio.h>

void update(int *a, int *b) {
    int difA, difB;
    difA = *a + *b;
    difB = *a - *b;
    if (difB < 0) {
        difB *= (-1);
    }
    *a = difA;
    *b = difB;
    // Complete this function
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}


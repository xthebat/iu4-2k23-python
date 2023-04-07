#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

int add(int a, int b) {
    return a + b;
}

void print_point(Point point) {
    printf("(%d, %d)\n", point.x, point.y);
}

#define CONSTANT 123

#ifndef SOME_CONSTANT
#define SOME_CONSTANT "some_value"
#endif

int main() {
    Point p = {1, 2};
    print_point(p);
    printf("add(2, 3) = %d\n", add(2, 3));
    printf("CONSTANT = %d\n", CONSTANT);
    printf("SOME_CONSTANT = %s\n", SOME_CONSTANT);
    return 0;
}

#include <stdio.h>

int factorial(int n);

int main() {
    int num;
    printf("Введите число: ");
    scanf("%d", &num);
    printf("Факториал %d равен %d\n", num, factorial(num));
    return 0;
}

int factorial(int n) {
    int result = 1;
    for(int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

#include <stdio.h>

int count_chars(char str[]);

int main() {
    char str[100];
    printf("Введите строку: ");
    fgets(str, sizeof(str), stdin);
    printf("Количество символов: %d\n", count_chars(str));
    return 0;
}

int count_chars(char str[]) {
    int count = 0;
    for(int i = 0; str[i] != '\0'; i++) {
        count++;
    }
    return count;
}

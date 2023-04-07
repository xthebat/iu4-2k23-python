#include <stdio.h>

float celsius_to_fahrenheit(float celsius);

float temperature;

int main() {
    printf("Введите температуру в градусах Цельсия: ");
    scanf("%f", &temperature);
    printf("%.2f градусов Цельсия = %.2f градусов Фаренгейта\n", temperature, celsius_to_fahrenheit(temperature));
    return 0;
}

float celsius_to_fahrenheit(float celsius) {
    return (celsius * 9 / 5) + 32;
}

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct Point {
    int x;
    int y;
};

struct Circle {
    struct Point center;
    double radius;
};

union Data {
    int i;
    float f;
    char str[20];
};

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    // Initialize variables
    int a = 15, b = 27;
    double pi = 3.14159;
    char buffer[MAX_LEN] = "HelloWorld";
    
    // Bitwise operations
    int xor_result = a ^ b;
    int and_result = a & b;
    int or_result = a | b;
    int shift_left = a << 2;
    int shift_right = b >> 1;
    
    // Mathematical operations
    double power_val = pow(a, 2);
    double sqrt_val = sqrt(b * 2);
    double sin_val = sin(pi / 6); // 30 degrees in radians
    
    // String operations
    int str_len = strlen(buffer);
    strcat(buffer, "CProgramming");
    int new_str_len = strlen(buffer);
    
    // Nested structures
    struct Circle circle1;
    circle1.center.x = xor_result % 10;
    circle1.center.y = and_result % 10;
    circle1.radius = sqrt(pow(circle1.center.x, 2) + pow(circle1.center.y, 2));
    
    // Union usage
    union Data data;
    data.i = factorial(5);
    
    // Complex calculation chain
    int temp1 = (shift_left + shift_right) * or_result;
    double temp2 = power_val / sqrt_val + sin_val * 100;
    int temp3 = new_str_len - str_len + data.i;
    
    // Final computation using all previous results
    int result = (int)(temp1 * temp2 / temp3 + circle1.radius * 10);
    
    // Mask result to fit in 16-bit range
    result = result & 0xFFFF;
    
    printf("Result: %d\n", result);
    return 0;
}
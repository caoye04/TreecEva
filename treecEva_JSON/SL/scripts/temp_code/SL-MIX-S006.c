#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

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

int main() {
    // Initialize variables
    int a = 15, b = 27;
    double pi = 3.141592653589793;
    
    // Bitwise operations
    int xor_val = a ^ b;
    int and_val = a & b;
    int or_val = a | b;
    int shifted = (xor_val << 2) + (and_val >> 1);
    
    // Nested structs
    struct Circle circles[2] = {{{{10, 20}, 5.5}, {{30, 40}, 7.2}}};
    
    // Union usage
    union Data data;
    data.i = shifted;
    
    // Complex mathematical expression
    double expr = pow(circles[0].radius, 2) * pi + sqrt(pow(circles[1].center.x - circles[0].center.x, 2) + 
                                                         pow(circles[1].center.y - circles[0].center.y, 2));
    
    // Conditional logic with multiple operations
    int condition_result = (data.i > 100) ? (int)(expr / 10) : (int)(expr * 2);
    
    // Array manipulation
    int values[] = {xor_val, and_val, or_val, shifted, condition_result};
    int sum = 0;
    for(int i = 0; i < 5; i++) {
        sum += values[i];
    }
    
    // Final calculation using multiple previous results
    int result = ((sum & 0xFF) ^ (int)circles[1].radius) | ((condition_result >> 2) & 0x0F);
    
    printf("Result: %d\n", result);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int main() {
    // Nested struct definition
    struct Point {
        double x;
        double y;
    };
    
    struct Rectangle {
        struct Point topLeft;
        struct Point bottomRight;
    };
    
    // Initialize rectangle
    struct Rectangle rect = {{0.0, 10.0}, {5.0, 0.0}};
    
    // Array of structs
    struct Point points[3] = {{1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0}};
    
    // Complex calculations
    double area = (rect.bottomRight.x - rect.topLeft.x) * (rect.topLeft.y - rect.bottomRight.y);
    
    // Perform operations on array of points
    double sum_x = 0, sum_y = 0;
    for(int i = 0; i < 3; i++) {
        sum_x += points[i].x;
        sum_y += points[i].y;
    }
    
    // Bitwise operations
    int a = 15;  // 1111 in binary
    int b = 9;   // 1001 in binary
    int bitwise_result = (a & b) | ((a ^ b) << 2);
    
    // Trigonometric and logarithmic operations
    double angle = M_PI / 4;  // 45 degrees
    double trig_result = sin(angle) * cos(angle);
    double log_result = log10(area + 1.0);
    
    // String operations
    char str1[20] = "Hello";
    char str2[20] = "World";
    strcat(str1, str2);
    int str_length = strlen(str1);
    
    // Complex expression combining multiple operations
    double complex_expr = (area * trig_result) + (bitwise_result / log_result) - (str_length * (sum_x + sum_y));
    
    // Conditional operations
    double final_result;
    if (complex_expr > 0) {
        final_result = sqrt(complex_expr) + ceil(log_result);
    } else {
        final_result = pow(complex_expr, 2) - floor(log_result);
    }
    
    // Apply modulo operation with a prime number
    final_result = fmod(final_result, 97.0);
    
    // Final adjustment based on bitwise result
    if (bitwise_result % 2 == 0) {
        final_result += 10.5;
    } else {
        final_result -= 5.25;
    }
    
    printf("Result: %.6f\n", final_result);
    return 0;
}
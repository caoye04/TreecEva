#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    char text1[] = "HelloWorld";
    char text2[] = "ComplexCode";
    
    // Mathematical operations with matrix elements
    int sum_diag = matrix[0][0] + matrix[1][1] + matrix[2][2];  // 2 + 11 + 23 = 36
    int product_off_diag = matrix[0][1] * matrix[1][0] * matrix[2][2];  // 3 * 7 * 23 = 483
    
    // Bitwise operations
    int bitwise_result = (sum_diag << 2) ^ (product_off_diag >> 3);  // (36 << 2) ^ (483 >> 3) = 144 ^ 60 = 180
    
    // String manipulations
    int len1 = strlen(text1);
    int len2 = strlen(text2);
    int combined_length = len1 + len2;  // 10 + 11 = 21
    
    // Complex calculation using math functions
    double trig_result = sin(M_PI/6) * cos(M_PI/3);  // 0.5 * 0.5 = 0.25
    int trig_int = (int)(trig_result * 10000);  // 2500
    
    // Multiple variable assignments and transformations
    int a = 10, b = 20, c = 30;
    int temp = a;
    a = b + c;
    b = temp * 2;
    c = a - b;
    
    // Nested conditional logic with compound expressions
    int conditional_result;
    if ((a > b) && (c < (bitwise_result % 100))) {
        conditional_result = (a * b) / c;
    } else if ((b > a) || (combined_length > 30)) {
        conditional_result = (b - a) * combined_length;
    } else {
        conditional_result = a + b + c + bitwise_result;
    }
    
    // Final complex computation
    int final_result = (conditional_result & 0xFF) + (trig_int >> 4) + matrix[1][2];
    
    printf("Result: %d\n", final_result);
    return 0;
}
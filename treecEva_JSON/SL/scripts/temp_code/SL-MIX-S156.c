#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    char text[] = "ComplexComputation";
    double values[] = {3.14159, 2.71828, 1.41421};
    
    // Step 1: Perform mathematical operations
    double sum = 0;
    for (int i = 0; i < 3; i++) {
        sum += values[i] * sin(values[i]);
    }
    
    // Step 2: Bitwise operations
    int a = 0x1F;  // 31 in decimal
    int b = 0x7C;  // 124 in decimal
    int xor_result = a ^ b;
    int shifted = xor_result << 2;
    
    // Step 3: String manipulation
    int text_len = strlen(text);
    int char_sum = 0;
    for (int i = 0; i < text_len; i++) {
        char_sum += text[i];
    }
    
    // Step 4: Matrix operations
    int diagonal_product = 1;
    for (int i = 0; i < 3; i++) {
        diagonal_product *= matrix[i][i];
    }
    
    // Step 5: Complex calculation combining all results
    double intermediate = pow(sum, 2) + sqrt(char_sum);
    int bit_operation = (shifted & 0xFF) | (diagonal_product >> 1);
    
    // Final calculation
    int result = (int)(intermediate) ^ bit_operation;
    
    // Apply modulus to ensure result is in a reasonable range
    result = result % 1000;
    
    printf("Result: %d\n", result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Nested data structures
    int matrix[3][3] = {{2, 3, 1}, {4, 5, 6}, {7, 8, 9}};
    char text[MAX_LEN] = "ComplexEvaluationBenchmark";
    double values[5] = {1.5, 2.7, 3.14, 4.0, 5.5};
    
    // Intermediate variables
    int sum = 0;
    double product = 1.0;
    int bitmask = 0;
    int text_length = strlen(text);
    
    // Step 1: Perform complex arithmetic on matrix
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == j) {  // Diagonal elements
                sum += matrix[i][j] * 2;
            } else if (i < j) {  // Upper triangle
                sum += matrix[i][j] + 3;
            } else {  // Lower triangle
                sum -= matrix[i][j] - 1;
            }
        }
    }
    
    // Step 2: Complex mathematical operations on values array
    for (int i = 0; i < 5; i++) {
        if (i % 2 == 0) {
            product *= sqrt(values[i] * 2.0);
        } else {
            product *= pow(values[i], 1.5);
        }
    }
    
    // Step 3: Bitwise operations with text length
    bitmask = text_length;
    bitmask = bitmask << 2;  // Left shift by 2
    bitmask = bitmask ^ 0xF0;  // XOR with 240
    bitmask = bitmask & 0xFF;  // Mask to 8 bits
    
    // Step 4: Advanced logical evaluations
    int condition_a = (sum > 50) && (product < 1000);
    int condition_b = (bitmask | 0x0F) == 0xFF;
    int condition_c = (text_length % 7 == 0) || (sum % 11 == 0);
    
    // Step 5: Complex mixed operations
    int intermediate_result = 0;
    if (condition_a && condition_b) {
        intermediate_result = sum + (int)product;
    } else if (condition_b || condition_c) {
        intermediate_result = sum * 2 - bitmask;
    } else {
        intermediate_result = sum ^ (int)product;
    }
    
    // Step 6: Final calculation combining all elements
    int final_result = 0;
    
    // Perform a series of operations based on multiple conditions
    switch (intermediate_result % 4) {
        case 0:
            final_result = (intermediate_result >> 2) + bitmask;
            break;
        case 1:
            final_result = intermediate_result * 3 - sum;
            break;
        case 2:
            final_result = (int)(product / 2.0) ^ bitmask;
            break;
        case 3:
            final_result = intermediate_result + (int)floor(sqrt(intermediate_result));
            break;
        default:
            final_result = 0;
    }
    
    // Apply final transformation
    if (final_result < 0) {
        final_result = abs(final_result) + text_length;
    } else if (final_result % 2 == 0) {
        final_result = final_result / 2 + 100;
    } else {
        final_result = final_result * 3 - 50;
    }
    
    printf("Result: %d\n", final_result);
    return 0;
}
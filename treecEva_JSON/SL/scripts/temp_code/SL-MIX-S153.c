#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    // Initialize complex nested data structure
    int matrix[3][4] = {{12, -5, 8, 17}, {3, 0, -9, 4}, {7, 15, -2, 11}};
    char text[] = "ComplexLogicalEvaluation";
    
    // Variables for computation
    int i, j;
    double accumulator = 0.0;
    int bitmask = 0xF0; // 240 in decimal, 11110000 in binary
    int toggle = 1;
    int result = 0;
    
    // First processing loop with conditional operations
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            if (matrix[i][j] > 0) {
                if (toggle) {
                    accumulator += sqrt((double)matrix[i][j]);
                } else {
                    accumulator -= log((double)matrix[i][j] + 1);
                }
                toggle = !toggle;
            }
        }
    }
    
    // Bitwise manipulation and string processing
    int text_length = strlen(text);
    int char_sum = 0;
    for (i = 0; i < text_length; i++) {
        char_sum += (int)text[i];
    }
    
    // Combine accumulator and char_sum using bitwise operations
    int acc_int = (int)(accumulator * 100); // Scale to preserve precision
    result = (acc_int & bitmask) | (char_sum & ~bitmask);
    
    // Mathematical transformation
    result = (int)(pow(result, 0.5) * 10); // Square root scaled by 10
    
    // Final adjustment based on parity
    if (result % 2 == 0) {
        result = result >> 2; // Right shift by 2 (divide by 4)
    } else {
        result = (result << 1) + 1; // Left shift and add 1
    }
    
    // Execution point Y
    result = result ^ 0xAA; // Final XOR operation
    
    printf("Result: %d\n", result);
    return 0;
}
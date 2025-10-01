#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

int main() {
    // Initialize complex nested data structures
    int matrix[MAX_SIZE][MAX_SIZE];
    int vector[MAX_SIZE];
    char text[] = "COMPLEX_REASONING_CHALLENGE";
    
    // Initialize matrix with fibonacci-like values
    for (int i = 0; i < MAX_SIZE; i++) {
        for (int j = 0; j < MAX_SIZE; j++) {
            if (i == 0 || j == 0) {
                matrix[i][j] = 1;
            } else {
                matrix[i][j] = (matrix[i-1][j] + matrix[i][j-1]) % 100;
            }
        }
    }
    
    // Calculate vector values based on matrix diagonal and text length
    int text_len = strlen(text);
    for (int i = 0; i < MAX_SIZE; i++) {
        vector[i] = (matrix[i][i] * text_len) + (int)text[i % strlen(text)];
    }
    
    // Perform complex mathematical operations
    double accumulator = 0.0;
    for (int i = 0; i < MAX_SIZE; i++) {
        accumulator += sqrt(fabs(sin(vector[i] * M_PI / 180.0))) * pow(2.5, i%3);
    }
    
    // Bitwise operations on vector elements
    int bitwise_result = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        if (i % 2 == 0) {
            bitwise_result ^= vector[i];
        } else {
            bitwise_result |= (vector[i] >> 2);
        }
    }
    
    // Complex conditional logic with multiple nested conditions
    int conditional_accum = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        for (int j = 0; j < MAX_SIZE; j++) {
            if ((matrix[i][j] > 50) && (i != j)) {
                if ((vector[i] % 7 == 0) || (vector[j] % 11 == 0)) {
                    conditional_accum += matrix[i][j] & vector[i];
                } else if ((matrix[i][j] + vector[j]) > 100) {
                    conditional_accum += matrix[i][j] | vector[j];
                }
            } else if (matrix[i][j] <= 10) {
                conditional_accum -= matrix[i][j] ^ vector[i];
            }
        }
    }
    
    // Final calculation combining all previous results
    int final_result = (int)(accumulator * 100) + bitwise_result + conditional_accum;
    
    // Apply modulo operation to keep result in reasonable range
    final_result %= 10000;
    
    printf("Result: %d\n", final_result);
    
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

int main() {
    // Initialize complex nested data structures
    int matrix[MAX_SIZE][MAX_SIZE];
    int vector[MAX_SIZE] = {0};
    char text[] = "COMPLEX_REASONING";
    
    // Initialize matrix with calculated values
    for (int i = 0; i < MAX_SIZE; i++) {
        for (int j = 0; j < MAX_SIZE; j++) {
            matrix[i][j] = (i + 1) * (j + 1) + (int)pow(i, 1.5);
        }
    }
    
    // Perform vector operations based on matrix diagonal
    for (int i = 0; i < MAX_SIZE; i++) {
        vector[i] = matrix[i][i] ^ (i << 2);
    }
    
    // Apply trigonometric transformations
    double accumulator = 0.0;
    for (int i = 0; i < MAX_SIZE; i++) {
        accumulator += sin(vector[i] * M_PI / 180.0);
    }
    
    // String manipulation with bitwise operations
    int text_sum = 0;
    for (int i = 0; i < strlen(text); i++) {
        text_sum += (text[i] & 0x1F) | (i << 1);
    }
    
    // Complex calculation combining all previous results
    int intermediate = (int)(accumulator * 1000);
    int mask = 0xFF;
    int shifted = intermediate >> 3;
    int combined = (shifted & mask) ^ text_sum;
    
    // Final complex computation
    int final_result = 0;
    for (int i = 0; i < 5; i++) {
        final_result += (combined >> i) & 1;
    }
    final_result *= (vector[3] % 7);
    final_result += (int)sqrt(matrix[7][2]);
    
    // Apply final transformation
    final_result = (final_result << 2) | ((final_result >> 4) & 0x0F);
    
    printf("Result: %d\n", final_result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_SIZE 10

int complex_operation(int x, int y) {
    return (x * 3 + y * 2) ^ (x & y);
}

int main() {
    int matrix[MAX_SIZE][MAX_SIZE];
    int i, j;
    int *ptr;
    int accumulator = 0;
    
    // Initialize matrix with complex pattern
    for (i = 0; i < MAX_SIZE; i++) {
        for (j = 0; j < MAX_SIZE; j++) {
            matrix[i][j] = (i + 1) * (j + 1) + (i ^ j);
        }
    }
    
    // Perform diagonal operations
    for (i = 0; i < MAX_SIZE; i++) {
        accumulator += matrix[i][i];
    }
    
    // Apply mathematical transformations
    accumulator = (int)(sqrt(accumulator) * 10);
    
    // Bitwise manipulations
    accumulator = (accumulator << 2) | (accumulator >> 3);
    
    // Pointer arithmetic and array traversal
    ptr = &matrix[0][0];
    int sum = 0;
    for (i = 0; i < 25; i++) {
        sum += *(ptr + i * 4);
    }
    
    // Function calls with complex logic
    int temp = complex_operation(accumulator, sum);
    
    // Additional mathematical operations
    double ratio = (double)temp / (double)accumulator;
    int result = (int)(ratio * 1000) % 997;
    
    // FINAL COMPUTATION
    result = (result ^ 0xFF) & ((temp >> 4) | 0x0F);
    
    printf("Result: %d\n", result);
    return 0;
}
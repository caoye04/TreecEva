#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int complex_operation(int x, int y) {
    return (x * 3 + y * 2) ^ (x & y);
}

int main() {
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int vector[3] = {10, 20, 30};
    int i, j;
    int temp = 0;
    int accumulator = 0;
    int mask = 0xF0;
    double pi_approx = 3.14159;
    
    // First processing loop
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if ((i + j) % 2 == 0) {
                matrix[i][j] = matrix[i][j] * 2 + (int)floor(pi_approx);
            } else {
                matrix[i][j] = matrix[i][j] - (int)ceil(pi_approx);
            }
        }
    }
    
    // Second processing with bitwise operations
    for (i = 0; i < 3; i++) {
        temp = (vector[i] << 1) & mask;
        accumulator += temp ^ (matrix[i][i] | 0x0A);
    }
    
    // Complex function calls and mathematical operations
    int intermediate = complex_operation(matrix[1][2], vector[0]);
    int power_result = (int)pow((double)(intermediate % 7), 3.0);
    
    // Final calculation sequence
    int result = accumulator;
    result = (result >> 2) + power_result;
    result = result * (matrix[2][1] & 0x0F) - (vector[2] >> 3);
    
    // CRITICAL_POINT
    printf("Result: %d\n", result);
    return 0;
}
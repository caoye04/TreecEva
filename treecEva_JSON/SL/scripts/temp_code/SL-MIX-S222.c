#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    double matrix[SIZE][SIZE] = {
        {1.5, 2.3, 3.7, 4.1, 5.9},
        {2.2, 3.8, 4.4, 5.6, 6.3},
        {3.1, 4.9, 5.5, 6.7, 7.2},
        {4.8, 5.1, 6.9, 7.4, 8.8},
        {5.5, 6.6, 7.3, 8.1, 9.9}
    };
    
    double vector[SIZE] = {1.1, 2.2, 3.3, 4.4, 5.5};
    double result_vector[SIZE] = {0};
    
    // Matrix-vector multiplication
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            result_vector[i] += matrix[i][j] * vector[j];
        }
    }
    
    // Compute the dot product of result_vector with itself
    double dot_product = 0.0;
    for (int i = 0; i < SIZE; i++) {
        dot_product += result_vector[i] * result_vector[i];
    }
    
    // Apply logarithmic transformation
    double log_result = log(dot_product);
    
    // Perform bitwise operations on an integer derived from log_result
    int int_part = (int)log_result;
    int shifted = int_part << 2;  // Left shift by 2
    int masked = shifted & 0xF0;  // Mask with 0xF0 (240 in decimal)
    
    // Final computation combining all previous results
    double final_result = pow(log_result, 2) + sqrt(masked) + (int_part % 7);
    
    printf("Result: %.6f\n", final_result);
    return 0;
}
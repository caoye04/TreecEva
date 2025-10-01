#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{2, 3, 1}, {4, 5, 6}, {7, 8, 9}};
    char text[MAX_LEN] = "ComplexComputationTask";
    double values[5] = {1.5, 2.7, 3.14, 4.0, 5.5};
    
    // Step 1: Perform mathematical operations on matrix
    int determinant = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                    - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                    + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    
    // Step 2: String manipulation
    int text_len = strlen(text);
    int char_sum = 0;
    for(int i = 0; i < text_len; i++) {
        char_sum += (int)text[i];
    }
    
    // Step 3: Complex mathematical computation with values array
    double product = 1.0;
    for(int i = 0; i < 5; i++) {
        product *= sqrt(values[i] * values[(i+1)%5]);
    }
    
    // Step 4: Bitwise operations
    int bitwise_result = (determinant & 0xF) | (char_sum >> 2);
    
    // Step 5: Advanced computation combining all previous results
    double trig_result = sin(product) + cos(determinant) + tan(bitwise_result);
    
    // Step 6: Conditional logic with multiple branches
    int final_result;
    if(trig_result > 0) {
        final_result = (int)(trig_result * determinant) % 1000;
    } else if(trig_result < 0) {
        final_result = (int)(fabs(trig_result) * char_sum) % 1000;
    } else {
        final_result = determinant ^ char_sum;
    }
    
    // Execution Point Y
    printf("Result: %d\n", final_result);
    return 0;
}
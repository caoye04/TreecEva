#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int main() {
    // Initialize nested data structures
    int matrix[3][3] = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    double vector[3] = {1.5, 2.7, 3.9};
    char text[] = "COMPUTATION";
    
    // Step 1: Compute the determinant of the 3x3 matrix
    int det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
             - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
             + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    
    // Step 2: Compute the sum of squares of the vector elements
    double sum_sq = 0;
    for (int i = 0; i < 3; i++) {
        sum_sq += vector[i] * vector[i];
    }
    
    // Step 3: Manipulate the text string
    int text_len = strlen(text);
    int ascii_sum = 0;
    for (int i = 0; i < text_len; i++) {
        ascii_sum += (int)text[i];
    }
    
    // Step 4: Perform complex bitwise operations
    int bitwise_result = (det & 0xFF) | ((int)sum_sq ^ ascii_sum);
    
    // Step 5: Apply trigonometric and logarithmic functions
    double trig_result = sin(det * 0.01) + cos(sum_sq * 0.1);
    double log_result = log(ascii_sum + 1);
    
    // Step 6: Combine all results in a complex expression
    double intermediate = pow(trig_result, 3) * sqrt(log_result) + bitwise_result;
    
    // Step 7: Final computation with multiple operations
    int final_result = (int)(intermediate * 1000) % 10000;
    
    // Adjust based on conditions
    if (final_result < 0) {
        final_result = abs(final_result);
    }
    
    if (final_result > 5000) {
        final_result = final_result >> 2;
    } else {
        final_result = final_result << 1;
    }
    
    printf("Result: %d\n", final_result);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    double vector[3] = {1.5, 2.5, 3.5};
    char text[MAX_LEN] = "ComplexComputationChallenge";
    
    // Step 1: Perform matrix-vector multiplication and store result in temp_vector
    double temp_vector[3] = {0};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            temp_vector[i] += matrix[i][j] * vector[j];
        }
    }
    
    // Step 2: Calculate the magnitude of temp_vector
    double magnitude = 0;
    for (int i = 0; i < 3; i++) {
        magnitude += temp_vector[i] * temp_vector[i];
    }
    magnitude = sqrt(magnitude);
    
    // Step 3: Perform bitwise operations on text length
    int text_len = strlen(text);
    int bit_operation_result = (text_len << 2) ^ (text_len >> 1);
    
    // Step 4: Complex mathematical expression combining previous results
    double complex_expr = pow(magnitude, 1.5) + log(bit_operation_result) * sin(M_PI / 4);
    
    // Step 5: Conditional logic with multiple branches
    int condition_a = (complex_expr > 100) ? 1 : 0;
    int condition_b = (bit_operation_result % 7 == 0) ? 1 : 0;
    
    // Step 6: Final calculation combining all previous steps
    double target_result;
    if (condition_a && condition_b) {
        target_result = complex_expr / magnitude * bit_operation_result;
    } else if (condition_a || condition_b) {
        target_result = complex_expr + magnitude - bit_operation_result;
    } else {
        target_result = complex_expr * magnitude + bit_operation_result;
    }
    
    // Target point
    printf("Target result: %.0f\n", target_result);
    
    return 0;
}
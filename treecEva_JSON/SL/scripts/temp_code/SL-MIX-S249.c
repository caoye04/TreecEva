#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{2, 3, 1}, {4, 5, 6}, {7, 8, 9}};
    char buffer[MAX_LEN] = "ComplexComputation";
    double values[5] = {1.5, 2.7, 3.14, 4.0, 5.5};
    
    // Intermediate calculations
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum += matrix[i][j] * (i + 1) - (j + 1);
        }
    }
    
    // String manipulation
    int str_len = strlen(buffer);
    int ascii_sum = 0;
    for (int i = 0; i < str_len; i++) {
        ascii_sum += (int)buffer[i];
    }
    
    // Mathematical operations
    double product = 1.0;
    for (int i = 0; i < 5; i++) {
        product *= sqrt(values[i]) + log(values[i] + 1);
    }
    
    // Bitwise operations
    int bitwise_result = (sum & 0xF) | (ascii_sum >> 2) ^ (int)product;
    
    // Complex conditional logic
    int conditional_value = 0;
    if (bitwise_result > 100) {
        conditional_value = bitwise_result / 3;
    } else if (bitwise_result > 50) {
        conditional_value = bitwise_result * 2;
    } else {
        conditional_value = bitwise_result + 100;
    }
    
    // Final computation sequence
    int final_step_1 = (conditional_value << 1) - sum;
    double final_step_2 = sin(final_step_1) * cos(ascii_sum) + tan(product);
    int final_step_3 = (int)(final_step_2 * 1000);
    
    // TARGET ASSIGNMENT
    int target_result = (final_step_3 ^ 0xABC) & (bitwise_result | 0xF0);
    
    printf("Result: %d\n", target_result);
    return 0;
}
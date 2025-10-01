#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize nested data structures
    int matrix[3][3] = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    char text[MAX_LEN] = "ComplexLogicalEvaluation";
    double values[5] = {1.5, 2.7, 3.9, 4.1, 5.6};
    
    // Step 1: Perform complex mathematical operations
    int sum_primes = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum_primes += matrix[i][j];
        }
    }
    
    // Step 2: Apply bitwise operations
    int bitwise_result = (sum_primes >> 2) & 0xF;
    
    // Step 3: String manipulation
    int text_length = strlen(text);
    int char_sum = 0;
    for (int i = 0; i < text_length; i++) {
        char_sum += text[i];
    }
    
    // Step 4: Advanced mathematical calculations
    double product_values = 1.0;
    for (int i = 0; i < 5; i++) {
        product_values *= values[i];
    }
    
    double log_result = log(product_values);
    int int_log = (int)floor(log_result);
    
    // Step 5: Complex logical evaluations
    int condition_a = (bitwise_result > 10) ? 1 : 0;
    int condition_b = (char_sum % 2 == 0) ? 1 : 0;
    int logical_xor = condition_a ^ condition_b;
    
    // Step 6: Final calculation combining all results
    int intermediate = (int_log << 1) + logical_xor;
    int final_result = (intermediate * bitwise_result) % sum_primes;
    
    printf("Result: %d\n", final_result);
    return 0;
}
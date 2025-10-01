#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize nested data structures
    int matrix[3][3] = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    char text[MAX_LEN] = "COMPLEX_LOGIC_2023";
    double values[5] = {M_PI, M_E, 1.414, 1.732, 2.718};
    
    // Step 1: Perform mathematical transformations
    int sum_primes = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum_primes += matrix[i][j];
        }
    }
    
    // Step 2: String manipulation and character analysis
    int char_sum = 0;
    for (int i = 0; i < strlen(text); i++) {
        char_sum += (int)text[i];
    }
    
    // Step 3: Advanced mathematical operations
    double product = 1.0;
    for (int i = 0; i < 5; i++) {
        product *= sqrt(values[i]);
    }
    
    // Step 4: Bitwise operations
    int bitwise_result = (sum_primes & char_sum) | ((int)product ^ 0xFF);
    
    // Step 5: Complex conditional logic
    int conditional_value = 0;
    if ((bitwise_result % 7) == 0) {
        conditional_value = sum_primes * 2;
    } else if ((bitwise_result % 5) == 0) {
        conditional_value = char_sum / 3;
    } else {
        conditional_value = (int)(product * 10);
    }
    
    // Step 6: Final calculation combining all previous results
    int final_result = ((bitwise_result << 2) + conditional_value) % 1000;
    
    // Additional transformation
    final_result = (final_result * 17 + 23) & 0x1FF;
    
    printf("Result: %d\n", final_result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize nested data structures
    int matrix[3][3] = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    char text[] = "COMPLEX_LOGIC";
    double values[5] = {1.5, 2.7, 3.14, 4.67, 5.99};
    
    // Variable declarations
    int i, j, temp_sum = 0;
    double product = 1.0;
    int bit_mask = 0xF0;
    int shifted_value;
    int result = 0;
    
    // Step 1: Perform matrix diagonal sum
    for (i = 0; i < 3; i++) {
        temp_sum += matrix[i][i];
    }
    
    // Step 2: Calculate product of values array
    for (i = 0; i < 5; i++) {
        product *= values[i];
    }
    
    // Step 3: Bitwise operations
    shifted_value = (temp_sum << 2) & bit_mask;
    
    // Step 4: String manipulation
    int text_length = strlen(text);
    int ascii_sum = 0;
    for (i = 0; i < text_length; i++) {
        ascii_sum += (int)text[i];
    }
    
    // Step 5: Complex mathematical operations
    double trig_result = sin(product) + cos(ascii_sum) + tan(temp_sum);
    int trig_int = (int)(trig_result * 1000); // Scale and convert to int
    
    // Step 6: Combine all results with logical operations
    int condition_a = (trig_int > 0) && (shifted_value != 0);
    int condition_b = (temp_sum % 2 == 0) || (ascii_sum < 1000);
    
    // Final calculation
    if (condition_a && condition_b) {
        result = (shifted_value ^ trig_int) + (temp_sum * ascii_sum);
    } else {
        result = (shifted_value | trig_int) - (int)product;
    }
    
    // Apply modulus to keep result in reasonable range
    result = result % 10000;
    
    printf("Result: %d\n", result);
    return 0;
}
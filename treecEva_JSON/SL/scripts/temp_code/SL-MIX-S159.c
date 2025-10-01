#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{2, -1, 3}, {0, 5, -2}, {7, 1, 4}};
    char text[] = "COMPUTATION";
    double values[] = {2.5, -1.3, 0.7, 3.14, -2.8};
    
    // Step 1: Perform matrix diagonal sum with conditional operations
    int diagonal_sum = 0;
    for(int i = 0; i < 3; i++) {
        if(matrix[i][i] > 0) {
            diagonal_sum += matrix[i][i] << 1;  // Left shift by 1 (multiply by 2)
        } else {
            diagonal_sum += ~matrix[i][i] + 1;  // Two's complement negation
        }
    }
    
    // Step 2: Process string with ASCII transformations
    int ascii_sum = 0;
    for(int i = 0; i < strlen(text); i++) {
        if(i % 2 == 0) {
            ascii_sum += (text[i] & 0xFF) ^ 0x55;  // XOR with 0x55
        } else {
            ascii_sum += (text[i] | 0xAA) & 0xFF;  // OR with 0xAA then mask
        }
    }
    
    // Step 3: Complex floating-point operations
    double float_calc = 0.0;
    for(int i = 0; i < 5; i++) {
        if(values[i] > 0) {
            float_calc += pow(values[i], 2.0) * sin(values[i]);
        } else {
            float_calc -= sqrt(fabs(values[i])) * cos(values[i]);
        }
    }
    
    // Step 4: Bitwise manipulations with conditional logic
    int bit_operations = 0;
    for(int i = 0; i < 8; i++) {
        int mask = 1 << i;
        if((diagonal_sum & mask) && (ascii_sum & mask)) {
            bit_operations |= mask;
        } else if(!(diagonal_sum & mask) && (ascii_sum & mask)) {
            bit_operations ^= mask;
        }
    }
    
    // Step 5: Final complex calculation combining all components
    long final_result = 0;
    
    // Apply modular arithmetic with large primes
    final_result = (long)(diagonal_sum * 17 + ascii_sum * 19) % 1000000007;
    
    // Mix in floating point component
    final_result = (final_result * (long)fabs(float_calc)) % 1000000007;
    
    // Apply bitwise transformation
    final_result = (final_result ^ bit_operations) & 0x7FFFFFFF;
    
    // Final adjustment
    final_result = (final_result * 23 + 42) % 1000000007;
    
    printf("Result: %ld\n", final_result);
    return 0;
}
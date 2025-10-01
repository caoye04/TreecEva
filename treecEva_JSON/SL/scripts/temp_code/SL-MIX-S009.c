#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

int main() {
    // Initialize complex nested data structures
    int matrix[MAX_SIZE][MAX_SIZE];
    int vector[MAX_SIZE];
    char text[] = "COMPLEX_REASONING";
    
    // Initialize matrix with fibonacci-like values
    for(int i = 0; i < MAX_SIZE; i++) {
        for(int j = 0; j < MAX_SIZE; j++) {
            if(i == 0 || j == 0) {
                matrix[i][j] = 1;
            } else {
                matrix[i][j] = (matrix[i-1][j] + matrix[i][j-1]) % 100;
            }
        }
    }
    
    // Initialize vector with prime-like values
    int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    for(int i = 0; i < MAX_SIZE; i++) {
        vector[i] = primes[i] * (i+1);
    }
    
    // Perform complex calculations
    long long accumulator = 0;
    int xor_accum = 0;
    double trig_sum = 0.0;
    
    for(int i = 0; i < MAX_SIZE; i++) {
        // Mathematical operations
        long long term1 = (long long)matrix[i][i] * vector[i];
        double term2 = sin((double)i) * cos((double)(MAX_SIZE-i));
        
        // Bitwise operations
        int bitwise_op = (matrix[i][MAX_SIZE-1-i] << 2) ^ (vector[i] >> 1);
        
        // Accumulate results
        accumulator += term1;
        xor_accum ^= bitwise_op;
        trig_sum += term2;
    }
    
    // String manipulation and additional calculations
    int text_length = strlen(text);
    int char_sum = 0;
    for(int i = 0; i < text_length; i++) {
        char_sum += (int)text[i];
    }
    
    // Final complex calculation combining all components
    double intermediate = pow(trig_sum, 3) + sqrt((double)char_sum);
    long long component1 = accumulator & 0xFFFF;
    int component2 = xor_accum | (text_length << 4);
    
    // The critical calculation that produces our target result
    int result = (int)((intermediate * 100) + component1 - component2) % 10000;
    
    // Apply final transformation
    result = (result ^ 0x5555) & 0x7FFF;
    
    printf("Result: %d\n", result);
    return 0;
}
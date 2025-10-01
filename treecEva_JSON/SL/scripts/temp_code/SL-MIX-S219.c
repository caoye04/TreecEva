#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int main() {
    // Initialize complex nested data structures
    int matrix[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    char text[] = "ComplexLogicalEvaluation";
    double values[5] = {3.14159, 2.71828, 1.41421, 1.73205, 0.57721};
    
    // Variable declarations
    int i, j, k;
    int accumulator = 0;
    double product = 1.0;
    int bit_pattern = 0xF0A5;
    int mask = 0x0F0F;
    int shift_count = 3;
    int result = 0;
    
    // Phase 1: Matrix operations with conditional logic
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            if ((i*j) % 2 == 0) {
                accumulator += matrix[i][j] * (int)pow(-1, i+j);
            } else {
                accumulator -= matrix[i][j] / 2;
            }
        }
    }
    
    // Phase 2: Floating point array processing
    for (i = 0; i < 5; i++) {
        product *= sqrt(values[i]);
    }
    
    // Phase 3: String analysis
    int vowel_count = 0;
    for (i = 0; i < strlen(text); i++) {
        char c = text[i];
        if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' ||
            c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowel_count++;
        }
    }
    
    // Phase 4: Bitwise operations
    int xor_result = bit_pattern ^ mask;
    int shifted = (xor_result << shift_count) | (xor_result >> (16 - shift_count));
    
    // Phase 5: Complex conditional evaluation
    if (accumulator > 0 && product > 10.0) {
        result = (accumulator * vowel_count) % (int)product;
    } else if (accumulator <= 0 || product <= 5.0) {
        result = accumulator + (int)product - vowel_count;
    } else {
        result = (accumulator & (int)product) | vowel_count;
    }
    
    // Phase 6: Final adjustment using all computed values
    result = result ^ shifted;
    
    // Apply final mathematical transformation
    result = (int)(result * sin(M_PI/4) + cos(M_PI/3) * 100);
    
    printf("Result: %d\n", result);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize nested data structures
    int matrix[3][3] = {{2, 3, 1}, {4, 5, 6}, {7, 8, 9}};
    char text[] = "COMPUTATION";
    double values[] = {3.14159, 2.71828, 1.41421};
    
    // Variable declarations
    int i, j, temp, sum = 0;
    double product = 1.0;
    int bitmask = 0;
    int result = 0;
    
    // Step 1: Process matrix diagonals
    for (i = 0; i < 3; i++) {
        sum += matrix[i][i];  // Main diagonal
        sum += matrix[i][2-i];  // Anti-diagonal
    }
    
    // Adjust for center element counted twice
    sum -= matrix[1][1];
    
    // Step 2: Calculate product of rounded values
    for (i = 0; i < 3; i++) {
        product *= round(values[i]);
    }
    
    // Step 3: Bitwise operations on text
    for (i = 0; i < strlen(text); i++) {
        // Create bitmask using ASCII values and position
        bitmask |= ((text[i] & 0x0F) << (i % 4));
    }
    
    // Step 4: Complex nested operations
    temp = (int)(sum * product);
    
    // Apply trigonometric transformation
    temp = (int)(temp * sin(M_PI/2) + cos(0));
    
    // Bitwise manipulation with masking
    temp = (temp & 0xFF) | ((bitmask >> 2) & 0xF0);
    
    // Final calculation combining all components
    result = temp ^ (int)floor(sqrt(sum + product + bitmask));
    
    // Conditional adjustment based on parity
    if (result % 2 == 0) {
        result = (result >> 1) + 0x10;
    } else {
        result = (result << 1) - 0x08;
    }
    
    // Apply final modulus to constrain range
    result = result % 1000;
    
    printf("Result: %d\n", result);
    return 0;
}
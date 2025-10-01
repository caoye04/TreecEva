#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    char text[] = "COMPUTATION";
    double values[] = {2.5, 3.7, 1.2, 4.8, 2.1};
    
    // Variable declarations
    int i, j, temp, sum = 0;
    double product = 1.0;
    int bitmask = 0xF0;
    int result = 0;
    
    // Step 1: Process matrix diagonal elements
    for (i = 0; i < 3; i++) {
        matrix[i][i] = matrix[i][i] * 2 + 1;
        sum += matrix[i][i];
    }
    
    // Step 2: Manipulate text string
    for (i = 0; i < strlen(text); i++) {
        if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = text[i] - 'A' + 'a';  // Convert to lowercase
        }
    }
    
    // Step 3: Complex mathematical operations on values array
    for (i = 0; i < 5; i++) {
        values[i] = pow(values[i], 1.5);
        product *= (int)values[i];
    }
    
    // Step 4: Bitwise operations
    temp = (int)product;
    temp = (temp & bitmask) >> 2;
    temp = temp ^ 0xAA;
    
    // Step 5: Final calculation combining all results
    result = sum;
    result = result * temp;
    result = result % 1000;
    
    // Additional transformations
    result = (result << 1) + 0x15;
    result = result & 0x1FF;
    
    printf("Result: %d\n", result);
    return 0;
}
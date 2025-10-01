#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    // Initialize complex data structures
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    char text[] = "COMPUTER";
    double values[] = {2.5, 3.7, 1.2, 4.8, 2.1};
    
    // Variables for computation
    int i, j;
    double sum = 0;
    int product = 1;
    int count = 0;
    
    // Process matrix diagonals
    for(i = 0; i < 3; i++) {
        product *= matrix[i][i];  // Main diagonal
        sum += matrix[i][2-i];    // Anti-diagonal
    }
    
    // Manipulate string data
    for(i = 0; i < strlen(text); i++) {
        if(text[i] == 'A' || text[i] == 'E' || text[i] == 'I' || text[i] == 'O' || text[i] == 'U') {
            count++;
        }
    }
    
    // Perform mathematical operations on array
    double avg = 0;
    for(i = 0; i < 5; i++) {
        avg += sin(values[i]) * cos(values[i]);
    }
    avg /= 5;
    
    // Complex conditional logic
    int temp = (int)(product * avg);
    int condition = (temp > 50) && (count < 3);
    
    // Bitwise operations
    int shifted = (temp << 1) ^ (count >> 1);
    
    // Final calculation
    int result = 0;
    if(condition) {
        result = shifted + (int)sum;
    } else {
        result = shifted - (int)sum;
    }
    
    // Apply modulo to keep result in reasonable range
    result = result % 1000;
    
    printf("Result: %d\n", result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX 10

int main() {
    int matrix[MAX][MAX];
    int i, j;
    int sum = 0;
    int temp;
    int result = 0;
    
    // Initialize matrix with values
    for (i = 0; i < MAX; i++) {
        for (j = 0; j < MAX; j++) {
            matrix[i][j] = (i + 1) * (j + 1);
        }
    }
    
    // Perform complex operations
    for (i = 0; i < MAX; i++) {
        for (j = 0; j < MAX; j++) {
            if ((i & 1) && (j & 1)) {  // Both i and j are odd
                temp = matrix[i][j] << 1;  // Bitwise left shift
                sum += temp;
            } else if (!(i & 1) && !(j & 1)) {  // Both i and j are even
                temp = matrix[i][j] >> 1;  // Bitwise right shift
                sum += temp;
            } else {  // One is odd, the other is even
                temp = (int)sqrt((double)matrix[i][j]);
                sum += temp * temp;
            }
        }
    }
    
    // Final calculation
    result = (sum & 0xFF) ^ ((sum >> 8) & 0xFF);  // XOR of lower and upper bytes
    
    printf("Result: %d\n", result);
    return 0;
}
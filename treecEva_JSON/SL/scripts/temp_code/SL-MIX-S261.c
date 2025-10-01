#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int main() {
    int arr[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    int i, j;
    int sum = 0;
    int product = 1;
    int xor_result = 0;
    double temp = 0.0;
    int result = 0;
    
    // Step 1: Compute sum of primary diagonal
    for (i = 0; i < 4; i++) {
        sum += arr[i][i];
    }
    
    // Step 2: Compute product of secondary diagonal
    for (i = 0; i < 4; i++) {
        product *= arr[i][3 - i];
    }
    
    // Step 3: XOR all elements in the array
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            xor_result ^= arr[i][j];
        }
    }
    
    // Step 4: Perform complex mathematical operation
    temp = pow(sum, 2) + sqrt(product) + log(fabs((double)xor_result));
    
    // Step 5: Bitwise operations
    int shifted = (int)temp << 2;
    int masked = shifted & 0xFF;
    
    // Step 6: Final computation
    result = (sum + product) ^ xor_result;
    result = result & masked;
    result = result | (sum >> 1);
    
    printf("Result: %d\n", result);
    return 0;
}
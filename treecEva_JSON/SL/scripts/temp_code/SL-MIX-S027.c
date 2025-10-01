#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    int arr[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    int *ptr = &arr[0][0];
    int x = 15, y = 7;
    double z = 3.5;
    int result = 0;
    
    // Step 1: Bitwise operations
    int a = (x & y) | ((x ^ y) << 1);
    
    // Step 2: Mathematical operations
    double b = pow(z, 2) + sqrt((double)a);
    
    // Step 3: Array manipulation with pointer arithmetic
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(i*j % 2 == 0) {
                *(ptr + i*4 + j) ^= (int)b;
            }
        }
    }
    
    // Step 4: Complex conditional assignment
    result = (a > b) ? (int)(a - b) : (int)(b - a);
    
    // Step 5: Final calculation using modified array values
    for(int i = 0; i < 4; i++) {
        result += arr[i][i] * (i+1);
    }
    
    printf("Result: %d\n", result);
    return 0;
}
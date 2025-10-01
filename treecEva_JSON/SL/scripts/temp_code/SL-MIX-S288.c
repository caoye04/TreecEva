#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX 10

int main() {
    int arr[MAX] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int i, j;
    int temp;
    double sum = 0;
    int mask = 0xF0;
    int shift_val = 2;
    
    // Step 1: Bitwise operations and array updates
    for (i = 0; i < MAX; i++) {
        arr[i] = (arr[i] & mask) >> shift_val;
    }
    
    // Step 2: Nested loop with mathematical operations
    for (i = 0; i < MAX - 1; i++) {
        for (j = i + 1; j < MAX; j++) {
            temp = arr[i] ^ arr[j];
            sum += sqrt((double)(temp * temp));
        }
    }
    
    // Step 3: Final computation
    int result = (int)(sum / MAX) & 0xFF;
    
    printf("Result: %d\n", result);
    return 0;
}
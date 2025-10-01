#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    int arr[SIZE] = {2, 4, 6, 8, 10};
    int mask = 0xF0;
    int shift = 2;
    double pi = 3.14159;
    int i, j;
    int temp1, temp2;
    int result = 0;
    
    for (i = 0; i < SIZE; i++) {
        temp1 = (arr[i] & mask) >> shift;
        temp2 = (int)(sin(pi/6) * 100 + 0.5); // sin(30°) ≈ 0.5
        
        if ((temp1 | temp2) > 40) {
            j = (i * i) % SIZE;
            result += arr[j] ^ (temp1 & temp2);
        } else {
            result -= (temp1 << 1) | (temp2 >> 2);
        }
        
        // Update mask for next iteration
        mask = mask >> 1;
        if (mask < 0x08) mask = 0xF0;
    }
    
    // Final adjustment
    result = result & 0xFF;
    
    printf("Result: %d\n", result);
    return 0;
}
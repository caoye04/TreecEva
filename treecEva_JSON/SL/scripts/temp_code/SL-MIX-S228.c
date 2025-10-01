#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 3

int main() {
    int cube[SIZE][SIZE][SIZE];
    int i, j, k;
    int base = 5;
    int shift_val = 2;
    int mask = 0xF0;
    int accumulator = 0;
    int target = 0;
    
    // Initialize the 3D array with computed values
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            for (k = 0; k < SIZE; k++) {
                int temp = (i * base) + (j * base * base) + (k * base * base * base);
                cube[i][j][k] = temp ^ (temp << shift_val) & mask;
            }
        }
    }
    
    // Perform complex nested operations
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            int local_sum = 0;
            for (k = 0; k < SIZE; k++) {
                if ((cube[i][j][k] & 0x01) == 0) {
                    local_sum += cube[i][j][k];
                } else {
                    local_sum -= cube[i][j][k] >> 1;
                }
            }
            accumulator += local_sum;
        }
    }
    
    // Final computation
    target = (accumulator & 0xFF) ^ (int)(pow(2, 7) - 1);
    
    printf("Result: %d\n", target);
    return 0;
}
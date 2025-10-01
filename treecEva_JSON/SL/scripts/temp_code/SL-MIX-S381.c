#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 3

int complex_calc(int x, int y) {
    return (x * 2 + y) ^ (x & y);
}

int main() {
    int arr[SIZE][SIZE][SIZE];
    int i, j, k;
    int temp = 0;
    int accumulator = 0;
    
    // Initialize 3D array with complex pattern
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            for (k = 0; k < SIZE; k++) {
                arr[i][j][k] = (i + 1) * (j + 2) * (k + 3) + (i ^ j ^ k);
            }
        }
    }
    
    // Perform nested calculations
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            temp = 0;
            for (k = 0; k < SIZE; k++) {
                temp += arr[i][j][k] * pow(-1, k);
            }
            accumulator += complex_calc(temp, i*j);
        }
    }
    
    // Bitwise manipulations and final calculation
    int mask = (accumulator >> 2) & 0xFF;
    int shift_val = (mask ^ 0xAA) << 1;
    double trig_result = sin(shift_val * M_PI / 180.0);
    int result = (int)(trig_result * 1000) + (accumulator & 0xF);
    
    // TARGET_POINT
    printf("Result: %d\n", result);
    return 0;
}
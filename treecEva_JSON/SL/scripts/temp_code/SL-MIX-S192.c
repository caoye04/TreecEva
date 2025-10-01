#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    int matrix[SIZE][SIZE] = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15},
        {16, 17, 18, 19, 20},
        {21, 22, 23, 24, 25}
    };
    
    int *ptr = &matrix[0][0];
    int i, j;
    long long accumulator = 0;
    double temp;
    int result = 0;
    
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            if ((i + j) % 2 == 0) {
                temp = pow(matrix[i][j], 2);
                accumulator += (long long)temp;
            } else {
                temp = sqrt(matrix[i][j]);
                accumulator -= (long long)temp;
            }
        }
    }
    
    // Bitwise operations on accumulator
    int mask = 0xFF;
    int shifted = (int)(accumulator >> 3);
    result = shifted & mask;
    
    // Final adjustment
    if (result > 128) {
        result = result ^ 0xAA;
    } else {
        result = result | 0x55;
    }
    
    printf("Result: %d\n", result);
    return 0;
}
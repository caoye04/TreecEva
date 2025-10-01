#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 3

int transform(int x) {
    return (x << 2) ^ (x >> 1) & 0xF;
}

int main() {
    int cube[SIZE][SIZE][SIZE] = {{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
                                  {{10, 11, 12}, {13, 14, 15}, {16, 17, 18}},
                                  {{19, 20, 21}, {22, 23, 24}, {25, 26, 27}}};
    
    int i, j, k;
    int accumulator = 0;
    
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            for (k = 0; k < SIZE; k++) {
                int temp = cube[i][j][k];
                if (temp % 2 == 0) {
                    temp = transform(temp);
                } else {
                    temp = (int)pow(temp, 1.5);
                }
                cube[i][j][k] = temp;
                accumulator += temp;
            }
        }
    }
    
    int result = 0;
    for (i = 0; i < SIZE; i++) {
        int slice_sum = 0;
        for (j = 0; j < SIZE; j++) {
            int row_sum = 0;
            for (k = 0; k < SIZE; k++) {
                row_sum += cube[i][j][k];
            }
            slice_sum += row_sum;
        }
        result ^= slice_sum;
    }
    
    result = result & 0xFF;
    printf("Result: %d\n", result);
    return 0;
}
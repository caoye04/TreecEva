#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    int matrix[SIZE][SIZE] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};
    int vector[SIZE] = {2, 3, 1, 4, 0};
    int result = 0;
    int temp = 0;
    int i, j;
    
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            if ((i + j) % 2 == 0) {
                temp = matrix[i][j] ^ vector[(i * j) % SIZE];
                temp = temp << 1;
            } else {
                temp = matrix[i][j] & vector[(i + j) % SIZE];
                temp = temp >> 1;
            }
            result += (int)pow(temp, 0.5);
        }
    }
    
    result = result % 1000;
    
    printf("Result: %d\n", result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX 5

int main() {
    int matrix[MAX][MAX] = {{1, 2, 3, 4, 5}, {2, 4, 6, 8, 10}, {3, 6, 9, 12, 15}, {4, 8, 12, 16, 20}, {5, 10, 15, 20, 25}};
    int vector[MAX] = {1, -1, 1, -1, 1};
    int result = 0;
    int temp = 0;
    int i, j;
    
    for (i = 0; i < MAX; i++) {
        for (j = 0; j < MAX; j++) {
            if ((i & 1) == 0) {
                temp += matrix[i][j] * vector[j];
            } else {
                temp -= matrix[i][j] * vector[j];
            }
        }
        result ^= temp;
        temp = 0;
    }
    
    result = (int)pow(result, 2) % 1000;
    
    printf("Result: %d\n", result);
    
    return 0;
}
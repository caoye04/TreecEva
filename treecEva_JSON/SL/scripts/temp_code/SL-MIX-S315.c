#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int recursive_sum(int *arr, int index) {
    if (index < 0) return 0;
    return arr[index] + recursive_sum(arr, index - 1);
}

int main() {
    int matrix[SIZE][SIZE] = {{1, 2, 3, 4, 5},
                              {6, 7, 8, 9, 10},
                              {11, 12, 13, 14, 15},
                              {16, 17, 18, 19, 20},
                              {21, 22, 23, 24, 25}};
    
    int diag_sum = 0;
    for (int i = 0; i < SIZE; i++) {
        diag_sum += matrix[i][i];
    }
    
    int row_sums[SIZE];
    for (int i = 0; i < SIZE; i++) {
        row_sums[i] = 0;
        for (int j = 0; j < SIZE; j++) {
            row_sums[i] += matrix[i][j];
        }
    }
    
    int max_row_sum = row_sums[0];
    for (int i = 1; i < SIZE; i++) {
        if (row_sums[i] > max_row_sum) {
            max_row_sum = row_sums[i];
        }
    }
    
    int *ptr = &matrix[2][3];
    int shifted_val = (*ptr << 2) ^ 0xF;
    
    double power_result = pow((double)diag_sum, 2.0);
    int truncated_power = (int)power_result;
    
    int recursive_total = recursive_sum(matrix[1], SIZE-1);
    
    int final_result = (truncated_power & 0xFF) | ((max_row_sum ^ recursive_total) >> 1);
    final_result += shifted_val;
    
    printf("Result: %d\n", final_result);
    return 0;
}
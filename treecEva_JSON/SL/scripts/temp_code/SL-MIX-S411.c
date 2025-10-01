#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    int arr[SIZE] = {2, 4, 6, 8, 10};
    int i, j;
    double x = 3.5;
    int mask = 0xF0;
    int shift_val = 2;
    int result = 0;
    
    // Perform nested operations
    for (i = 0; i < SIZE; i++) {
        arr[i] = (arr[i] << shift_val) & mask;
    }
    
    for (j = 0; j < SIZE; j++) {
        x += sqrt((double)arr[j]);
    }
    
    result = (int)(x * 10) ^ 0xAA;
    
    // Execution point Y
    printf("Result: %d\n", result);
    
    return 0;
}
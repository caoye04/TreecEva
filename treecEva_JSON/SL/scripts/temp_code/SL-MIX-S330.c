#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_LEN 10

int main() {
    int arr[MAX_LEN] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    int *ptr = arr;
    int mask = 0xF0;
    int shift_val = 2;
    double accumulator = 0.0;
    int result_value = 0;
    
    for(int i = 0; i < MAX_LEN; i++) {
        int temp = *(ptr + i);
        temp = (temp & 0x0F) << shift_val;
        temp ^= mask;
        accumulator += sqrt((double)temp);
    }
    
    int intermediate = (int)floor(accumulator);
    
    // Nested conditional logic with bitwise operations
    if((intermediate & 0x01) == 0) {
        if((intermediate & 0x02) != 0) {
            intermediate = intermediate >> 1;
        } else {
            intermediate = intermediate << 1;
        }
    } else {
        intermediate = intermediate ^ 0xFF;
    }
    
    // Pointer manipulation and array indexing
    int *p = &intermediate;
    char buffer[5];
    sprintf(buffer, "%d", *p);
    int len = 0;
    while(buffer[len] != '\0') len++;
    
    // FINAL_EVALUATION
    result_value = (len * (*p)) + (buffer[0] - '0');
    
    printf("Result: %d\n", result_value);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    int arr[SIZE] = {2, 4, 6, 8, 10};
    int *ptr = arr;
    double sum_logs = 0.0;
    int product = 1;
    int xor_result = 0;
    int final_result;

    // Step 1: Process array elements using pointer arithmetic
    for(int i=0; i<SIZE; i++) {
        int val = *(ptr + i);
        if(val % 3 == 0) {
            sum_logs += log((double)val);
        }
        if(val % 4 == 0) {
            product *= val;
        }
        if(val > 5) {
            xor_result ^= val;
        }
    }

    // Step 2: Perform bit shifting and masking
    int shifted = (product >> 2) & 0xF;

    // Step 3: Nested conditionals with mathematical operations
    double temp = pow(sum_logs, 2);
    if(temp > 10) {
        if(shifted < 10) {
            final_result = (int)(temp / 2) + shifted;
        } else {
            final_result = (int)(temp / 3) - shifted;
        }
    } else {
        final_result = xor_result * 2;
    }

    // Final adjustment based on bitwise operation
    if((xor_result & 1) == 1) {
        final_result += 5;
    } else {
        final_result -= 3;
    }

    printf("Result: %d\n", final_result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int *ptr_arr[3] = {arr[0], arr[1], arr[2]};
    int x = 5, y = 3, z = 2;
    double pi = 3.14159;
    char str1[MAX_LEN] = "Hello";
    char str2[MAX_LEN] = "World";
    
    // Perform complex calculations
    int step1 = (x << 2) + (y >> 1);  // Bitwise operations
    int step2 = (int)(pi * 100) % 256;  // Mathematical operations
    int step3 = ptr_arr[1][2] * z;  // Array access and multiplication
    
    // String manipulation
    strcat(str1, str2);
    int str_len = strlen(str1);
    
    // More complex arithmetic
    int step4 = step1 ^ step2;  // XOR operation
    int step5 = (step3 & 0xF0) | (str_len << 1);  // Bitwise AND/OR with shift
    
    // Nested conditions and calculations
    int condition_result;
    if ((step4 > 20) && (step5 < 100)) {
        condition_result = step4 + step5;
    } else if ((step4 < 10) || (step5 > 150)) {
        condition_result = step4 * step5;
    } else {
        condition_result = step4 - step5;
    }
    
    // Final complex computation
    double temp = pow(condition_result, 1.0/3.0);  // Cube root
    int final_step = (int)(temp * 10);
    
    // Multi-dimensional array manipulation
    int md_arr[2][2][2] = {{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}};
    int idx1 = (final_step / 10) % 2;
    int idx2 = (final_step / 5) % 2;
    int idx3 = final_step % 2;
    
    // Final result computation
    int final_result = md_arr[idx1][idx2][idx3] + final_step;
    
    printf("Result: %d\n", final_result);
    return 0;
}
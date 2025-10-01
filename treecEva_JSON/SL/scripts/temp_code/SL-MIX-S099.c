#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_LEN 10

int main() {
    int arr[MAX_LEN] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    int *ptr = arr;
    int i = 0, j = MAX_LEN - 1;
    int temp;
    double angle = M_PI / 4.0;
    
    // Reverse the array using pointer arithmetic
    while (i < j) {
        temp = *(ptr + i);
        *(ptr + i) = *(ptr + j);
        *(ptr + j) = temp;
        i++;
        j--;
    }
    
    // Perform bitwise operations on even indices
    for (i = 0; i < MAX_LEN; i += 2) {
        arr[i] = arr[i] ^ (int)(sin(angle) * 10);
    }
    
    // Calculate a cumulative XOR of all elements
    int result = 0;
    for (i = 0; i < MAX_LEN; i++) {
        result ^= arr[i];
    }
    
    // Apply a final transformation using bit shifting
    result = (result << 2) | (result >> 1);
    
    printf("Result: %d\n", result);
    return 0;
}
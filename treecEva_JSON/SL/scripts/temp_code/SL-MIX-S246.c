#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

int compute(int *arr, int size, int depth) {
    if (depth <= 0 || size <= 0) {
        return 0;
    }
    
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    
    int mid = size / 2;
    int left = compute(arr, mid, depth - 1);
    int right = compute(arr + mid, size - mid, depth - 1);
    
    int combined = (left ^ right) + sum;
    return (combined << 1) | ((combined >> 2) & 0x03);
}

int main() {
    int data[] = {7, -2, 15, 8, -3, 12, 5, -1};
    int size = sizeof(data) / sizeof(data[0]);
    
    int *ptr = data;
    int shifted_value = (*(ptr + 2) << 1) ^ (*(ptr + 5) >> 1);
    
    double angle = 45.0;
    int trig_result = (int)(100 * (sin(angle * M_PI / 180.0) + cos(angle * M_PI / 180.0)));
    
    int depth = 3;
    int recursive_result = compute(data, size, depth);
    
    int result = (shifted_value & 0xFF) + (trig_result | 0x10) - (recursive_result ^ 0xAA);
    
    printf("Result: %d\n", result);
    return 0;
}
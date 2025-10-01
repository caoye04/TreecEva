#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int sum_array(int arr[], int size) {
    int s = 0;
    for (int i = 0; i < size; i++) {
        s += arr[i];
    }
    return s;
}

int max_of_three(int a, int b, int c) {
    int max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    return max;
}

int main() {
    int nums[SIZE] = {3, 7, 2, 9, 4};
    int *ptr = nums;
    int x = 15, y = 22, z = 8;
    
    // Step 1: Modify array using pointer arithmetic and conditionals
    for (int i = 0; i < SIZE; i++) {
        if (*(ptr + i) % 2 == 0) {
            *(ptr + i) = *(ptr + i) * 2;
        } else {
            *(ptr + i) = *(ptr + i) + 5;
        }
    }
    
    // Step 2: Perform arithmetic and bitwise operations
    int a = (x + y) * 3;
    int b = (z << 2) | 3; // Left shift z by 2, then bitwise OR with 3
    int c = (int)pow(2, 4); // 2^4
    
    // Step 3: Call functions and perform logical evaluations
    int sum_nums = sum_array(nums, SIZE);
    int max_val = max_of_three(a, b, c);
    
    // Step 4: Complex conditional logic
    int intermediate;
    if ((sum_nums > 100) && (max_val < 100)) {
        intermediate = sum_nums & max_val;
    } else if ((sum_nums < 50) || (max_val > 150)) {
        intermediate = sum_nums | max_val;
    } else {
        intermediate = sum_nums ^ max_val;
    }
    
    // Step 5: Final computation involving trigonometric function
    double angle = 1.5708; // Approximately pi/2
    double sin_val = sin(angle);
    int multiplier = (sin_val > 0.9) ? 10 : 5;
    
    // Final step: Compute the result
    int result = (intermediate + multiplier) / 3;
    
    printf("Result: %d\n", result);
    return 0;
}
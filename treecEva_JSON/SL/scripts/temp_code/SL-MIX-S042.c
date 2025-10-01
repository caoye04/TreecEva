#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

int compute_sum(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

void transform_array(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        if (i % 2 == 0) {
            arr[i] = (int)(pow(arr[i], 2));
        } else {
            arr[i] = factorial(arr[i]);
        }
    }
}

int main() {
    int numbers[SIZE] = {2, 3, 4, 5, 6};
    int* ptr = numbers;
    
    // Step 1: Transform array elements based on index parity
    transform_array(ptr, SIZE);
    
    // Step 2: Compute initial sum
    int sum = compute_sum(numbers, SIZE);
    
    // Step 3: Apply conditional logic and bit operations
    int mask = 0xF0;  // Binary: 11110000
    int shifted_sum = (sum << 2) & mask;
    
    // Step 4: Nested conditionals with floating point precision handling
    double sqrt_val = sqrt((double)shifted_sum);
    int rounded_sqrt = (int)(sqrt_val + 0.5);  // Round to nearest integer
    
    // Step 5: Final computation using multiple variables
    int base = 10;
    int exponent = 2;
    int power_result = (int)(pow(base, exponent));
    
    int result = ((rounded_sqrt ^ power_result) + (numbers[0] | numbers[4])) - (factorial(3) / 2);
    
    printf("Result: %d\n", result);
    return 0;
}
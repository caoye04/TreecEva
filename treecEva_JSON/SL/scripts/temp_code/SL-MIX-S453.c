#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_ROWS 4
#define MAX_COLS 4

int modified_fibonacci(int n) {
    if (n <= 1) return n;
    return modified_fibonacci(n - 1) + modified_fibonacci(n - 2) + (n & 1);
}

int main() {
    int matrix[MAX_ROWS][MAX_COLS] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    
    int i, j;
    int sum = 0;
    int xor_result = 0;
    
    // Step 1: Process matrix diagonals and apply bitwise operations
    for (i = 0; i < MAX_ROWS; i++) {
        for (j = 0; j < MAX_COLS; j++) {
            if (i == j) {  // Main diagonal
                sum += matrix[i][j] * (int)pow(2, i);
            } else if (i + j == MAX_ROWS - 1) {  // Anti-diagonal
                xor_result ^= matrix[i][j];
            }
        }
    }
    
    // Step 2: Apply recursive function and additional operations
    int fib_result = modified_fibonacci(6);
    int intermediate = (sum & xor_result) | fib_result;
    
    // Step 3: Manipulate matrix elements based on computed values
    for (i = 0; i < MAX_ROWS; i++) {
        for (j = 0; j < MAX_COLS; j++) {
            if ((i + j) % 2 == 0) {
                matrix[i][j] = (matrix[i][j] ^ intermediate) & 0xFF;
            } else {
                matrix[i][j] = (matrix[i][j] + intermediate) % 256;
            }
        }
    }
    
    // Step 4: Calculate final target value
    int target_value = 0;
    for (i = 0; i < MAX_ROWS; i++) {
        for (j = 0; j < MAX_COLS; j++) {
            target_value += matrix[i][j] * (i + 1) * (j + 1);
        }
    }
    
    // Apply final transformation
    target_value = (target_value >> 2) ^ (target_value & 0xF);
    
    printf("Result: %d\n", target_value);
    return 0;
}
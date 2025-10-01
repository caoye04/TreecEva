#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    int matrix[3][3] = {{2, 4, 8}, {16, 32, 64}, {128, 256, 512}};
    int vector[3] = {1, 2, 3};
    int temp[3] = {0};
    int i, j;
    long long accumulator = 0;
    
    // Step 1: Matrix-vector multiplication with bitwise shifts
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            temp[i] += (matrix[i][j] << (vector[j] - 1));
        }
    }
    
    // Step 2: Apply trigonometric transformation and accumulate
    for (i = 0; i < 3; i++) {
        accumulator += (long long)(temp[i] * sin(M_PI / 2 * (i + 1)));
    }
    
    // Step 3: Bitwise manipulation with masking
    long long mask = 0xF0F0F0F0LL;
    accumulator = (accumulator & mask) ^ ((accumulator >> 4) & mask);
    
    // Step 4: Final arithmetic and logical operations
    int final_result = (int)((accumulator % 987654321) + sqrt(accumulator & 0xFF) * 1000);
    
    printf("Result: %d\n", final_result);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

int main() {
    int base = 5;
    int exp = 3;
    double angle = M_PI / 4;
    int arr[4] = {2, 4, 6, 8};
    int* ptr = arr;
    
    // Step 1: Compute power and trigonometric value
    double power_result = pow(base, exp);
    double sin_value = sin(angle);
    
    // Step 2: Bitwise operations
    int bitwise_and = (*ptr) & (*(ptr + 1));
    int bitwise_or = (*(ptr + 2)) | (*(ptr + 3));
    int bitwise_xor = bitwise_and ^ bitwise_or;
    
    // Step 3: Complex arithmetic with casting
    double intermediate = power_result * sin_value;
    int casted_intermediate = (int)floor(intermediate);
    
    // Step 4: Pointer arithmetic and array manipulation
    int sum = 0;
    for(int i = 0; i < 4; i++) {
        sum += *(ptr + i);
    }
    
    // Step 5: Final computation combining all values
    int result = (casted_intermediate + bitwise_xor) % sum;
    
    // FINAL COMPUTATION
    printf("Result: %d\n", result);
    
    return 0;
}
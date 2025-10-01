#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int compute_power_sum(int base, int exp) {
    return (int)(pow(base, exp) + pow(exp, base));
}

void process_arrays(int* arr1, int* arr2, int size, int* out) {
    for (int i = 0; i < size; i++) {
        if (i % 2 == 0) {
            out[i] = arr1[i] * arr2[size - i - 1];
        } else {
            out[i] = (arr1[i] + arr2[i]) ^ (arr1[i] - arr2[i]);
        }
    }
}

int main() {
    int A[] = {2, 3, 5, 7};
    int B[] = {1, 4, 6, 8};
    int C[4];
    int x = 3;
    int y = 4;
    double z = 2.5;
    
    process_arrays(A, B, 4, C);
    
    int temp = 0;
    for (int i = 0; i < 4; i++) {
        temp += C[i];
    }
    
    int power_val = compute_power_sum(x, y);
    int mask = 0xF0;
    int masked_val = temp & mask;
    
    double sin_val = sin(z);
    int sin_scaled = (int)(sin_val * 100);
    
    int final_result = (power_val | masked_val) + sin_scaled;
    
    printf("Result: %d\n", final_result);
    return 0;
}
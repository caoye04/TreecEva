#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

int complex_operation(int x, int y) {
    return (x * 3 + y * 2) ^ (x & y);
}

int main() {
    int arr[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    int *ptr = &arr[1][2];
    int i = 3, j = 2;
    double f1 = 2.5, f2 = 3.7;
    int a = 12, b = 7, c = 5;
    
    // Perform a series of operations
    a = (int)(f1 * f2) + (a >> 2);
    b = complex_operation(b, c);
    c = (int)sqrt(a + b);
    
    // Pointer arithmetic and array access
    i = *(ptr + 1) - *(ptr - 1);
    j = arr[i%4][j] | (i & 0x0F);
    
    // Bitwise and logical operations
    int mask = 0xF0;
    int temp = ((a ^ b) & mask) >> 2;
    
    // Complex calculation chain
    int result = 0;
    for (int k = 0; k < 3; k++) {
        result += (arr[k][i%4] * k) + ((j >> k) & 0x03);
    }
    
    result = result ^ temp;
    result = result + (c * (i | j));
    
    /* TARGET EVALUATION POINT */
    
    printf("Result: %d\n", result);
    return 0;
}
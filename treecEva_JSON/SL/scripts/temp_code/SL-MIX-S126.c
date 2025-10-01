#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    // Initialize variables
    int x = 7, y = 3;
    double z = 2.5;
    char str1[] = "hello";
    char str2[] = "world";
    
    // Perform arithmetic and logical operations
    int a = (x << 2) + (y & 0x03);
    double b = pow(z, 3) - sqrt(4.0);
    int c = strlen(str1) * strlen(str2);
    
    // Nested conditional logic with short-circuit evaluation
    int d;
    if ((a > 10) && (b < 10.0 || c == 25)) {
        d = a ^ (int)b;
    } else {
        d = ~(a | (int)b);
    }
    
    // Array and pointer manipulations
    int arr[5] = {1, 2, 3, 4, 5};
    int *p = arr;
    int sum = 0;
    for(int i=0; i<5; i++){
        sum += *(p+i) * (d % (i+2));
    }
    
    // Bitwise and mathematical operations combined
    int e = (sum >> 2) & 0xFF;
    double f = log(exp(2.0)) + cos(M_PI);
    
    // Final computation
    int result = ((e * (int)f) + (a & c)) ^ (d | 0xF0);
    
    printf("Result: %d\n", result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int a = 15, b = 27;
    double x = 3.14159, y = 2.71828;
    char str1[MAX_LEN] = "HelloWorld";
    char str2[MAX_LEN] = "ComplexCode";
    
    // Nested struct definition
    struct Inner {
        int val1;
        double val2;
    };
    
    struct Outer {
        struct Inner inner;
        int arr[5];
        char text[20];
    };
    
    // Initialize struct
    struct Outer data = {{a * 2, x * y}, {1, 2, 3, 4, 5}, "Initial"};
    
    // Perform bitwise operations
    int bitwise_result = (a & b) | ((a ^ b) << 2);
    
    // Mathematical operations
    double trig_result = sin(x) * cos(y) + tan(x / 2);
    int log_result = (int)(log10(bitwise_result) * 100);
    
    // String operations
    strcat(str1, str2);
    int str_len = strlen(str1);
    
    // Update struct values
    data.inner.val1 += log_result;
    data.inner.val2 *= trig_result;
    
    // Array manipulation
    for (int i = 0; i < 5; i++) {
        data.arr[i] = data.arr[i] * (i + 1) + (int)trig_result;
    }
    
    // Complex calculation using all previous results
    int final_result = ((data.inner.val1 & 0xFF) * str_len) + (int)data.inner.val2;
    final_result ^= (data.arr[2] << 3);
    final_result += (bitwise_result % 17);
    
    // Final adjustment
    final_result = (final_result >> 2) * ((int)trunc(trig_result) + 1);
    
    printf("Result: %d\n", final_result);
    
    return 0;
}
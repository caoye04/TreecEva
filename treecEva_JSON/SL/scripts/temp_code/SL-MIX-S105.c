#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    // Initialize variables
    int a = 15, b = 7;
    double x = 3.5, y = 2.0;
    char str1[] = "Hello";
    char str2[] = "World";
    
    // Perform arithmetic operations
    int product = a * b;
    double power = pow(x, y);
    int division = product / (int)power;
    
    // Bitwise operations
    int bitwise_and = a & b;
    int bitwise_or = a | b;
    int xor_result = bitwise_and ^ bitwise_or;
    
    // Logical operations with short-circuit
    int logical_result = (a > 10) && (b < 5 || division > 20);
    
    // String operations
    int str_length = strlen(str1) + strlen(str2);
    
    // Complex calculation using all previous results
    double mixed_calc = (double)(division + xor_result) * sqrt(power) + (double)str_length;
    
    // Conditional assignment based on complex expression
    int selector = ((int)mixed_calc % 7) & 3;
    
    // Array initialization and manipulation
    int values[4] = {10, 20, 30, 40};
    int sum_array = 0;
    for(int i=0; i<4; i++) {
        if(i != selector) {
            sum_array += values[i];
        }
    }
    
    // Final complex computation
    int result = (sum_array * logical_result) + ((int)mixed_calc & 0xF) - (bitwise_or >> 1);
    
    printf("Result: %d\n", result);
    return 0;
}
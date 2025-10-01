#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int a = 15, b = 7;
    double x = 3.5, y = 2.0;
    char str1[MAX_LEN] = "Hello";
    char str2[MAX_LEN] = "World";
    
    // Perform arithmetic operations
    int sum = a + b;
    double product = x * y;
    int power = (int)pow((double)a, 2);
    
    // Logical operations
    int logic_result = (sum > 20) && (product < 10);
    
    // String operations
    strcat(str1, str2);
    int str_length = strlen(str1);
    
    // Array operations
    int arr[5] = {1, 2, 3, 4, 5};
    int arr_sum = 0;
    for(int i=0; i<5; i++) {
        arr_sum += arr[i];
    }
    
    // Bitwise operations
    int bitwise_and = a & b;
    int bitwise_or = a | b;
    int bitwise_xor = a ^ b;
    int left_shift = a << 1;
    int right_shift = b >> 1;
    
    // Complex calculation using all previous results
    double temp1 = (double)(power + bitwise_and);
    double temp2 = log(product + 1.0);
    int temp3 = str_length + arr_sum;
    
    // Final complex expression
    int result = (int)((temp1 * temp2) / (double)temp3);
    result = result ^ bitwise_xor;
    result = result + (left_shift - right_shift);
    
    // Conditional modification
    if(logic_result) {
        result = result * 2;
    } else {
        result = result / 2;
    }
    
    // Final adjustment
    result = result % 100;
    
    printf("Result: %d\n", result);
    return 0;
}
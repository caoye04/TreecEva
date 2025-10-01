#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int a = 15, b = 7;
    double x = 3.14159, y = 2.71828;
    char str1[MAX_LEN] = "HelloWorld";
    char str2[MAX_LEN] = "Programming";
    
    // Perform arithmetic operations
    int product = a * b;
    double power = pow(x, 2);
    int mod_result = product % 13;
    
    // Perform bitwise operations
    int bitwise_and = a & b;
    int bitwise_or = a | b;
    int xor_result = bitwise_and ^ bitwise_or;
    
    // Manipulate strings
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    char combined[MAX_LEN*2];
    strcpy(combined, str1);
    strcat(combined, str2);
    int total_len = strlen(combined);
    
    // Complex conditional logic
    int condition1 = (mod_result > 5) ? 1 : 0;
    int condition2 = (len1 + len2 == total_len) ? 1 : 0;
    int logic_result = condition1 && condition2;
    
    // Array operations
    int arr[5] = {2, 4, 6, 8, 10};
    int sum = 0;
    for(int i=0; i<5; i++) {
        if(i % 2 == 0) {
            sum += arr[i] * (int)y;
        } else {
            sum -= arr[i];
        }
    }
    
    // Final calculation
    double intermediate = power * xor_result;
    int final_addition = (int)(intermediate + sum);
    int result = final_addition * logic_result + (total_len - len1 - len2);
    
    printf("Result: %d\n", result);
    return 0;
}
#define M_PI 3.14159265358979323846
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
    
    // Complex arithmetic operations
    int step1 = (a << 2) + (b >> 1);  // Bitwise shifts and addition
    double step2 = pow(x, 2) + sqrt(y);  // Power and square root
    
    // String manipulation
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    char combined[MAX_LEN*2];
    strcpy(combined, str1);
    strcat(combined, str2);
    int combined_len = strlen(combined);
    
    // Conditional logic with multiple branches
    int condition_result;
    if ((step1 > 50) && (len1 > len2)) {
        condition_result = (int)(step2 * 2);
    } else if ((step1 <= 50) || (len1 <= len2)) {
        condition_result = (int)(step2 / 2);
    } else {
        condition_result = step1 + len1;
    }
    
    // Array operations
    int arr[5] = {10, 20, 30, 40, 50};
    int sum = 0;
    for(int i=0; i<5; i++) {
        if(i % 2 == 0) {
            sum += arr[i] * 2;
        } else {
            sum -= arr[i] / 2;
        }
    }
    
    // Nested mathematical operations
    double nested_calc = sin(x) * cos(y) + tan(M_PI/4);
    int nested_int = (int)(nested_calc * 100);
    
    // Final complex calculation combining all previous results
    int result = ((condition_result & 0xFF) ^ (sum | 0x0F)) + nested_int;
    
    printf("Result: %d\n", result);
    return 0;
}
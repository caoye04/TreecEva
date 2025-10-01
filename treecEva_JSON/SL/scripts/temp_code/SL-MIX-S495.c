#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int i, j;
    double sum = 0;
    char str1[] = "hello";
    char str2[] = "world";
    
    // Step 1: Compute sum of square roots of all elements in arr
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            sum += sqrt((double)arr[i][j]);
        }
    }
    
    // Step 2: Perform bitwise operations
    int a = 15;  // binary: 1111
    int b = 9;   // binary: 1001
    int bitwise_result = (a & b) | ((a ^ b) << 2);
    
    // Step 3: String manipulation
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int str_product = len1 * len2;
    
    // Step 4: Complex mathematical expression
    double expr = pow(sum, 1.5) + log(bitwise_result) * sin(M_PI / 4);
    
    // Step 5: Conditional logic with multiple branches
    int condition = (int)(expr / 10);
    int result;
    
    if (condition > 10) {
        result = (int)(expr * 0.5);
    } else if (condition > 5) {
        result = (int)(expr - sum);
    } else {
        result = (int)(expr + str_product);
    }
    
    // Step 6: Final adjustment using modulo and absolute value
    result = abs(result % 1000);
    
    printf("Result: %d\n", result);
    return 0;
}
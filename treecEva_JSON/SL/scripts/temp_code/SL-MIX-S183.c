#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int a = 12, b = 7;
    double x = 3.5, y = 2.0;
    char str1[MAX_LEN] = "HelloWorld";
    char str2[MAX_LEN] = "Programming";
    
    // Step 1: Perform arithmetic and bitwise operations
    int step1 = ((a + b) * 3) & 0xFF;
    
    // Step 2: Perform floating-point operations
    double step2 = pow(x, y) + log10(step1);
    
    // Step 3: String manipulation
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int str_product = len1 * len2;
    
    // Step 4: Complex conditional logic
    int condition_result;
    if ((step1 > 50) && (step2 < 50.0)) {
        condition_result = step1 | str_product;
    } else if ((step1 <= 50) || (step2 >= 50.0)) {
        condition_result = step1 ^ str_product;
    } else {
        condition_result = ~(step1 & str_product);
    }
    
    // Step 5: Array operations
    int arr[5] = {1, 4, 9, 16, 25};
    int arr_sum = 0;
    for (int i = 0; i < 5; i++) {
        arr_sum += (int)sqrt(arr[i]);
    }
    
    // Step 6: Final calculation combining all previous results
    int final_result = (condition_result + arr_sum) % 100;
    
    printf("Result: %d\n", final_result);
    return 0;
}
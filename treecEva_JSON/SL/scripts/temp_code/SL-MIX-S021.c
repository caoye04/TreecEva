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
    
    // Step 1: Perform arithmetic and bitwise operations
    int step1 = (a * b) ^ ((int)(x + y));
    
    // Step 2: Logical operations with short-circuit evaluation
    int step2 = (a > b) && (strlen(str1) > strlen(str2)) ? step1 : (step1 | a);
    
    // Step 3: Mathematical function calls
    double step3 = pow(x, 2) + sqrt(y) - fabs(-step2);
    
    // Step 4: Complex string manipulations
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    char combined[MAX_LEN*2];
    strcpy(combined, str1);
    strcat(combined, str2);
    int combined_len = strlen(combined);
    
    // Step 5: Nested calculations using previous results
    int step5 = ((len1 + len2) * combined_len) % (int)ceil(step3);
    
    // Step 6: Array operations
    int arr[5] = {step1, step2, (int)step3, len1, len2};
    int sum_arr = 0;
    for(int i=0; i<5; i++) {
        sum_arr += arr[i] & 0xFF;  // Bitwise AND with 255
    }
    
    // Step 7: Final complex calculation involving all previous steps
    int final_result = (step5 * sum_arr) / (int)(log(step3) * 10) + (combined_len ^ step2);
    
    printf("Result: %d\n", final_result);
    return 0;
}
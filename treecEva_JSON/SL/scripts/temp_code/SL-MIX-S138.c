#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int arr[5][5] = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
    double matrix[3][3] = {{1.5, 2.7, 3.9}, {4.1, 5.3, 6.5}, {7.7, 8.9, 9.1}};
    char str[MAX_LEN] = "ComplexComputationChallenge";
    
    // Step 1: Perform nested loop operations on integer array
    int sum1 = 0;
    for(int i=0; i<5; i++) {
        for(int j=0; j<5; j++) {
            if((i+j) % 2 == 0) {
                sum1 += arr[i][j];
            }
        }
    }
    
    // Step 2: Process floating-point matrix with mathematical functions
    double product1 = 1.0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            product1 *= sqrt(matrix[i][j]);
        }
    }
    
    // Step 3: Manipulate string and perform bitwise operations
    int str_len = strlen(str);
    int xor_result = 0;
    for(int i=0; i<str_len; i++) {
        xor_result ^= (int)str[i];
    }
    
    // Step 4: Complex conditional logic with multiple variables
    int condition_var = ((sum1 > 100) ? (int)product1 : (int)(product1 * 2)) & xor_result;
    
    // Step 5: Perform advanced arithmetic operations
    long long factorial = 1;
    for(int i=1; i<=7; i++) {
        factorial *= i;
    }
    
    double power_operation = pow((double)condition_var, 3);
    
    // Step 6: Combine results using modular arithmetic
    int intermediate_result = ((int)power_operation + (int)factorial) % 1000;
    
    // Step 7: Final complex computation involving all previous results
    int final_result = ((intermediate_result << 2) ^ (sum1 >> 1)) + (int)(product1 * 10) - xor_result;
    
    printf("Result: %d\n", final_result);
    return 0;
}
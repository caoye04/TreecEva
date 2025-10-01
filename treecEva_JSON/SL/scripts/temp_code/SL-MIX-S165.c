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
    char buffer[MAX_LEN];
    
    // Step 1: Perform arithmetic operations
    int step1 = (a << 2) + (b >> 1);  // Bitwise shifts and addition
    
    // Step 2: Mathematical functions
    double step2 = pow(x, 2) + log(y) * sin(M_PI/4);
    
    // Step 3: Boolean logic with short-circuit evaluation
    int condition = (step1 > 50) && (step2 < 10.0) || (a & b);
    
    // Step 4: String manipulation
    sprintf(buffer, "Value: %d", step1 * (int)floor(step2));
    int str_length = strlen(buffer);
    
    // Step 5: Complex nested operations
    int nested_calc = ((condition ? step1 : step2) + str_length) ^ (a | b);
    
    // Step 6: Array operations
    int arr[5] = {nested_calc % 10, nested_calc / 10, step1 & 0xF, (int)step2 % 7, condition + 1};
    int sum = 0;
    for(int i = 0; i < 5; i++) {
        sum += arr[i] * (i + 1);
    }
    
    // Step 7: Final complex computation
    int final_result = (sum & 0xFF) | ((nested_calc >> 2) & 0x3F);
    
    printf("Result: %d\n", final_result);
    return 0;
}
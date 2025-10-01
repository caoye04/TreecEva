#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int a = 12, b = 5;
    double x = 3.14159, y = 2.71828;
    char str1[MAX_LEN] = "HelloWorld";
    char str2[MAX_LEN] = "Programming";
    
    // Step 1: Perform arithmetic and bitwise operations
    int step1 = (a * b) + ((a & b) << 2);
    
    // Step 2: Use math functions
    double step2 = pow(x, 2) + log(y) + sin(M_PI/2);
    
    // Step 3: String operations
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int step3 = len1 ^ len2;
    
    // Step 4: Complex conditional logic
    int condition = (step1 > 50) ? (step2 > 10 ? 1 : 0) : (step3 > 0 ? -1 : 0);
    
    // Step 5: Array manipulation
    int arr[5] = {step1 % 10, (int)step2 % 10, step3 % 10, condition, a % b};
    int sum = 0;
    for(int i = 0; i < 5; i++) {
        if(i % 2 == 0) {
            sum += arr[i] * 2;
        } else {
            sum -= arr[i];
        }
    }
    
    // Step 6: Nested operations
    int nested = ((sum >> 1) & 0xF) | ((condition << 2) & 0xF0);
    
    // Final calculation
    int final_result = (nested * condition) + (int)(step2 * 100) - (step1 ^ step3);
    
    printf("Result: %d\n", final_result);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int a = 15;
    int b = 7;
    double x = 3.14159;
    double y = 2.71828;
    char str1[MAX_LEN] = "HelloWorld";
    char str2[MAX_LEN] = "Programming";
    
    // Step 1: Perform arithmetic and bitwise operations
    int step1 = (a * b) & (a | b);
    
    // Step 2: Mathematical operations
    double step2 = pow(x, 2) + log(y) - sin(M_PI/4);
    
    // Step 3: String operations
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    
    // Step 4: Complex conditional logic
    int condition = ((step1 > 50) && (len1 > len2)) ? step1 : (len1 + len2);
    
    // Step 5: Array manipulation
    int arr[5] = {step1 % 10, (int)step2 % 10, len1 % 10, len2 % 10, condition % 10};
    int sum = 0;
    for(int i=0; i<5; i++) {
        sum += arr[i] * (i+1);
    }
    
    // Step 6: Bit shifting and masking
    int shifted = (sum << 2) & 0xFF;
    
    // Step 7: Final calculation combining all previous results
    int final_result = (step1 * 3) + (int)(step2 * 10) + (len1 ^ len2) + condition + shifted;
    
    // Adjust based on a special condition
    if(final_result % 2 == 0) {
        final_result = final_result >> 1;
    } else {
        final_result = final_result * 2 + 1;
    }
    
    printf("Result: %d\n", final_result);
    return 0;
}
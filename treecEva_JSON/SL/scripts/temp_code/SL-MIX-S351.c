#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize complex nested data structures
    int matrix[3][3] = {{2, 3, 1}, {4, 5, 6}, {7, 8, 9}};
    char text1[] = "HelloWorld";
    char text2[MAX_LEN];
    
    // Mathematical operations with nested calculations
    double a = 3.5, b = 2.1;
    int x = 12, y = 8;
    
    // Perform a series of arithmetic and logical operations
    int step1 = (int)(pow(a, b) + sqrt(x*y));
    int step2 = (step1 & 0xF) << 2;  // Bitwise AND with 15, then left shift by 2
    
    // String manipulation
    strcpy(text2, text1);
    int str_len = strlen(text2);
    
    // Complex conditional logic
    int condition_result = ((step2 > 20) && (str_len < 15)) ? 1 : 0;
    
    // Matrix manipulation with nested loops
    int matrix_sum = 0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if(i != j) {
                matrix_sum += matrix[i][j] * (i+j);
            }
        }
    }
    
    // Advanced calculation combining all previous results
    double temp_calc = log(step2 + 1) * sin(M_PI/4);
    int intermediate = (int)(temp_calc + matrix_sum);
    
    // Final complex expression
    int final_result = ((intermediate ^ 0xFF) | (condition_result << 4)) % 100;
    
    printf("Result: %d\n", final_result);
    return 0;
}
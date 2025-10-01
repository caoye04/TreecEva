#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int arr[5][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};
    int i, j;
    double x = 2.5, y = 3.7;
    char str1[MAX_LEN] = "HelloWorld";
    char str2[MAX_LEN] = "Programming";
    int bitmask = 0b11001100;
    long long accumulator = 0;
    
    // Step 1: Perform nested loop with conditional operations
    for(i=0; i<5; i++) {
        for(j=0; j<5; j++) {
            if((i+j) % 2 == 0) {
                arr[i][j] = (int)(pow(arr[i][j], 1.5) + 0.5);  // Square root then square
            } else {
                arr[i][j] = arr[i][j] << ((i*j)%3);  // Bit shift based on position
            }
        }
    }
    
    // Step 2: Complex mathematical expression
    double temp = pow(x, y) + log(y) * sin(M_PI/4);
    int transformed = (int)(temp * 100) & 0xFF;
    
    // Step 3: String manipulation
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    char combined[MAX_LEN];
    strcpy(combined, str1);
    strcat(combined, str2);
    int combined_len = strlen(combined);
    
    // Step 4: Bitwise operations
    int masked_value = bitmask ^ 0b10101010;
    masked_value = masked_value >> 2;
    masked_value |= 0xF0;
    
    // Step 5: Accumulate values from array
    for(i=0; i<5; i++) {
        for(j=0; j<5; j++) {
            accumulator += arr[i][j];
        }
    }
    
    // Step 6: Final calculation combining all components
    long long final_result = (accumulator % 1000) * transformed;
    final_result = final_result ^ masked_value;
    final_result = final_result + combined_len * (len1 + len2);
    
    printf("Result: %lld\n", final_result);
    return 0;
}
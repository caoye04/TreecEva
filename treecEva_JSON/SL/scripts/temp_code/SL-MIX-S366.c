#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

int main() {
    // Initialize variables
    int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    double matrix[2][2] = {{2.5, 3.7}, {1.2, 4.8}};
    char str[MAX_LEN] = "HelloWorld";
    int i, j;
    double sum = 0.0;
    int product = 1;
    int final_result;

    // Step 1: Compute the sum of all elements in arr
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            sum += arr[i][j];
        }
    }

    // Step 2: Compute the product of diagonal elements in matrix
    product = (int)(matrix[0][0] * matrix[1][1]);

    // Step 3: Manipulate string
    int len = strlen(str);
    for (i = 0; i < len; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = str[i] + 32; // Convert to lowercase
        }
    }

    // Step 4: Perform a complex mathematical operation
    double temp = pow(sum, 2) + sqrt(product);
    int temp_int = (int)temp;

    // Step 5: Bitwise operations
    int bitwise_result = (temp_int << 2) ^ 0xF0;

    // Step 6: Final computation
    final_result = (bitwise_result & 0xFF) + len;

    printf("Result: %d\n", final_result);
    return 0;
}
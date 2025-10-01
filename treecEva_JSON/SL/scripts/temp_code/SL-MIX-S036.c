#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SIZE 5

int main() {
    int arr[SIZE] = {2, 4, 6, 8, 10};
    int *ptr = arr;
    double matrix[2][2] = {{1.5, 2.5}, {3.5, 4.5}};
    int i, j;
    int sum_indices = 0;
    double product_matrix = 1.0;
    int final_result;

    // Step 1: Compute sum of indices where arr[i] > 5
    for(i = 0; i < SIZE; i++) {
        if(*(ptr + i) > 5) {
            sum_indices += i;
        }
    }

    // Step 2: Compute product of all elements in matrix
    for(i = 0; i < 2; i++) {
        for(j = 0; j < 2; j++) {
            product_matrix *= matrix[i][j];
        }
    }

    // Step 3: Perform complex calculation using sum_indices and product_matrix
    double intermediate = pow(product_matrix, 1.0/4.0);
    int rounded_intermediate = (int)(intermediate + 0.5);

    // Step 4: Conditional logic based on sum_indices and rounded_intermediate
    if(sum_indices > rounded_intermediate) {
        final_result = (sum_indices << 2) ^ rounded_intermediate;
    } else {
        final_result = (rounded_intermediate & sum_indices) | (sum_indices >> 1);
    }

    // Step 5: Final adjustment using trigonometric function
    double angle = (double)final_result;
    int trig_adjustment = (int)(sin(angle * M_PI / 180.0) * 100);
    final_result += trig_adjustment;

    printf("Result: %d\n", final_result);
    return 0;
}
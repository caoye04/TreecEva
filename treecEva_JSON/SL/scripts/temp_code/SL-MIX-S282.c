#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX 10

int recursive_sum(int arr[], int n) {
    if (n <= 0) return 0;
    return arr[n-1] + recursive_sum(arr, n-1);
}

int main() {
    int data[MAX] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    int i, j;
    long long temp = 0;
    double pi_approx = 3.14159;
    char buffer[50];
    
    // Step 1: Bitwise transformation
    for(i = 0; i < MAX; i++) {
        data[i] = (data[i] << 2) ^ (data[i] >> 1);
    }
    
    // Step 2: Apply sine function and accumulate
    for(j = 0; j < MAX; j++) {
        temp += (long long)(sin(data[j] * pi_approx / 180.0) * 1000);
    }
    
    // Step 3: Reverse array elements
    for(i = 0; i < MAX/2; i++) {
        int t = data[i];
        data[i] = data[MAX - 1 - i];
        data[MAX - 1 - i] = t;
    }
    
    // Step 4: Recursive sum of transformed array
    int sum = recursive_sum(data, MAX);
    
    // Step 5: Final calculation
    int result = ((temp & 0xFF) + sum) % 256;
    
    printf("Result: %d\n", result);
    return 0;
}
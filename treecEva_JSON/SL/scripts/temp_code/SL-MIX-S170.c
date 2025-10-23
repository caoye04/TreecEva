#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

int main() {
    volatile int *temperatures;
    int n = 5;
    temperatures = (volatile int *)malloc(n * sizeof(volatile int));
    
    // Initialize temperature readings
    temperatures[0] = 22;
    temperatures[1] = 25;
    temperatures[2] = 24;
    temperatures[3] = 26;
    temperatures[4] = 23;
    
    int target_temp = 24;
    int *adjustments = (int *)malloc(n * sizeof(int));
    int cumulative_adjustment = 0;
    
    // Calculate adjustments using dynamic programming approach
    for (int i = 0; i < n; i++) {
        adjustments[i] = target_temp - temperatures[i];
        if (i > 0) {
            adjustments[i] += adjustments[i-1];
        }
        cumulative_adjustment += adjustments[i];
    }
    
    free((void*)temperatures);
    free(adjustments);
    
    printf("Result: %d\n", cumulative_adjustment);
    return 0;
}
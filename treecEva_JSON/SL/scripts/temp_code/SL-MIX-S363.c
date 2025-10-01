#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 10

int complex_operation(int x, int y) {
    return (x * 3 + y * 2) ^ (x & y);
}

struct DataPoint {
    int values[3];
    char label[8];
};

struct Container {
    struct DataPoint points[2];
    int count;
};

int main() {
    struct Container containers[2];
    
    // Initialize first container
    containers[0].count = 2;
    containers[0].points[0].values[0] = 5;
    containers[0].points[0].values[1] = 12;
    containers[0].points[0].values[2] = 7;
    strcpy(containers[0].points[0].label, "alpha");
    
    containers[0].points[1].values[0] = 3;
    containers[0].points[1].values[1] = 9;
    containers[0].points[1].values[2] = 15;
    strcpy(containers[0].points[1].label, "beta");
    
    // Initialize second container
    containers[1].count = 1;
    containers[1].points[0].values[0] = 8;
    containers[1].points[0].values[1] = 4;
    containers[1].points[0].values[2] = 11;
    strcpy(containers[1].points[0].label, "gamma");
    
    int accumulator = 0;
    int i, j, k;
    
    for (i = 0; i < 2; i++) {
        for (j = 0; j < containers[i].count; j++) {
            for (k = 0; k < 3; k++) {
                if (containers[i].points[j].values[k] % 2 == 0) {
                    accumulator += containers[i].points[j].values[k] * 2;
                } else {
                    accumulator += (int)pow(containers[i].points[j].values[k], 1.5);
                }
            }
        }
    }
    
    // Perform pointer arithmetic and bitwise operations
    int* ptr = &containers[0].points[1].values[2];
    int offset_value = *(ptr - 1) << 1;
    
    // Complex mathematical expression
    double trig_result = sin(accumulator * M_PI / 180.0);
    int trig_int = (int)(trig_result * 1000);
    
    // Conditional logic with function call
    int func_result = complex_operation(accumulator % 10, trig_int % 7);
    
    // Bitwise manipulation chain
    int masked = (func_result & 0xFF) | ((accumulator >> 2) ^ 0x0F);
    int shifted = masked >> (func_result % 4);
    
    // Final calculation combining all previous results
    int result = ((accumulator + offset_value) * shifted) % 1000;
    
    // TARGET_VARIABLE
    result = result ^ (int)sqrt(abs(trig_int));
    
    printf("Result: %d\n", result);
    
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_LEN 10

struct Point {
    int x;
    int y;
};

struct DataContainer {
    struct Point points[MAX_LEN];
    int count;
    double* values;
};

int main() {
    struct DataContainer container;
    container.count = 5;
    
    double vals[] = {2.5, 3.7, 1.2, 4.8, 2.1};
    container.values = vals;
    
    // Initialize points
    for(int i = 0; i < container.count; i++) {
        container.points[i].x = i * 3;
        container.points[i].y = (i + 1) * 2;
    }
    
    // Perform transformations
    int sum_x = 0;
    for(int i = 0; i < container.count; i++) {
        sum_x += container.points[i].x;
    }
    
    double product_vals = 1.0;
    for(int i = 0; i < container.count; i++) {
        product_vals *= container.values[i];
    }
    
    // Bitwise operations
    int bitwise_result = (sum_x & 0xF) | ((int)floor(product_vals) ^ 0xA);
    
    // Pointer arithmetic
    int* ptr = &(container.points[2].x);
    int offset_value = *(ptr + 1); // This will be container.points[2].y
    
    // Mathematical computation
    double power_result = pow((double)bitwise_result, 2.0);
    int mod_result = ((int)power_result) % 7;
    
    // Final computation
    int target_result = (mod_result << 2) + offset_value + (bitwise_result & 0x3);
    
    printf("Result: %d\n", target_result);
    return 0;
}
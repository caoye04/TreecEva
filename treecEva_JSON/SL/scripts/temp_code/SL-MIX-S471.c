#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct DataPoint {
    int values[5];
    double weight;
};

struct ComplexData {
    struct DataPoint points[3];
    char label[20];
    int count;
};

int complex_calculation(int x, int y) {
    return (x * 3 + y * 2) ^ (x & y);
}

double weighted_sum(struct DataPoint* dp) {
    double sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += dp->values[i] * dp->weight;
    }
    return sum;
}

int main() {
    struct ComplexData data;
    strcpy(data.label, "Test Data");
    data.count = 3;
    
    // Initialize data points
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            data.points[i].values[j] = (i + 1) * (j + 1) + (i * j);
        }
        data.points[i].weight = sqrt(i + 2.5);
    }
    
    // Perform complex calculations
    int intermediate[3];
    for (int i = 0; i < 3; i++) {
        intermediate[i] = complex_calculation(data.points[i].values[2], data.points[(i+1)%3].values[3]);
    }
    
    // Apply bitwise transformations
    intermediate[0] = (intermediate[0] << 2) | (intermediate[1] >> 1);
    intermediate[1] = intermediate[1] ^ intermediate[2];
    intermediate[2] = ~(intermediate[0] & intermediate[1]);
    
    // Calculate weighted sums
    double w_sums[3];
    for (int i = 0; i < 3; i++) {
        w_sums[i] = weighted_sum(&data.points[i]);
    }
    
    // Combine results using trigonometric functions
    double trig_result = sin(w_sums[0]) + cos(w_sums[1]) * tan(w_sums[2]);
    
    // Final computation
    int result = (int)(trig_result * 1000);
    result = result ^ intermediate[0];
    result = (result >> 3) + (result << 1);
    
    /* TARGET POINT */
    
    printf("Result: %d\n", result);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_ELEMENTS 10

struct DataPoint {
    int x;
    double y;
};

struct ComplexData {
    struct DataPoint points[MAX_ELEMENTS];
    int count;
    unsigned int flags;
};

int main() {
    struct ComplexData data = {
        .points = {{1, 2.5}, {3, 4.7}, {5, 6.1}, {7, 8.9}, {9, 10.3}},
        .count = 5,
        .flags = 0xF0F0
    };

    double accumulator = 0.0;
    int mask = 0xAA;
    int i, j;
    
    // First processing loop
    for (i = 0; i < data.count; i++) {
        if ((data.flags >> i) & 1) {
            accumulator += pow(data.points[i].x, 2) * sin(data.points[i].y);
        }
    }
    
    // Bitwise manipulation
    data.flags = data.flags ^ (mask << 4);
    
    // Second processing with nested loop
    for (i = 0; i < data.count - 1; i++) {
        for (j = i + 1; j < data.count; j++) {
            if ((data.flags >> (i+j)) & 1) {
                double diff = fabs(data.points[i].y - data.points[j].y);
                accumulator *= (1.0 + diff / 10.0);
            }
        }
    }
    
    // Mathematical transformation
    accumulator = log(accumulator + 1.0);
    
    // Final calculation involving bit shifting and modular arithmetic
    long long temp = (long long)(accumulator * 1000);
    temp = (temp << 3) ^ (temp >> 2);
    int final_result = (int)(temp % 10000);
    
    // Adjust based on parity
    if (final_result % 2 == 0) {
        final_result = (final_result >> 2) + 0x7F;
    } else {
        final_result = (final_result << 1) - 0x100;
    }
    
    printf("Result: %d\n", final_result);
    return 0;
}
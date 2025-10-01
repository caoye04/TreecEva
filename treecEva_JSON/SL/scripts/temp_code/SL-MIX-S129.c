#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int complex_operation(int x, int y) {
    return (x & y) ^ (x | y) >> 2;
}

struct DataPoint {
    int values[3];
    double weight;
};

struct Container {
    struct DataPoint points[2];
    int count;
};

int main() {
    struct Container data = {
        .points = {
            {{12, -5, 7}, 2.5},
            {{-8, 15, 3}, 1.8}
        },
        .count = 2
    };
    
    int indices[4] = {0, 1, 0, 1};
    int offsets[4] = {1, -1, 2, -2};
    
    double accumulator = 0.0;
    int bit_pattern = 0xF0;
    int mask = 0x0F;
    
    for (int i = 0; i < 4; i++) {
        int idx = indices[i];
        int offset = offsets[i];
        
        struct DataPoint* dp = &data.points[idx];
        int value = dp->values[(i + offset) % 3];
        
        if (value > 0) {
            accumulator += sqrt(pow(value, 2)) * dp->weight;
        } else {
            accumulator -= log(fabs(value) + 1) * dp->weight;
        }
        
        bit_pattern = (bit_pattern >> 1) | ((bit_pattern & 1) << 7);
        mask = mask ^ (1 << (i % 4));
    }
    
    int intermediate = (int)(accumulator * 10);
    int result = complex_operation(intermediate, bit_pattern) & mask;
    
    /* TARGET EVALUATION POINT */
    
    // Apply final transformation
    result = result ^ (result >> 4);
    
    printf("Result: %d\n", result);
    return 0;
}
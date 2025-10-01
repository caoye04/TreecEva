#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct DataPoint {
    int x;
    double y;
    char label[16];
};

struct ComplexData {
    struct DataPoint points[3];
    int count;
    unsigned int flags;
};

int process_value(double val, int mod) {
    int ival = (int)floor(val);
    return (ival % mod) ^ (ival >> 2);
}

int main() {
    struct ComplexData data = {
        .points = {
            {12, 3.14159, "alpha"},
            {7, 2.71828, "beta"},
            {23, 1.41421, "gamma"}
        },
        .count = 3,
        .flags = 0b11010010
    };
    
    double accumulator = 0.0;
    int i;
    for (i = 0; i < data.count; i++) {
        accumulator += data.points[i].y * data.points[i].x;
    }
    
    int base = (int)accumulator;
    int mask = 0xF0;
    int shifted = (base << 3) & mask;
    
    double trig_val = sin(accumulator / 100.0);
    int trig_int = (int)(trig_val * 1000);
    
    int xor_result = shifted ^ trig_int;
    
    char buffer[32];
    sprintf(buffer, "%d", xor_result);
    int str_len = strlen(buffer);
    
    int result = process_value(accumulator, str_len) + (data.flags & 0x0F);
    
    // Execution point Y
    printf("Result: %d\n", result);
    
    return 0;
}
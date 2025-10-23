#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

union DataConverter {
    float raw_float;
    unsigned int raw_bits;
};

int main() {
    volatile int sensor_readings[3][4] = {{120, 150, 135, 125}, {140, 130, 138, 142}, {128, 133, 137, 130}};
    int i, j;
    union DataConverter converter;
    float sum = 0.0;
    int calibrated_output = 0;
    
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            if (sensor_readings[i][j] > 130) {
                converter.raw_float = (float)sensor_readings[i][j];
                converter.raw_bits = converter.raw_bits & 0xFFFFFFF0; // Mask lower 4 bits
                sum += converter.raw_float;
            } else {
                converter.raw_float = (float)sensor_readings[i][j];
                converter.raw_bits = converter.raw_bits | 0x0000000F; // Set lower 4 bits
                sum += converter.raw_float;
            }
        }
    }
    
    float mean = sum / 12.0;
    sum = 0.0;
    
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            float diff = (float)sensor_readings[i][j] - mean;
            sum += diff * diff;
        }
    }
    
    float variance = sum / 12.0;
    calibrated_output = (int)(mean + sqrt(variance));
    
    printf("Result: %d\n", calibrated_output);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define SENSOR_COUNT 5

struct SensorReading {
    volatile int x_coord;
    volatile int y_coord;
    volatile int value;
};

int main() {
    struct SensorReading sensors[SENSOR_COUNT] = {
        {10, 20, 150},
        {15, 25, 160},
        {20, 30, 155},
        {25, 35, 165},
        {30, 40, 158}
    };
    
    volatile int values[SENSOR_COUNT];
    volatile int sum = 0;
    volatile int mean = 0;
    volatile int variance = 0;
    volatile int calibration_output = 0;
    volatile int mask = 0xF0;
    
    // Step 1: Extract values and compute sum
    for (int i = 0; i < SENSOR_COUNT; i++) {
        values[i] = sensors[i].value;
        sum += values[i];
    }
    
    // Step 2: Compute mean
    mean = sum / SENSOR_COUNT;
    
    // Step 3: Compute variance
    for (int i = 0; i < SENSOR_COUNT; i++) {
        int diff = values[i] - mean;
        variance += diff * diff;
    }
    variance = variance / SENSOR_COUNT;
    
    // Step 4: Apply geometric calculation based on coordinates
    volatile int geometric_factor = 0;
    for (int i = 0; i < SENSOR_COUNT; i++) {
        // Euclidean distance from origin
        int distance = (int)sqrt(sensors[i].x_coord * sensors[i].x_coord + 
                                sensors[i].y_coord * sensors[i].y_coord);
        geometric_factor += distance;
    }
    
    // Step 5: Apply switch-based logic
    volatile int adjustment = 0;
    switch (geometric_factor % 4) {
        case 0:
            adjustment = variance & mask;
            break;
        case 1:
            adjustment = variance | 0x0F;
            break;
        case 2:
            adjustment = variance ^ 0xAA;
            break;
        default:
            adjustment = variance << 1;
    }
    
    // Step 6: Final calibration output with conditional logic
    if (mean > 155) {
        if (variance > 20) {
            calibration_output = (geometric_factor >> 2) + adjustment;
        } else {
            calibration_output = geometric_factor + (adjustment & 0xFF);
        }
    } else {
        calibration_output = geometric_factor - (adjustment >> 1);
    }
    
    // Step 7: Apply final mask
    calibration_output = calibration_output & 0x1FF;
    
    printf("Result: %d\n", calibration_output);
    return 0;
}
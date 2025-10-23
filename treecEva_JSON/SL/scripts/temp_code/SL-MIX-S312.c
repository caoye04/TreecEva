#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int initial_temp;
    int *readings;
    int count;
} ThermalSensor;

int main() {
    ThermalSensor sensor;
    sensor.initial_temp = 18;
    sensor.count = 4;
    sensor.readings = (int *)malloc(sensor.count * sizeof(int));
    
    // Initialize modified Fibonacci sequence: 1, 1, 1, 2
    sensor.readings[0] = 1;
    sensor.readings[1] = 1;
    sensor.readings[2] = sensor.readings[0] + sensor.readings[1] - 1; // 1
    sensor.readings[3] = sensor.readings[1] + sensor.readings[2] - 1; // 1
    
    int final_temperature = sensor.initial_temp;
    for(int i = 0; i < 3; i++) {
        final_temperature += sensor.readings[i];
    }
    
    free(sensor.readings);
    printf("Result: %d\n", final_temperature);
    return 0;
}
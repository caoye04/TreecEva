#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int count;
    double readings[]; 
} SensorData;

int main() {
    int n = 6;
    SensorData *sensor = malloc(sizeof(SensorData) + n * sizeof(double));
    sensor->count = n;
    
    double initial_values[] = {10.0, 20.0, 30.0, 40.0, 50.0, 60.0};
    for(int i = 0; i < n; i++) {
        sensor->readings[i] = initial_values[i];
    }
    
    double *ptr = sensor->readings;
    for(int i = 0; i < n/2; i++) {
        *(ptr + i) *= 2;
    }
    
    double sum = 0;
    for(int i = 0; i < n; i++) {
        sum += sensor->readings[i];
    }
    
    double processed_average = sum / n;
    printf("Result: %.1f\n", processed_average);
    free(sensor);
    return 0;
}
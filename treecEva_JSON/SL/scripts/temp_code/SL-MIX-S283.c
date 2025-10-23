#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define CALIBRATION_FACTOR 1.05
#define SENSOR_COUNT 5

union converter {
    float f_val;
    int i_val;
};

struct temp_data {
    float raw_values[SENSOR_COUNT];
    float calibrated_values[SENSOR_COUNT];
    int count;
};

void calibrate_temperatures(struct temp_data* data) {
    for (int i = 0; i < data->count; i++) {
        union converter cvt;
        cvt.f_val = data->raw_values[i] * CALIBRATION_FACTOR;
        data->calibrated_values[i] = cvt.f_val;
    }
}

float calculate_median(float arr[], int n) {
    // Simple bubble sort for small arrays
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                float temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    
    if (n % 2 == 0) {
        return (arr[n/2-1] + arr[n/2]) / 2.0;
    } else {
        return arr[n/2];
    }
}

int main() {
    struct temp_data sensors = {
        .raw_values = {20.0, 22.5, 19.8, 21.3, 23.1},
        .count = SENSOR_COUNT
    };
    
    calibrate_temperatures(&sensors);
    float calibrated_median = calculate_median(sensors.calibrated_values, sensors.count);
    
    printf("Result: %.2f\n", calibrated_median);
    return 0;
}
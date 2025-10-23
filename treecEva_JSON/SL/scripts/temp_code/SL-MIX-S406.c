#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

union sensor_data {
    float temperature;
    unsigned int raw_bits;
};

struct thermal_sensor {
    int sensor_id;
    union sensor_data reading;
    double calibration_factor;
};

struct sensor_array {
    int count;
    struct thermal_sensor sensors[];  // flexible array member
};

int main() {
    // Allocate memory for sensor array with 3 sensors
    struct sensor_array *array = malloc(sizeof(struct sensor_array) + 3 * sizeof(struct thermal_sensor));
    array->count = 3;
    
    // Initialize sensor readings
    array->sensors[0].reading.temperature = 85.5f;
    array->sensors[1].reading.temperature = 92.0f;
    array->sensors[2].reading.temperature = 78.25f;
    
    // Set calibration factors
    array->sensors[0].calibration_factor = 1.05;
    array->sensors[1].calibration_factor = 0.98;
    array->sensors[2].calibration_factor = 1.02;
    
    double aggregate_reading = 0.0;
    unsigned int bit_mask = 0;
    
    for (int i = 0; i < array->count; i++) {
        // Apply logarithmic scaling if temperature is above threshold
        if (array->sensors[i].reading.temperature > 80.0f && 
            !(array->sensors[i].calibration_factor < 1.0)) {  // Short-circuit evaluation
            double scaled_temp = log(array->sensors[i].reading.temperature) * array->sensors[i].calibration_factor;
            aggregate_reading += scaled_temp;
            
            // Type punning: access raw bits of temperature
            bit_mask |= array->sensors[i].reading.raw_bits;
        } else if (!(array->sensors[i].reading.temperature <= 80.0f) ||  // Short-circuit evaluation
                   array->sensors[i].calibration_factor > 1.0) {
            double corrected_temp = exp(array->sensors[i].reading.temperature / 100.0) * array->sensors[i].calibration_factor;
            aggregate_reading += corrected_temp;
        }
    }
    
    // Apply final correction using bit manipulation
    union sensor_data final_correction;
    final_correction.raw_bits = bit_mask & 0x7FFFFFFF;  // Remove sign bit
    
    double final_thermal_index = aggregate_reading * final_correction.temperature * 0.001;
    
    printf("Result: %.6f\n", final_thermal_index);
    
    free(array);
    return 0;
}
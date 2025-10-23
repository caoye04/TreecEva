#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define NUM_SENSORS 5
#define NUM_READINGS 4

// Union for type punning between float and int
union FloatInt {
    float f;
    int i;
};

// Volatile variable to simulate hardware register
volatile int sensor_status_register = 0x0F;

// Function pointer type for callback
typedef void (*FinalizeCallback)(int* result);

// Pattern matching function to detect anomalies
int is_anomaly(float reading) {
    // Simple pattern: readings outside 2 standard deviations
    const float mean = 25.0f;
    const float stddev = 5.0f;
    return fabsf(reading - mean) > (2.0f * stddev);
}

// Callback function to finalize results
void finalize_result(int* result) {
    // Apply a final adjustment based on sensor status
    *result += (sensor_status_register & 0x03);
}

int main() {
    // Temperature readings from 5 sensors, 4 readings each
    float sensor_data[NUM_SENSORS][NUM_READINGS] = {
        {24.5f, 25.1f, 23.9f, 24.8f},
        {35.2f, 36.0f, 34.8f, 35.5f},  // Anomalous sensor
        {24.9f, 25.3f, 24.7f, 25.0f},
        {15.1f, 14.8f, 15.3f, 14.9f},  // Anomalous sensor
        {25.2f, 24.8f, 25.0f, 24.9f}
    };
    
    // Matrix to store anomaly flags
    int anomaly_matrix[NUM_SENSORS][NUM_READINGS];
    
    // Statistical accumulators
    float sensor_means[NUM_SENSORS] = {0};
    int anomaly_counts[NUM_SENSORS] = {0};
    
    // Process each sensor's readings
    for (int sensor = 0; sensor < NUM_SENSORS; sensor++) {
        // Calculate mean for this sensor
        for (int reading = 0; reading < NUM_READINGS; reading++) {
            sensor_means[sensor] += sensor_data[sensor][reading];
        }
        sensor_means[sensor] /= NUM_READINGS;
        
        // Check each reading for anomalies
        for (int reading = 0; reading < NUM_READINGS; reading++) {
            anomaly_matrix[sensor][reading] = is_anomaly(sensor_data[sensor][reading]);
            if (anomaly_matrix[sensor][reading]) {
                anomaly_counts[sensor]++;
            }
        }
    }
    
    // Count total anomalies across all sensors
    int total_anomalies = 0;
    for (int sensor = 0; sensor < NUM_SENSORS; sensor++) {
        total_anomalies += anomaly_counts[sensor];
    }
    
    // Apply pattern matching to identify sensors with multiple anomalies
    int multi_anomaly_sensors = 0;
    for (int sensor = 0; sensor < NUM_SENSORS; sensor++) {
        if (anomaly_counts[sensor] > 1) {
            multi_anomaly_sensors++;
        }
    }
    
    // Use union for type punning to encode sensor information
    union FloatInt encoder;
    encoder.f = (float)multi_anomaly_sensors;
    
    // Final anomaly count incorporates pattern matching results
    int final_anomaly_count = total_anomalies + (encoder.i & 0xFF);
    
    // Apply callback to finalize result
    FinalizeCallback callback = finalize_result;
    callback(&final_anomaly_count);
    
    printf("Result: %d\n", final_anomaly_count);
    return 0;
}
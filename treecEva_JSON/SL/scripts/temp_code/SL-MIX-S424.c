#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdint.h>

union float_bits {
    float value;
    uint32_t bits;
};

struct telemetry_packet {
    unsigned int sensor_id : 4;
    unsigned int reading_type : 2;
    unsigned int encoded_value : 26;
};

int main() {
    float transformation_matrix[2][2] = {{1.5f, 0.8f}, {0.2f, 1.3f}};
    float sensor_readings[] = {2.5f, 3.7f, 1.2f, 4.8f};
    int num_readings = 4;
    
    union float_bits fb;
    struct telemetry_packet packet;
    uint32_t telemetry_sum = 0;
    
    for (int i = 0; i < num_readings; i++) {
        fb.value = sensor_readings[i];
        
        // Apply transformation matrix (simplified for 1D case)
        float transformed = transformation_matrix[0][0] * fb.value + 
                           transformation_matrix[0][1] * (i+1);
        
        // Encode using bit manipulation
        fb.value = transformed;
        packet.sensor_id = i % 4;
        packet.reading_type = (i / 2) % 2;
        packet.encoded_value = (fb.bits >> 3) & 0x3FFFFFF; // Extract 26 bits
        
        // Accumulate encoded values with bit shifting
        telemetry_sum += (packet.encoded_value << (i % 5)) ^ (packet.sensor_id * 17);
    }
    
    printf("Result: %u\n", telemetry_sum);
    return 0;
}
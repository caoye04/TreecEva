#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdint.h>

#define SIGN_MASK     0x8000
#define MAGNITUDE_MASK 0x7FFF
#define NOISE_THRESHOLD 100

struct TelemetryPacket {
    unsigned int sensor_id : 4;
    unsigned int parity_bit : 1;
    unsigned int magnitude : 15;
};

int16_t raw_readings[] = {2048, -150, 89, -2000, 55};
int n = sizeof(raw_readings)/sizeof(raw_readings[0]);

int main() {
    int16_t processed_value = 0;
    int i;
    
    // Greedy noise reduction: select first value above threshold
    for (i = 0; i < n; i++) {
        if (raw_readings[i] > NOISE_THRESHOLD || raw_readings[i] < -NOISE_THRESHOLD) {
            processed_value = raw_readings[i];
            break;
        }
    }
    
    // Encoding phase
    uint16_t sign_bit = (processed_value & SIGN_MASK) >> 15;
    uint16_t magnitude = processed_value & MAGNITUDE_MASK;
    
    // Parity calculation (odd parity)
    uint16_t temp = magnitude;
    int parity = 0;
    while(temp) {
        parity ^= (temp & 1);
        temp >>= 1;
    }
    
    // Pack into bit-field struct
    struct TelemetryPacket packet;
    packet.sensor_id = 9;  // 1001 in binary
    packet.parity_bit = parity;
    packet.magnitude = magnitude;
    
    // Final encoding with bit manipulation
    uint32_t final_encoded = 0;
    final_encoded |= ((uint32_t)packet.sensor_id << 20);
    final_encoded |= ((uint32_t)packet.parity_bit << 19);
    final_encoded |= packet.magnitude;
    
    printf("Result: %u\n", final_encoded);
    return 0;
}
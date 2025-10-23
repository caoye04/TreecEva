#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdint.h>

struct SensorReading {
    uint16_t data;
} __attribute__((packed));

union TelemetryData {
    struct SensorReading reading;
    uint16_t raw;
};

// Simple hash table for correction factors
int correction_map[16] = {2, 3, 1, 4, 2, 5, 3, 1, 4, 2, 6, 3, 5, 1, 2, 4};

int main() {
    union TelemetryData packet[5];
    
    // Initialize sensor readings with bit-packed data
    packet[0].raw = 0x1A2B;  // ID=11, Status=2, Cal=10, Flags=1
    packet[1].raw = 0x3C4D;  // ID=13, Status=4, Cal=12, Flags=3
    packet[2].raw = 0x5E6F;  // ID=15, Status=6, Cal=14, Flags=5
    packet[3].raw = 0x7A8B;  // ID=11, Status=8, Cal=10, Flags=7
    packet[4].raw = 0x9C0D;  // ID=13, Status=12, Cal=12, Flags=9
    
    int aggregate_correction = 0;
    
    for (int i = 0; i < 5; i++) {
        uint16_t raw_value = packet[i].raw;
        
        // Extract bit fields
        int sensor_id = raw_value & 0x000F;              // bits 0-3
        int status = (raw_value >> 4) & 0x000F;          // bits 4-7
        int cal_factor = (raw_value >> 8) & 0x000F;      // bits 8-11
        int env_flags = (raw_value >> 12) & 0x000F;      // bits 12-15
        
        // Apply correction based on sensor ID hash lookup
        int correction = correction_map[sensor_id];
        
        // Compute weighted correction
        int weighted_correction = correction * status + cal_factor - env_flags;
        
        // Apply to aggregate with alternating sign
        if (i % 2 == 0) {
            aggregate_correction += weighted_correction;
        } else {
            aggregate_correction -= weighted_correction;
        }
    }
    
    printf("Result: %d\n", aggregate_correction);
    return 0;
}
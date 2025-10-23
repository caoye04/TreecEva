#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdint.h>

struct PacketHeader {
    uint32_t flags : 8;
    uint32_t type : 4;
    uint32_t priority : 3;
    uint32_t reserved : 17;
};

union HeaderAccessor {
    struct PacketHeader fields;
    uint32_t raw;
};

int main() {
    union HeaderAccessor packet;
    packet.raw = 0x1AC5F39B; // Initial header value
    
    uint8_t mask1 = 0xF0;     // Mask for upper nibble
    uint8_t mask2 = 0x0F;     // Mask for lower nibble
    
    // Extract and transform flags using bit operations
    uint8_t extracted = (packet.fields.flags & mask1) >> 4;
    uint8_t transformed = ((extracted ^ 0x0A) & mask2) << 2;
    
    // Apply another transformation using dynamic programming approach
    uint8_t dp_table[16];
    for(int i = 0; i < 16; i++) {
        dp_table[i] = (i * 3 + 7) & 0x0F;
    }
    
    uint8_t lookup_result = dp_table[transformed >> 2];
    uint8_t processed_flags = (lookup_result | (packet.fields.priority << 1)) ^ 0x03;
    
    printf("Result: %d\n", processed_flags);
    return 0;
}
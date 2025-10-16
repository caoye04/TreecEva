#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

struct PacketHeader {
    unsigned int version : 4;
    unsigned int type : 4;
    unsigned int priority : 3;
    unsigned int reserved : 1;
};

union Encoder {
    struct PacketHeader fields;
    unsigned short packed;
};

int main() {
    union Encoder encoder;
    encoder.fields.version = 2;
    encoder.fields.type = 5;
    encoder.fields.priority = 7;
    encoder.fields.reserved = 0;
    
    char transform_buffer[16] = "PACKET_HEADER";
    int validation_code = 0;
    
    // Stage 1: Bit manipulation
    encoder.packed ^= 0xAAAA;
    
    // Stage 2: String transformation with nested loops
    for (int i = 0; i < strlen(transform_buffer); i++) {
        for (int j = 0; j <= i; j++) {
            if (transform_buffer[j] >= 'A' && transform_buffer[j] <= 'Z') {
                transform_buffer[j] = (transform_buffer[j] - 'A' + encoder.fields.version) % 26 + 'a';
            }
        }
        if (i == 7) break;  // Early break after 8 iterations
    }
    
    // Stage 3: Checksum calculation
    for (int i = 0; i < 8; i++) {
        if (transform_buffer[i] != '\0') {
            validation_code += (transform_buffer[i] << (i % 4));
        } else {
            return 1;  // Early return on null termination
        }
    }
    
    // Stage 4: Final adjustment using bit fields
    validation_code &= (encoder.packed >> 4);
    
    printf("Result: %d\n", validation_code);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_READINGS 10
#define CHECKSUM_MASK 0xF0

typedef struct {
    char data[9];
    int valid;
} SensorReading;

int hex_char_to_int(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return 0;
}

int validate_reading(const char* hex_str) {
    if (strlen(hex_str) != 8) return 0;
    
    for (int i = 0; i < 8; i++) {
        if (!isxdigit(hex_str[i])) return 0;
    }
    
    int checksum = 0;
    for (int i = 0; i < 6; i++) {
        checksum ^= hex_char_to_int(hex_str[i]);
    }
    
    int provided_checksum = (hex_char_to_int(hex_str[6]) << 4) | hex_char_to_int(hex_str[7]);
    return ((checksum << 4) & CHECKSUM_MASK) == (provided_checksum & CHECKSUM_MASK);
}

int main() {
    SensorReading readings[MAX_READINGS] = {
        {"A1B2C3D4", 0},
        {"FF00EE11", 0},
        {"12345678", 0},
        {"DEADBEEF", 0},
        {"CAFEBABE", 0},
        {"89ABCDEF", 0},
        {"00000000", 0},
        {"FFFFFFFF", 0},
        {"55555555", 0},
        {"AAAAAAAA", 0}
    };
    
    int validated_count = 0;
    
    for (int i = 0; i < MAX_READINGS; i++) {
        readings[i].valid = validate_reading(readings[i].data);
        if (readings[i].valid) {
            validated_count++;
        }
    }
    
    // Execution point Y
    printf("Result: %d\n", validated_count);
    return 0;
}
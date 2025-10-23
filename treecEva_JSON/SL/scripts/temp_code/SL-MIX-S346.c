#define _USE_MATH_DEFINES
#include <stdio.h>

#define SENSOR_COUNT 8
#define MODULUS 251

int main() {
    volatile int sensor_readings[SENSOR_COUNT] = {42, 18, 73, 29, 55, 91, 37, 64};
    int* reading_ptr = sensor_readings;
    int checksum = 0;
    int i;
    
    for (i = 0; i < SENSOR_COUNT; i++) {
        int temp = *(reading_ptr + i);
        
        // Apply modular arithmetic with previous checksum
        temp = (temp * 3 + checksum) % MODULUS;
        
        // Bitwise transformations
        if (i % 2 == 0) {
            temp = (temp ^ 0xAA) & 0xFF;  // XOR with 170, mask to 8 bits
        } else {
            temp = ((temp << 2) | (temp >> 6)) & 0xFF;  // Rotate left by 2
        }
        
        // Update checksum using modular addition
        checksum = (checksum + temp) % MODULUS;
        
        // Apply bitwise AND with index for even positions
        if ((i & 1) == 0) {
            checksum &= (0xFF >> (i/2));  // Progressive masking
        }
    }
    
    // Final adjustment
    checksum = checksum ^ (checksum >> 4);
    checksum = (checksum * 7) % MODULUS;
    
    printf("Result: %d\n", checksum);
    return 0;
}
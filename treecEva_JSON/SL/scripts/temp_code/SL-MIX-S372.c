#define _USE_MATH_DEFINES
#include <stdio.h>

struct PixelConfig {
    unsigned int blue : 5;
    unsigned int green : 6;
    unsigned int red : 5;
};

int main() {
    unsigned int pixel_value = 0b1101010110101011;
    unsigned int green_mask = 0x7E0; // Mask for bits 10-5
    unsigned int green_intensity;
    
    // Extract green component using mask and shift
    green_intensity = (pixel_value & green_mask) >> 5;
    
    printf("Result: %u\n", green_intensity);
    return 0;
}
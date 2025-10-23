#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

struct Pixel {
    unsigned int red : 5;
    unsigned int green : 6;
    unsigned int blue : 5;
};

int main() {
    struct Pixel p = {15, 32, 10};
    double distance_factor;
    int adjusted_brightness;
    
    // Calculate Euclidean distance from origin in color space
    distance_factor = sqrt(p.red * p.red + p.green * p.green + p.blue * p.blue);
    
    // Normalize and scale
    adjusted_brightness = (int)(distance_factor * 2.5);
    
    // Apply bit masking
    adjusted_brightness = adjusted_brightness & 0x7F;
    
    printf("Result: %d\n", adjusted_brightness);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

struct ThermalPixel {
    unsigned int isValid : 1;
    unsigned int isHotSpot : 1;
    unsigned int reserved : 6;
    float temperature;
};

struct ThermalImage {
    int width;
    int height;
    struct ThermalPixel pixels[];  // flexible array member
};

int main() {
    // Allocate memory for a 4x4 thermal image
    struct ThermalImage* img = (struct ThermalImage*)malloc(sizeof(struct ThermalImage) + 16 * sizeof(struct ThermalPixel));
    img->width = 4;
    img->height = 4;
    
    // Initialize thermal readings (4x4 matrix)
    float readings[4][4] = {
        {23.5f, 24.1f, 25.0f, 22.8f},
        {26.3f, 30.2f, 28.9f, 27.4f},
        {24.7f, 25.5f, 31.8f, 29.6f},
        {23.9f, 26.1f, 28.3f, 25.7f}
    };
    
    // Populate the flexible array with initial data
    for (int i = 0; i < 16; i++) {
        int row = i / 4;
        int col = i % 4;
        img->pixels[i].temperature = readings[row][col];
        img->pixels[i].isValid = 1;
        img->pixels[i].isHotSpot = 0;
        img->pixels[i].reserved = 0;
    }
    
    float thermalSum = 0.0f;
    volatile int hotSpotCount = 0;  // volatile variable
    
    // Process each pixel
    for (int i = 0; i < 16; i++) {
        // Apply a floating-point transformation (normalize to 0-1 range)
        float normalized = (img->pixels[i].temperature - 20.0f) / 15.0f;
        
        // Update hot spot flag using bit manipulation
        if (normalized > 0.7f) {
            img->pixels[i].isHotSpot = 1;
            hotSpotCount++;
        }
        
        // Apply another floating-point operation (square root of normalized value)
        if (normalized >= 0) {
            thermalSum += sqrtf(normalized);
        }
        
        // Use pointer arithmetic to access the next pixel
        struct ThermalPixel* current = img->pixels + i;
        if (current->isHotSpot) {
            thermalSum *= 1.05f;  // Boost sum for hot spots
        }
    }
    
    // Final adjustment using bitwise operations
    if (hotSpotCount & 1) {  // if odd number of hot spots
        thermalSum += 1.0f;
    }
    
    printf("Result: %.6f\n", thermalSum);
    free(img);
    return 0;
}
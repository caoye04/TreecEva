#define _USE_MATH_DEFINES
#include <stdio.h>
#define GAIN_FACTOR 3

int main() {
    int audio_buffer[8] = {10, 20, 30, 40, 50, 60, 70, 80};
    int mask = 0xF0;  // Bitwise mask to filter upper nibble
    int processed[8];
    int i;
    
    // Apply gain and mask
    for (i = 0; i < 8; i++) {
        processed[i] = (audio_buffer[i] * GAIN_FACTOR) & mask;
    }
    
    // Binary search for threshold value 0x60
    int target = 0x60;
    int left = 0;
    int right = 7;
    int threshold_index = -1;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        if (processed[mid] == target) {
            threshold_index = mid;
            break;
        } else if (processed[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    printf("Result: %d\n", threshold_index);
    return 0;
}
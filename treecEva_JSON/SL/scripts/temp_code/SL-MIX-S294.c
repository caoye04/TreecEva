#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 16

int main() {
    float audio_buffer[BUFFER_SIZE];
    float *head = audio_buffer;
    float *tail = audio_buffer + 3;  // Initially 3 positions behind head
    
    int head_index = 0;
    int tail_index = 3;
    
    // Process 17 audio frames
    for (int frame = 0; frame < 17; frame++) {
        // Advance head by 5 positions with wrap-around
        head_index = (head_index + 5) % BUFFER_SIZE;
        head = audio_buffer + head_index;
        
        // Update tail only if buffer isn't overly full
        // (maintain at least 2 positions gap)
        int gap = (head_index - tail_index + BUFFER_SIZE) % BUFFER_SIZE;
        if (gap >= 2 || gap == 0) {  // Short-circuit: check if safe to advance
            tail_index = (tail_index + 1) % BUFFER_SIZE;
            tail = audio_buffer + tail_index;
        }
        
        // Simulate audio processing with floating point operations
        *head = (float)frame * 0.5f + 1.25f;
        
        // Apply gain control using modular arithmetic on frame count
        if ((frame % 3 == 0) && (frame > 0)) {  // Logical AND with short-circuit
            *head *= (float)(frame % 7);
        }
    }
    
    int tail_offset = tail_index;
    printf("Result: %d\n", tail_offset);
    return 0;
}
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef int (*transform_func)(int);

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int apply_window(int sample) {
    return sample & 0xFF; // Mask to 8-bit
}

int scale_amplitude(int sample) {
    int fib_factor = fibonacci(6); // 8
    return (sample * fib_factor) >> 3; // Divide by 8 using bit shift
}

int main() {
    transform_func pipeline[2] = {apply_window, scale_amplitude};
    
    int raw_sample = 0x1A7F; // Raw 16-bit audio sample
    int processed_sample = raw_sample;
    
    // Apply transformation pipeline
    for (int i = 0; i < 2; i++) {
        processed_sample = pipeline[i](processed_sample);
    }
    
    // Calculate gain adjustment with logical operations
    int base_gain = 0xF0;
    int modulation = 0x0F;
    int final_gain = (base_gain & ~modulation) | ((processed_sample ^ 0xAA) & modulation);
    
    printf("Result: %d\n", final_gain);
    return 0;
}
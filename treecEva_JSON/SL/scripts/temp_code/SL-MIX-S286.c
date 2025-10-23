#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef int (*filter_func_t)(int*, int);

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int apply_filter(int* signal_block, int block_size) {
    int accumulator = 0;
    for (int i = 0; i < block_size; i++) {
        accumulator += signal_block[i] * fibonacci(i+1);
        if (i > 0 && (signal_block[i] & signal_block[i-1]) != 0) {
            accumulator ^= 0xFF;
        }
    }
    return accumulator;
}

int process_audio_stream(filter_func_t filter_callback, int* stream, int stream_length) {
    int processed_samples = 0;
    int block_size = 4;
    
    for (int i = 0; i < stream_length; i += block_size) {
        int remaining = (stream_length - i < block_size) ? stream_length - i : block_size;
        int block_result = filter_callback(&stream[i], remaining);
        
        if ((block_result & 0x01) == 1) {
            processed_samples += remaining * 2;
        } else {
            processed_samples += remaining;
        }
        
        if (block_result > 100) {
            processed_samples -= 1;
        }
    }
    
    return processed_samples;
}

int main() {
    int audio_stream[] = {3, 7, 2, 5, 8, 1, 4, 6};
    int stream_length = sizeof(audio_stream)/sizeof(audio_stream[0]);
    
    int processed_samples = process_audio_stream(apply_filter, audio_stream, stream_length);
    
    printf("Result: %d\n", processed_samples);
    return 0;
}
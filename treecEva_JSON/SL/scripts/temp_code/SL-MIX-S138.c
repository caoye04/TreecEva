#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BUFFER_SIZE 8
#define FLAG_FULL    0x01
#define FLAG_EMPTY   0x02
#define FLAG_LOCKED  0x04
#define FLAG_DIRTY   0x08

typedef struct {
    int16_t *samples;
    uint8_t state_flags;
    uint8_t head;
    uint8_t tail;
} AudioBuffer;

AudioBuffer* create_buffer() {
    AudioBuffer* buf = (AudioBuffer*)malloc(sizeof(AudioBuffer));
    buf->samples = (int16_t*)calloc(BUFFER_SIZE, sizeof(int16_t));
    buf->state_flags = FLAG_EMPTY;
    buf->head = 0;
    buf->tail = 0;
    return buf;
}

int main() {
    AudioBuffer* pcm_buffer = create_buffer();
    uint8_t control_word = 0xAA;  // 10101010
    
    // Simulate buffer filling
    for (int i = 0; i < 5; i++) {
        pcm_buffer->samples[pcm_buffer->head] = (int16_t)(i * 100);
        pcm_buffer->head = (pcm_buffer->head + 1) % BUFFER_SIZE;
    }
    
    // Update state using bitwise operations
    if (pcm_buffer->head != pcm_buffer->tail) {
        pcm_buffer->state_flags &= ~FLAG_EMPTY;
        pcm_buffer->state_flags |= FLAG_DIRTY;
    }
    
    // Process control word with short-circuit evaluation
    if ((control_word & 0xF0) && (pcm_buffer->state_flags & FLAG_DIRTY)) {
        control_word ^= 0x55;  // XOR with 01010101
        pcm_buffer->state_flags |= FLAG_LOCKED;
    }
    
    // Final state calculation
    uint8_t final_state = 0;
    if (!(pcm_buffer->state_flags & FLAG_FULL) || (pcm_buffer->head == pcm_buffer->tail)) {
        final_state = (pcm_buffer->state_flags << 2) ^ (control_word >> 3);
    }
    
    printf("Result: %d\n", final_state);
    
    free(pcm_buffer->samples);
    free(pcm_buffer);
    return 0;
}
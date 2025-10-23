#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    volatile int head;
    volatile int tail;
    volatile int size;
    int data[];  // flexible array member
} circular_buffer_t;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int calculate_checksum(circular_buffer_t* buffer) {
    int checksum = 0;
    int capacity = buffer->size - 1;
    
    // Short-circuit evaluation in condition
    if (buffer != NULL && buffer->head >= 0 && buffer->tail >= 0) {
        // Use GCD in calculation
        checksum = gcd(buffer->head + 1, buffer->tail + 1);
        checksum += gcd(capacity, buffer->head);
        
        // Conditional branch based on buffer state
        if (buffer->head > buffer->tail) {
            checksum += (buffer->head - buffer->tail);
        } else if (buffer->head < buffer->tail) {
            checksum += (buffer->tail - buffer->head);
        } else {
            checksum += buffer->size;
        }
    }
    
    return checksum;
}

int main() {
    int buffer_size = 8;
    circular_buffer_t* sensor_buffer = malloc(sizeof(circular_buffer_t) + buffer_size * sizeof(int));
    
    sensor_buffer->head = 5;
    sensor_buffer->tail = 2;
    sensor_buffer->size = buffer_size;
    
    // Initialize buffer data
    for (int i = 0; i < buffer_size; i++) {
        sensor_buffer->data[i] = i * 3 + 1;
    }
    
    int diagnostic_checksum = calculate_checksum(sensor_buffer);
    
    // Perform some buffer operations that modify volatile variables
    sensor_buffer->head = (sensor_buffer->head + 3) % buffer_size;
    sensor_buffer->tail = (sensor_buffer->tail + 1) % buffer_size;
    
    // Recalculate checksum after operations
    diagnostic_checksum += calculate_checksum(sensor_buffer);
    
    printf("Result: %d\n", diagnostic_checksum);
    free(sensor_buffer);
    return 0;
}
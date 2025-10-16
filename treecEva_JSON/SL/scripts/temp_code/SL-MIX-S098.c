#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 8
#define PACKET_MASK 0x07

typedef struct {
    int head;
    int tail;
    int count;
    unsigned char data[];
} CircularBuffer;

int main() {
    size_t buffer_size = sizeof(CircularBuffer) + BUFFER_SIZE * sizeof(unsigned char);
    CircularBuffer* buffer = (CircularBuffer*)malloc(buffer_size);
    
    buffer->head = 0;
    buffer->tail = 0;
    buffer->count = 0;
    
    int incoming_data[] = {0x15, 0x2A, 0x3F, 0x4C, 0x59, 0x6E, 0x7D, 0x8B, 0x98, 0xA3};
    int data_len = sizeof(incoming_data)/sizeof(incoming_data[0]);
    
    int processed_packets = 0;
    int i = 0;
    
    while (i < data_len) {
        // Enqueue if space available (short-circuit evaluation)
        if (buffer->count < BUFFER_SIZE && (buffer->data[buffer->head] = (unsigned char)(incoming_data[i] & 0xFF)) || 1) {
            buffer->head = (buffer->head + 1) & PACKET_MASK;
            buffer->count++;
            i++;
        }
        
        // Process packets based on priority determined by MSB
        switch ((buffer->data[buffer->tail] >> 4) & 0x0F) {
            case 0x01:
            case 0x02:
            case 0x03:
                processed_packets += (buffer->data[buffer->tail] & 0x0F) ? 2 : 1;
                break;
            case 0x04:
            case 0x05:
                processed_packets += 3;
                break;
            default:
                processed_packets += (buffer->data[buffer->tail] > 0x80) ? 4 : 1;
        }
        
        // Dequeue processed packet
        buffer->tail = (buffer->tail + 1) & PACKET_MASK;
        buffer->count--;
        
        // Priority boost for every 3rd packet (ternary operator)
        processed_packets += (++processed_packets % 3 == 0) ? 5 : 0;
    }
    
    // Handle remaining packets in buffer
    while (buffer->count > 0) {
        int priority = (buffer->data[buffer->tail] >> 4) & 0x0F;
        processed_packets += (priority >= 0x06) ? 
                            ((priority & 0x01) ? 6 : 7) : 
                            ((buffer->data[buffer->tail] & 0x03) + 1);
        buffer->tail = (buffer->tail + 1) & PACKET_MASK;
        buffer->count--;
    }
    
    free(buffer);
    printf("Result: %d\n", processed_packets);
    return 0;
}
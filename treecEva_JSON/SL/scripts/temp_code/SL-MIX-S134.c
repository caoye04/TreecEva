#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define HEAP_SIZE 16

// Bit field for packet priority flags
struct PacketFlags {
    unsigned int priority : 3;   // 0-7 priority levels
    unsigned int retry : 1;      // Retry flag
    unsigned int ack : 1;        // Acknowledgment flag
    unsigned int reserved : 3;   // Reserved bits
};

// Min-heap implementation for packet scheduling
int heap[HEAP_SIZE];
int heap_count = 0;

void heap_push(int priority) {
    if (heap_count >= HEAP_SIZE) return;
    heap[heap_count] = priority;
    int i = heap_count++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent] <= heap[i]) break;
        int temp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = temp;
        i = parent;
    }
}

int heap_pop() {
    if (heap_count <= 0) return -1;
    int result = heap[0];
    heap[0] = heap[--heap_count];
    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;
        if (left < heap_count && heap[left] < heap[smallest])
            smallest = left;
        if (right < heap_count && heap[right] < heap[smallest])
            smallest = right;
        if (smallest == i) break;
        int temp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = temp;
        i = smallest;
    }
    return result;
}

// State machine states
enum PacketState {
    IDLE = 0,
    QUEUED = 1,
    TRANSMITTING = 2,
    ACKNOWLEDGED = 3,
    RETRANSMIT = 4
};

int main() {
    // Packet processing state machine
    enum PacketState state = IDLE;
    int transmission_rounds = 0;
    int ack_count = 0;
    
    // Process 7 packets with different priority flags
    struct PacketFlags packets[7] = {
        {5, 0, 1, 0},  // High priority, acknowledged
        {2, 1, 0, 0},  // Medium priority, needs retry
        {7, 0, 0, 0},  // Low priority, no ack
        {1, 1, 1, 0},  // Highest priority, retry but ack'd
        {4, 1, 0, 0},  // Mid priority, retry needed
        {3, 0, 1, 0},  // High-mid priority, ack'd
        {6, 1, 0, 0}   // Low-mid priority, retry needed
    };
    
    for (int i = 0; i < 7; i++) {
        struct PacketFlags *pkt = &packets[i];
        
        // State transition logic
        switch (state) {
            case IDLE:
                if (pkt->priority > 3) {
                    state = QUEUED;
                } else {
                    state = TRANSMITTING;
                }
                break;
                
            case QUEUED:
                if (pkt->retry) {
                    heap_push(pkt->priority);
                    state = RETRANSMIT;
                } else if (pkt->ack) {
                    ack_count += 1;
                    state = ACKNOWLEDGED;
                } else {
                    state = TRANSMITTING;
                }
                break;
                
            case TRANSMITTING:
                if (pkt->ack) {
                    ack_count += 1;
                    state = ACKNOWLEDGED;
                } else if (pkt->retry) {
                    heap_push(pkt->priority);
                    state = RETRANSMIT;
                } else {
                    state = IDLE;
                }
                break;
                
            case ACKNOWLEDGED:
                state = IDLE;
                break;
                
            case RETRANSMIT:
                transmission_rounds += 1;
                if (pkt->ack) {
                    ack_count += 1;
                    state = ACKNOWLEDGED;
                } else {
                    state = IDLE;
                }
                break;
        }
    }
    
    // Process retransmission queue
    while (heap_count > 0) {
        heap_pop();
        transmission_rounds += 2;  // Each retransmission takes 2 rounds
    }
    
    printf("Result: %d\n", transmission_rounds);
    return 0;
}
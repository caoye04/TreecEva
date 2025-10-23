#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define PACKET_COUNT 7

typedef struct {
    int priority;
    int size;
    long timestamp;
} PacketHeader;

typedef struct Node {
    int data;
    struct Node* next;
} QueueNode;

typedef struct {
    QueueNode* front;
    QueueNode* rear;
} Queue;

Queue* create_queue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

void enqueue(Queue* q, int value) {
    QueueNode* newNode = (QueueNode*)malloc(sizeof(QueueNode));
    newNode->data = value;
    newNode->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    volatile int total_processing_weight = 0;
    volatile int packet_sequence_mask = 0xF0; // 11110000 in binary
    
    Queue* processing_queue = create_queue();
    
    PacketHeader headers[PACKET_COUNT] = {
        {3, 128, 1000},
        {1, 256, 1005},
        {2, 64,  1012},
        {3, 512, 1020},
        {1, 32,  1030},
        {2, 192, 1035},
        {3, 96,  1042}
    };
    
    for (int i = 0; i < PACKET_COUNT; i++) {
        // Calculate packet weight using GCD of size and priority
        int base_weight = headers[i].size / gcd(headers[i].size, headers[i].priority);
        
        // Apply timestamp factor using bitwise operations
        int timestamp_factor = (headers[i].timestamp & packet_sequence_mask) >> 4;
        
        // Compute processing weight with arithmetic operations
        int processing_weight = (base_weight * headers[i].priority) + (timestamp_factor ^ 0x0A);
        
        // Add to queue for processing
        enqueue(processing_queue, processing_weight);
        
        // Update accumulator with cumulative XOR
        total_processing_weight ^= processing_weight;
    }
    
    // Final adjustment - sum all queued values with accumulator
    QueueNode* current = processing_queue->front;
    while (current != NULL) {
        total_processing_weight += (current->data & 0xFF); // Only lower 8 bits
        current = current->next;
    }
    
    printf("Result: %d\n", total_processing_weight);
    
    // Cleanup
    while (processing_queue->front != NULL) {
        QueueNode* temp = processing_queue->front;
        processing_queue->front = processing_queue->front->next;
        free(temp);
    }
    free(processing_queue);
    
    return 0;
}
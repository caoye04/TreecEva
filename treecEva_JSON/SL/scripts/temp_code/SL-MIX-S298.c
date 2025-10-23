#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 8

struct packet_metadata {
    unsigned int priority : 3;
    unsigned int type : 5;
    unsigned int checksum : 8;
    unsigned int reserved : 16;
};

union memory_block {
    struct packet_metadata meta;
    unsigned int raw_data;
};

struct node {
    union memory_block data;
    struct node* next;
};

struct queue {
    struct node* front;
    struct node* rear;
};

struct stack {
    struct node* top;
};

void enqueue(struct queue* q, union memory_block block) {
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = block;
    temp->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
}

union memory_block dequeue(struct queue* q) {
    if (q->front == NULL) {
        union memory_block empty = {0};
        return empty;
    }
    struct node* temp = q->front;
    union memory_block block = temp->data;
    q->front = q->front->next;
    if (q->front == NULL) q->rear = NULL;
    free(temp);
    return block;
}

void push(struct stack* s, union memory_block block) {
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = block;
    temp->next = s->top;
    s->top = temp;
}

union memory_block pop(struct stack* s) {
    if (s->top == NULL) {
        union memory_block empty = {0};
        return empty;
    }
    struct node* temp = s->top;
    union memory_block block = temp->data;
    s->top = s->top->next;
    free(temp);
    return block;
}

int main() {
    struct queue packet_queue = {NULL, NULL};
    struct stack processing_stack = {NULL};
    
    // Initialize packets
    union memory_block packets[4];
    packets[0].meta.priority = 5;
    packets[0].meta.type = 12;
    packets[0].meta.checksum = 0xAA;
    
    packets[1].meta.priority = 3;
    packets[1].meta.type = 7;
    packets[1].meta.checksum = 0x55;
    
    packets[2].meta.priority = 7;
    packets[2].meta.type = 21;
    packets[2].meta.checksum = 0xCC;
    
    packets[3].meta.priority = 1;
    packets[3].meta.type = 3;
    packets[3].meta.checksum = 0x33;
    
    // Enqueue all packets
    for (int i = 0; i < 4; i++) {
        enqueue(&packet_queue, packets[i]);
    }
    
    // Process packets: dequeue and push to stack
    for (int i = 0; i < 3; i++) {
        union memory_block block = dequeue(&packet_queue);
        // Modify checksum using bitwise operations
        block.meta.checksum = (block.meta.checksum ^ 0xFF) & 0xFF;
        push(&processing_stack, block);
    }
    
    // Calculate final checksum
    unsigned int final_checksum = 0;
    while (processing_stack.top != NULL) {
        union memory_block block = pop(&processing_stack);
        // Combine checksums using XOR
        final_checksum ^= block.meta.checksum;
        // Apply floating point operation
        float f_val = (float)final_checksum * 1.5f;
        // Convert back to integer
        final_checksum = (unsigned int)f_val;
        // Apply bit shift
        final_checksum = (final_checksum << 1) | (final_checksum >> 7);
        // Mask to 8 bits
        final_checksum &= 0xFF;
    }
    
    printf("Result: %u\n", final_checksum);
    return 0;
}
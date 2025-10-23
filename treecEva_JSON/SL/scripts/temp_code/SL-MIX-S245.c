#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#define HEAP_SIZE 8

struct PacketHeader {
    unsigned int type : 3;
    unsigned int priority : 4;
    unsigned int reserved : 1;
    unsigned int flags : 8;
};

int heap[HEAP_SIZE];
int heap_count = 0;

void heap_push(int value) {
    if (heap_count >= HEAP_SIZE) return;
    int i = heap_count++;
    heap[i] = value;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent] >= heap[i]) break;
        int temp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = temp;
        i = parent;
    }
}

int heap_pop() {
    if (heap_count <= 0) return 0;
    int result = heap[0];
    heap[0] = heap[--heap_count];
    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = i;
        if (left < heap_count && heap[left] > heap[largest])
            largest = left;
        if (right < heap_count && heap[right] > heap[largest])
            largest = right;
        if (largest == i) break;
        int temp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = temp;
        i = largest;
    }
    return result;
}

int main() {
    struct PacketHeader pkt1 = {0};
    pkt1.type = 5;
    pkt1.priority = 12;
    pkt1.flags = 0xAB;
    
    struct PacketHeader pkt2 = {0};
    pkt2.type = 3;
    pkt2.priority = 7;
    pkt2.flags = 0x3C;
    
    int mask = 0xF0;
    int masked_flags1 = pkt1.flags & mask;
    int masked_flags2 = pkt2.flags & mask;
    
    int xor_result = masked_flags1 ^ masked_flags2;
    int shifted_priority1 = pkt1.priority << 1;
    int shifted_priority2 = pkt2.priority >> 1;
    
    double exp_val = pow(2.0, 3.0);
    int log_val = (int)log2((double)xor_result);
    
    heap_push(shifted_priority1);
    heap_push(shifted_priority2);
    heap_push(log_val);
    heap_push((int)exp_val);
    
    int sum_popped = 0;
    int iterations = 0;
    while (heap_count > 0 && iterations < 3) {
        sum_popped += heap_pop();
        iterations++;
    }
    
    int final_priority = sum_popped & 0xFF;
    printf("Result: %d\n", final_priority);
    return 0;
}
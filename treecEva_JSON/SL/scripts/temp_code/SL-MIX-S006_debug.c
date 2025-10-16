#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define HEAP_SIZE 100
#define PRIORITY_MASK 0x0F
#define MOD_BASE 17

int heap[HEAP_SIZE];
int heap_size = 0;

void push(int value) {
    if (heap_size >= HEAP_SIZE) return;
    int i = heap_size++;
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

int pop() {
    if (heap_size <= 0) return 0;
    int result = heap[0];
    heap[0] = heap[--heap_size];
    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = i;
        if (left < heap_size && heap[left] > heap[largest])
            largest = left;
        if (right < heap_size && heap[right] > heap[largest])
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
    int packet_data[] = {23, 45, 12, 67, 34, 89, 56};
    int data_size = sizeof(packet_data) / sizeof(packet_data[0]);
    
    for (int i = 0; i < data_size; i++) {
        int masked_value = packet_data[i] & PRIORITY_MASK;
        int priority = (masked_value * 3 + 7) % MOD_BASE;
        push(priority);
    }
    
    int extracted_priorities[3];
    for (int i = 0; i < 3; i++) {
        extracted_priorities[i] = pop();
    }
    
    int final_priority = 0;
    for (int i = 0; i < 3; i++) {
        final_priority ^= (extracted_priorities[i] << (i * 2));
    }
    
    final_priority = (final_priority + 11) % MOD_BASE;
    
    printf("Result: %d\n", final_priority);
    return 0;
}
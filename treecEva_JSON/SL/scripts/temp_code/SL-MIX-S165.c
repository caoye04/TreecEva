#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

#define HEAP_SIZE 10
#define SIGNAL_COUNT 5

volatile int heap[HEAP_SIZE];
int heap_size = 0;

void heap_push(int value) {
    if (heap_size >= HEAP_SIZE) return;
    heap[heap_size] = value;
    int current = heap_size++;
    while (current > 0) {
        int parent = (current - 1) / 2;
        if (heap[current] >= heap[parent]) break;
        int temp = heap[current];
        heap[current] = heap[parent];
        heap[parent] = temp;
        current = parent;
    }
}

int heap_pop() {
    if (heap_size <= 0) return 0;
    int result = heap[0];
    heap[0] = heap[--heap_size];
    int current = 0;
    while (1) {
        int left = current * 2 + 1;
        int right = current * 2 + 2;
        if (left >= heap_size) break;
        int swap_idx = left;
        if (right < heap_size && heap[right] < heap[left])
            swap_idx = right;
        if (heap[current] <= heap[swap_idx]) break;
        int temp = heap[current];
        heap[current] = heap[swap_idx];
        heap[swap_idx] = temp;
        current = swap_idx;
    }
    return result;
}

union SignalData {
    float value;
    unsigned int bits;
};

int process_signal(const char* signal_type, float raw_value) {
    union SignalData data;
    data.value = raw_value;
    
    if (strcmp(signal_type, "TEMP") == 0) {
        return (int)(data.value * 10) & 0xFF;
    } else if (strcmp(signal_type, "PRESSURE") == 0) {
        return (data.bits >> 16) & 0xFF;
    } else if (strcmp(signal_type, "VOLTAGE") == 0) {
        return (int)data.value % 256;
    }
    return 0;
}

int main() {
    const char* signals[SIGNAL_COUNT] = {"TEMP", "PRESSURE", "VOLTAGE", "TEMP", "PRESSURE"};
    float values[SIGNAL_COUNT] = {25.7f, 1013.25f, 3.3f, 18.4f, 998.7f};
    
    int state = 0;
    volatile int adjusted_priority = 0;
    
    for (int i = 0; i < SIGNAL_COUNT; i++) {
        int base_priority = process_signal(signals[i], values[i]);
        
        switch (state) {
            case 0: 
                heap_push(base_priority);
                if (base_priority > 100) state = 1;
                break;
            case 1:
                heap_push(base_priority + 10);
                if (base_priority < 50) state = 2;
                break;
            case 2:
                heap_push(base_priority - 5);
                state = 0;
                break;
        }
    }
    
    while (heap_size > 0) {
        adjusted_priority += heap_pop();
    }
    
    printf("Result: %d\n", adjusted_priority);
    return 0;
}
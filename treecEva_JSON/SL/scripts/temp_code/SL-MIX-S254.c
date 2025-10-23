#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define HEAP_SIZE 100

int heap[HEAP_SIZE];
int heap_size = 0;

void heapify_up(int index) {
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap[index] <= heap[parent]) break;
        int temp = heap[index];
        heap[index] = heap[parent];
        heap[parent] = temp;
        index = parent;
    }
}

void insert(int value) {
    if (heap_size >= HEAP_SIZE) return;
    heap[heap_size] = value;
    heapify_up(heap_size);
    heap_size++;
}

int main() {
    int packets[] = {100, 250, 50, 400, 150};
    int n = sizeof(packets) / sizeof(packets[0]);
    
    for (int i = 0; i < n; i++) {
        int scaled_priority;
        switch (i % 3) {
            case 0:
                scaled_priority = (int)(log(packets[i]) * 10);
                break;
            case 1:
                scaled_priority = (int)(exp(packets[i] / 100.0));
                break;
            case 2:
            default:
                scaled_priority = packets[i] * 2;
                break;
        }
        insert(scaled_priority);
    }
    
    printf("Result: %d\n", heap[0]);
    return 0;
}
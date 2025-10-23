#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdint.h>

#define HEAP_SIZE 16

uint32_t heap[HEAP_SIZE];
int heap_size = 0;

void push(uint32_t task_priority) {
    if (heap_size >= HEAP_SIZE) return;
    int i = heap_size++;
    heap[i] = task_priority;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent] >= heap[i]) break;
        uint32_t temp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = temp;
        i = parent;
    }
}

uint32_t pop() {
    if (heap_size <= 0) return 0;
    uint32_t root = heap[0];
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
        uint32_t temp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = temp;
        i = largest;
    }
    return root;
}

int partition(uint32_t* arr, int low, int high) {
    uint32_t pivot = (arr[low] >> 28) & 0xF;
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (((arr[j] >> 28) & 0xF) >= pivot) {
            i++;
            uint32_t temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    uint32_t temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i + 1;
}

void quick_select(uint32_t* arr, int low, int high, int k) {
    if (low < high) {
        int pi = partition(arr, low, high);
        if (pi == k) return;
        else if (pi > k)
            quick_select(arr, low, pi - 1, k);
        else
            quick_select(arr, pi + 1, high, k);
    }
}

int main() {
    // Priority encoding: bits 31-28 = urgency (0-15), bits 27-0 = category
    uint32_t tasks[] = {0x70000001, 0xA0000002, 0x30000003, 0xF0000004, 0x50000005,
                        0xC0000006, 0x10000007, 0xE0000008, 0x60000009, 0xB000000A,
                        0x2000000B, 0xD000000C, 0x4000000D, 0x9000000E, 0x0000000F,
                        0x80000010};
    
    // Initialize heap with tasks
    for (int i = 0; i < 16; i++) {
        push(tasks[i]);
    }
    
    int sched_yield_count = 0;
    
    // Process 3 rounds of greedy task selection
    for (int round = 0; round < 3; round++) {
        // Copy heap for divide-and-conquer partitioning
        uint32_t temp_heap[HEAP_SIZE];
        for (int i = 0; i < heap_size; i++) {
            temp_heap[i] = heap[i];
        }
        
        // Partition around median urgency (position 7)
        quick_select(temp_heap, 0, heap_size - 1, 7);
        
        // Greedy selection: process tasks with urgency > threshold
        int threshold = 8;
        int round_count = 0;
        for (int i = 0; i < heap_size; i++) {
            int urgency = (heap[i] >> 28) & 0xF;
            if (urgency > threshold) {
                round_count++;
            }
        }
        sched_yield_count += round_count;
        
        // Remove processed tasks from heap
        for (int i = 0; i < round_count; i++) {
            pop();
        }
    }
    
    printf("Result: %d\n", sched_yield_count);
    return 0;
}
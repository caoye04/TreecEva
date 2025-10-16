#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define HEAP_SIZE 8

// Min-heap structure
typedef struct {
    int* data;
    int size;
    int capacity;
} MinHeap;

MinHeap* create_heap(int capacity) {
    MinHeap* heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->capacity = capacity;
    heap->size = 0;
    heap->data = (int*)malloc(capacity * sizeof(int));
    return heap;
}

void insert_heap(MinHeap* heap, int value) {
    if (heap->size >= heap->capacity) return;
    heap->data[heap->size] = value;
    int current = heap->size++;
    while (current > 0) {
        int parent = (current - 1) / 2;
        if (heap->data[current] >= heap->data[parent]) break;
        int temp = heap->data[current];
        heap->data[current] = heap->data[parent];
        heap->data[parent] = temp;
        current = parent;
    }
}

int fibonacci(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    MinHeap* key_heap = create_heap(HEAP_SIZE);
    
    // Populate heap with Fibonacci numbers mod 256
    for (int i = 1; i <= HEAP_SIZE; i++) {
        insert_heap(key_heap, fibonacci(i*2) % 256);
    }
    
    // Bitwise scramble phase
    int scramble_mask = 0xAA;  // 10101010
    for (int i = 0; i < key_heap->size; i++) {
        key_heap->data[i] = (key_heap->data[i] << 2) ^ scramble_mask;
    }
    
    // Extract and combine keys using XOR
    int master_key = 0;
    for (int i = 0; i < key_heap->size; i++) {
        master_key ^= key_heap->data[i];
    }
    
    // TARGET VARIABLE
    printf("Result: %d\n", master_key);
    
    free(key_heap->data);
    free(key_heap);
    return 0;
}
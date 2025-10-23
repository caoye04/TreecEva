#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define HEAP_SIZE 100

int heap[HEAP_SIZE];
int heap_count = 0;

void heap_push(int value) {
    heap[heap_count] = value;
    int idx = heap_count++;
    
    while (idx > 0) {
        int parent = (idx - 1) / 2;
        if (heap[parent] <= heap[idx]) break;
        int temp = heap[parent];
        heap[parent] = heap[idx];
        heap[idx] = temp;
        idx = parent;
    }
}

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    // Simulate memory allocations with Fibonacci-sized blocks
    for (int i = 1; i <= 7; i++) {
        heap_push(fibonacci(i));
    }
    
    // After all insertions, what is the root of the min-heap?
    printf("Result: %d\n", heap[0]);
    return 0;
}
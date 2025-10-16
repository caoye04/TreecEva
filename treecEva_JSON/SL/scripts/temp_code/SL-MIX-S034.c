#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define HEAP_SIZE 100

// Simple min-heap implementation
int heap[HEAP_SIZE];
int heap_size = 0;

void push(int value) {
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

int pop() {
    if (heap_size <= 0) return -1;
    int result = heap[0];
    heap[0] = heap[--heap_size];
    int current = 0;
    while (1) {
        int left = current * 2 + 1;
        int right = current * 2 + 2;
        if (left >= heap_size) break;
        int smallest = (right < heap_size && heap[right] < heap[left]) ? right : left;
        if (heap[current] <= heap[smallest]) break;
        int temp = heap[current];
        heap[current] = heap[smallest];
        heap[smallest] = temp;
        current = smallest;
    }
    return result;
}

// Encoding/decoding function using XOR and position-based mask
int encode_size(int size, int position) {
    return size ^ (0x5A5A ^ (position << 3));
}

int decode_size(int encoded, int position) {
    return encoded ^ (0x5A5A ^ (position << 3));
}

int main() {
    // Function pointer for size processing
    int (*size_processor)(int, int) = decode_size;
    
    // Initialize heap with encoded block sizes
    int initial_blocks[] = {0x5B5B, 0x5858, 0x5F5F, 0x5C5C};
    int num_initial = sizeof(initial_blocks) / sizeof(initial_blocks[0]);
    
    // Add initial blocks to heap after decoding
    for (int i = 0; i < num_initial; i++) {
        int decoded = size_processor(initial_blocks[i], i);
        push(decoded);
    }
    
    // Simulate allocation requests
    int allocations[] = {16, 32};
    int num_allocations = sizeof(allocations) / sizeof(allocations[0]);
    
    for (int i = 0; i < num_allocations; i++) {
        int requested = allocations[i];
        // Find a block that's large enough
        int temp_heap[HEAP_SIZE];
        int temp_size = 0;
        int found_block = -1;
        
        // Extract all blocks and find one that fits
        while (heap_size > 0) {
            int block = pop();
            temp_heap[temp_size++] = block;
            if (block >= requested) {
                found_block = block;
                break;
            }
        }
        
        // Put back unused blocks
        for (int j = 0; j < temp_size; j++) {
            if (temp_heap[j] != found_block) {
                push(temp_heap[j]);
            }
        }
        
        // If we found a block, split it if necessary and put back remainder
        if (found_block > requested) {
            push(found_block - requested);
        }
    }
    
    // Simulate deallocation with encoded block sizes
    int deallocations[] = {encode_size(24, 4), encode_size(12, 5)};
    int num_deallocations = sizeof(deallocations) / sizeof(deallocations[0]);
    
    for (int i = 0; i < num_deallocations; i++) {
        int decoded = size_processor(deallocations[i], i+4);
        push(decoded);
    }
    
    // Apply a ternary operator to adjust the top block size
    int top_block = pop();
    top_block = (top_block > 50) ? top_block - 10 : top_block + 5;
    push(top_block);
    
    // What is the value of the smallest block size in the heap?
    int smallest_block_size = heap[0];
    printf("Result: %d\n", smallest_block_size);
    return 0;
}
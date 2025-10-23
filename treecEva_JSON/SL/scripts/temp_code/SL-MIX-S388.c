#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define CALCULATE_TOTAL_ALLOCATED(heap, count, total) \
    do { \
        total = 0; \
        for (int i = 0; i < count; i++) { \
            if (heap[i].status == 1) { \
                total += heap[i].size; \
            } \
        } \
    } while(0)

typedef struct {
    int size;
    int status;
} MemoryBlock;

int main() {
    MemoryBlock heap[] = {{100, 1}, {250, 0}, {50, 1}, {300, 1}, {75, 0}};
    int block_count = sizeof(heap) / sizeof(heap[0]);
    int total_memory;
    
    CALCULATE_TOTAL_ALLOCATED(heap, block_count, total_memory);
    
    printf("Result: %d\n", total_memory);
    return 0;
}
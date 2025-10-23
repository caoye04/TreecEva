#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define HEAP_SIZE 1024
#define PAGE_MASK 0xFFF00000
#define PAGE_SHIFT 20

typedef struct {
    uint32_t* data;
    int size;
    int capacity;
} Stack;

void stack_init(Stack* s) {
    s->data = (uint32_t*)malloc(100 * sizeof(uint32_t));
    s->size = 0;
    s->capacity = 100;
}

void stack_push(Stack* s, uint32_t value) {
    if (s->size < s->capacity) {
        s->data[s->size++] = value;
    }
}

uint32_t stack_pop(Stack* s) {
    if (s->size > 0) {
        return s->data[--s->size];
    }
    return 0;
}

void heap_sort(uint32_t arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        int parent = i;
        while (parent * 2 + 1 < n) {
            int child = parent * 2 + 1;
            if (child + 1 < n && arr[child] < arr[child + 1])
                child++;
            if (arr[parent] < arr[child]) {
                uint32_t temp = arr[parent];
                arr[parent] = arr[child];
                arr[child] = temp;
                parent = child;
            } else {
                break;
            }
        }
    }
    for (int i = n - 1; i > 0; i--) {
        uint32_t temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        int parent = 0;
        while (parent * 2 + 1 < i) {
            int child = parent * 2 + 1;
            if (child + 1 < i && arr[child] < arr[child + 1])
                child++;
            if (arr[parent] < arr[child]) {
                temp = arr[parent];
                arr[parent] = arr[child];
                arr[child] = temp;
                parent = child;
            } else {
                break;
            }
        }
    }
}

int binary_search(uint32_t arr[], int n, uint32_t target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    Stack alloc_stack;
    stack_init(&alloc_stack);
    
    uint32_t heap_pages[HEAP_SIZE];
    uint32_t page_mask = PAGE_MASK;
    uint32_t checksum = 0;
    
    // Simulate allocations
    for (int i = 0; i < 16; i++) {
        uint32_t addr = 0x10000000 + (i * 0x1000);
        uint32_t page = (addr & page_mask) >> PAGE_SHIFT;
        heap_pages[i] = page;
        stack_push(&alloc_stack, page);
    }
    
    // Sort pages
    heap_sort(heap_pages, 16);
    
    // Process stack
    while (alloc_stack.size > 0) {
        uint32_t page = stack_pop(&alloc_stack);
        int index = binary_search(heap_pages, 16, page);
        if (index != -1) {
            checksum ^= (page << 4) | (index & 0xF);
        }
    }
    
    printf("Result: %u\n", checksum);
    return 0;
}
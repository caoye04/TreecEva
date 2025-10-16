#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define MAX_TASKS 100

typedef struct {
    int priority;
} Task;

typedef struct {
    Task* tasks;
    int size;
    int capacity;
} TaskHeap;

TaskHeap* create_heap(int capacity) {
    TaskHeap* heap = (TaskHeap*)malloc(sizeof(TaskHeap));
    heap->capacity = capacity;
    heap->size = 0;
    heap->tasks = (Task*)malloc(capacity * sizeof(Task));
    return heap;
}

void swap(Task* a, Task* b) {
    Task temp = *a;
    *a = *b;
    *b = temp;
}

void heapify_up(TaskHeap* heap, int index) {
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap->tasks[index].priority <= heap->tasks[parent].priority)
            break;
        swap(&heap->tasks[index], &heap->tasks[parent]);
        index = parent;
    }
}

void heapify_down(TaskHeap* heap, int index) {
    while (1) {
        int left_child = 2 * index + 1;
        int right_child = 2 * index + 2;
        int largest = index;

        if (left_child < heap->size && heap->tasks[left_child].priority > heap->tasks[largest].priority)
            largest = left_child;
        if (right_child < heap->size && heap->tasks[right_child].priority > heap->tasks[largest].priority)
            largest = right_child;

        if (largest == index)
            break;

        swap(&heap->tasks[index], &heap->tasks[largest]);
        index = largest;
    }
}

void insert_task(TaskHeap* heap, int priority) {
    if (heap->size >= heap->capacity) return;
    heap->tasks[heap->size].priority = priority;
    heapify_up(heap, heap->size);
    heap->size++;
}

Task extract_max(TaskHeap* heap) {
    if (heap->size <= 0) {
        Task empty = {0};
        return empty;
    }
    Task max_task = heap->tasks[0];
    heap->tasks[0] = heap->tasks[heap->size - 1];
    heap->size--;
    heapify_down(heap, 0);
    return max_task;
}

int main() {
    TaskHeap* scheduler = create_heap(MAX_TASKS);
    
    // Insert initial tasks
    insert_task(scheduler, 15);
    insert_task(scheduler, 30);
    insert_task(scheduler, 10);
    insert_task(scheduler, 45);
    insert_task(scheduler, 20);
    
    // Extract the highest priority task
    extract_max(scheduler);
    
    // Insert new tasks
    insert_task(scheduler, 35);
    insert_task(scheduler, 5);
    
    // Extract another task
    extract_max(scheduler);
    
    // Final root priority after all operations
    int final_root_priority = scheduler->tasks[0].priority;
    
    printf("Result: %d\n", final_root_priority);
    
    free(scheduler->tasks);
    free(scheduler);
    
    return 0;
}
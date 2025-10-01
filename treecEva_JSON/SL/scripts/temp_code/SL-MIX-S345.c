#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_NODES 5

struct Node {
    int value;
    struct Node* next;
};

struct DataContainer {
    int array[3];
    struct Node* head;
    double multiplier;
};

int bitwise_transform(int x, int y) {
    return (x & 0xF) | ((y << 2) ^ 0xAA);
}

int main() {
    struct DataContainer container = {{2, 4, 8}, NULL, 1.5};
    struct Node nodes[MAX_NODES];
    
    // Initialize linked list
    for (int i = 0; i < MAX_NODES; i++) {
        nodes[i].value = (i + 1) * 3;
        nodes[i].next = (i < MAX_NODES - 1) ? &nodes[i+1] : NULL;
    }
    container.head = &nodes[0];
    
    // Stage 1: Array manipulation with math operations
    for (int i = 0; i < 3; i++) {
        container.array[i] = (int)(pow(container.array[i], 2) + sqrt(container.array[i] * 4));
    }
    
    // Stage 2: Linked list traversal with bitwise operations
    struct Node* current = container.head;
    int accumulator = 0;
    int index = 0;
    while (current != NULL) {
        accumulator ^= bitwise_transform(current->value, index);
        current = current->next;
        index++;
    }
    
    // Stage 3: Complex calculation using container data
    double intermediate = 0.0;
    for (int i = 0; i < 3; i++) {
        intermediate += container.array[i] * container.multiplier;
    }
    
    // Stage 4: Final computation combining all elements
    int list_sum = 0;
    current = container.head;
    while (current != NULL) {
        list_sum += current->value;
        current = current->next;
    }
    
    int final_result = (int)(intermediate) ^ (accumulator & 0xFF) ^ (list_sum >> 1);
    
    printf("Result: %d\n", final_result);
    return 0;
}
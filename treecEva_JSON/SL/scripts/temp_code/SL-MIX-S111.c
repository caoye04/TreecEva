#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 5

struct Node {
    int values[3];
    struct Node* next;
};

struct DataContainer {
    struct Node* head;
    int size;
};

int complex_operation(int a, int b, int c) {
    return (a * b + c) ^ (a | b) & ~(c >> 1);
}

int calculate_sum(struct DataContainer* container) {
    int sum = 0;
    struct Node* current = container->head;
    
    while (current != NULL) {
        for (int i = 0; i < 3; i++) {
            sum += current->values[i] * (i + 1);
        }
        current = current->next;
    }
    
    return sum;
}

int main() {
    struct DataContainer container = {NULL, 0};
    
    // Create linked list nodes
    struct Node nodes[MAX_NODES];
    
    // Initialize nodes with complex values
    for (int i = 0; i < MAX_NODES; i++) {
        nodes[i].values[0] = (i + 1) * (i + 2);
        nodes[i].values[1] = (int)pow(i + 1, 3);
        nodes[i].values[2] = (i + 1) * (i + 3) + 7;
        nodes[i].next = (i < MAX_NODES - 1) ? &nodes[i + 1] : NULL;
    }
    
    container.head = &nodes[0];
    container.size = MAX_NODES;
    
    // Perform complex calculations
    int intermediate = calculate_sum(&container);
    
    // Apply mathematical transformations
    double sqrt_val = sqrt((double)intermediate);
    int trig_val = (int)(sin(sqrt_val) * 1000);
    
    // Bitwise operations
    int bitwise_result = (intermediate & 0xFF) | ((trig_val >> 2) ^ 0xAA);
    
    // Final complex operation
    int final_calc = complex_operation(intermediate, trig_val, bitwise_result);
    
    // Apply modulo to keep result in reasonable range
    int result = final_calc % 10000;
    
    printf("Result: %d\n", result);
    
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_NODES 5

struct Node {
    int value;
    struct Node* next;
};

struct DataContainer {
    int values[3];
    struct Node* head;
};

int complex_operation(int a, int b) {
    return (a << 2) ^ (b >> 1) & 0xF;
}

int main() {
    struct DataContainer container;
    struct Node nodes[MAX_NODES];
    
    // Initialize array values
    container.values[0] = 12;
    container.values[1] = 25;
    container.values[2] = 8;
    
    // Build linked list
    for(int i = 0; i < MAX_NODES; i++) {
        nodes[i].value = (i + 1) * 7;
        nodes[i].next = (i < MAX_NODES - 1) ? &nodes[i+1] : NULL;
    }
    container.head = &nodes[0];
    
    // Perform calculations
    int sum = 0;
    for(int i = 0; i < 3; i++) {
        sum += container.values[i] * (int)pow(-1, i);
    }
    
    // Traverse linked list and apply complex operation
    struct Node* current = container.head;
    int accumulator = 0;
    int counter = 0;
    while(current != NULL && counter < 3) {
        accumulator = complex_operation(accumulator, current->value);
        current = current->next;
        counter++;
    }
    
    // Final computation
    int intermediate = (sum & 0xFF) | (accumulator << 4);
    double trig_result = sin(intermediate * M_PI / 180.0);
    int final_result = (int)(trig_result * 1000) + (intermediate ^ 0xAA);
    
    printf("Result: %d\n", final_result);
    return 0;
}
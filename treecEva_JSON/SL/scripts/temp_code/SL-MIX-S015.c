#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_NODES 5

struct Node {
    int id;
    double value;
    struct Node* next;
};

typedef struct {
    struct Node nodes[MAX_NODES];
    int count;
} NodeList;

int main() {
    NodeList list = {0};
    
    // Initialize node values using compound literals and pointer arithmetic
    for (int i = 0; i < MAX_NODES; i++) {
        list.nodes[i].id = i + 1;
        list.nodes[i].value = pow(-1, i) * (i + 1) * M_PI;
        if (i < MAX_NODES - 1) {
            list.nodes[i].next = &list.nodes[i+1];
        } else {
            list.nodes[i].next = NULL;
        }
    }
    list.count = MAX_NODES;
    
    // Perform complex bitwise and arithmetic operations
    long long accumulator = 0;
    unsigned int mask = 0xF0F0F0F0;
    
    struct Node* current = list.nodes;
    int index = 0;
    
    while(current != NULL && index < 3) {
        long long temp = (long long)(current->value * 100);
        
        // Bitwise operations combined with modulo arithmetic
        if ((index & 1) == 0) {
            temp ^= mask;
        } else {
            temp |= (mask >> 4);
        }
        
        // Apply sign based on node id parity and mathematical transformation
        if (current->id % 2 == 0) {
            temp = labs(temp) % 1000000;
        } else {
            temp = -(labs(temp) % 1000000);
        }
        
        accumulator += temp;
        current = current->next;
        index++;
    }
    
    // Final transformation sequence
    accumulator >>= 2;
    accumulator *= -1;
    
    // String manipulation to extract numeric component
    char buffer[32];
    snprintf(buffer, sizeof(buffer), "%lld", accumulator);
    
    int target_result = 0;
    for(int i=0; buffer[i] != '\0'; i++) {
        if(buffer[i] >= '0' && buffer[i] <= '9') {
            target_result += buffer[i] - '0';
        } else if(buffer[i] == '-') {
            target_result -= 10;
        }
    }
    
    // Mathematical finalization
    target_result = abs(target_result) * (int)ceil(sin(M_PI/6) * 10);
    
    printf("Target result: %d\n", target_result);
    return 0;
}
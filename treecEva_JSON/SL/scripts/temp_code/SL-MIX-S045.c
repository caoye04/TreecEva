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
    int i;
    double accumulator = 0.0;
    int bitmask = 0xF0;
    int shift_val = 2;
    
    // Initialize nodes
    for (i = 0; i < MAX_NODES; i++) {
        list.nodes[i].id = i + 1;
        list.nodes[i].value = pow(-1, i) * (i + 1) * M_PI;
        if (i < MAX_NODES - 1) {
            list.nodes[i].next = &list.nodes[i+1];
        } else {
            list.nodes[i].next = NULL;
        }
    }
    list.count = MAX_NODES;
    
    // Traverse and compute
    struct Node* current = list.nodes;
    i = 0;
    while (current != NULL && i < 3) {
        double temp = current->value;
        if (i % 2 == 0) {
            temp = fabs(temp);
        }
        accumulator += temp;
        current = current->next;
        i++;
    }
    
    // Bitwise and mathematical operations
    int x = (bitmask >> shift_val) & 0x0F;
    double y = sin(M_PI / 6);
    int z = (int)(y * 100);
    
    // Final computation
    int result = (int)(accumulator) ^ (x + z);
    printf("Result: %d\n", result);
    return 0;
}
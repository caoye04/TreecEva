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

struct Graph {
    struct Node nodes[MAX_NODES];
    int count;
};

void initialize_graph(struct Graph* g) {
    for (int i = 0; i < MAX_NODES; i++) {
        g->nodes[i].id = i;
        g->nodes[i].value = pow(-1, i) * (i + 1) * M_PI;
        g->nodes[i].next = (i < MAX_NODES - 1) ? &g->nodes[i+1] : NULL;
    }
    g->count = MAX_NODES;
}

int main() {
    struct Graph g;
    initialize_graph(&g);
    
    double accumulator = 0.0;
    int counter = 0;
    struct Node* current = g.nodes;
    
    while (current != NULL && counter < 3) {
        if (counter % 2 == 0) {
            accumulator += current->value * 2;
        } else {
            accumulator -= fabs(current->value);
        }
        current = current->next;
        counter++;
    }
    
    // Perform a bitwise operation on counter
    int mask = 0xF0;
    counter = (counter << 2) & mask;
    
    // Use counter to index into a calculated array
    double values[4] = {sin(accumulator), cos(accumulator), tan(accumulator/2), sqrt(fabs(accumulator))};
    double selected = values[(counter >> 4) % 4];
    
    // Final calculation
    int target_value = (int)(selected * 1000) ^ 0xAA;
    
    printf("Result: %d\n", target_value);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 10

typedef struct {
    int id;
    double value;
    int links[3];
} Node;

typedef struct {
    Node nodes[MAX_NODES];
    int count;
} Graph;

int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

double compute_weighted_sum(Graph* g, int node_index) {
    double sum = 0.0;
    Node* n = &g->nodes[node_index];
    
    for (int i = 0; i < 3; i++) {
        int link_id = n->links[i];
        if (link_id >= 0 && link_id < g->count) {
            sum += g->nodes[link_id].value * sin(g->nodes[link_id].value);
        }
    }
    
    return sum + n->value * cos(n->value);
}

int main() {
    Graph g;
    g.count = 5;
    
    // Initialize nodes
    for (int i = 0; i < g.count; i++) {
        g.nodes[i].id = i;
        g.nodes[i].value = (i + 1) * M_PI / 4.0;
        
        // Set up links (circular references)
        g.nodes[i].links[0] = (i + 1) % g.count;
        g.nodes[i].links[1] = (i + 3) % g.count;
        g.nodes[i].links[2] = (i + 4) % g.count;
    }
    
    // Perform complex transformations
    double accumulator = 0.0;
    for (int i = 0; i < g.count; i++) {
        double weighted = compute_weighted_sum(&g, i);
        g.nodes[i].value = pow(weighted, 1.0/3.0) + log(fabs(weighted) + 1);
        accumulator += g.nodes[i].value;
    }
    
    // Apply bitwise operations to transform accumulator
    int bit_pattern = (int)(accumulator * 1000) & 0x3FF;  // Take 10 bits
    bit_pattern = (bit_pattern << 3) | (bit_pattern >> 7); // Rotate left by 3
    bit_pattern ^= 0x155; // XOR with pattern
    
    // Final calculation combining all elements
    double trig_component = sin(accumulator) * cos(accumulator/2.0);
    double exp_component = exp(trig_component);
    
    // Use factorial in final computation
    int final_result = (int)(exp_component * 1000) + factorial(bit_pattern % 6);
    
    printf("Result: %d\n", final_result);
    return 0;
}
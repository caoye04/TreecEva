#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int weight;
    struct Node* left;
    struct Node* right;
};

struct Packet {
    volatile int priority;
    int metadata;
};

int process_packet(struct Packet* pkt, struct Node* root) {
    if (!root) return pkt->metadata;
    
    // Apply modular transformation
    pkt->metadata = (pkt->metadata * root->weight + 7) % 13;
    
    // Conditional routing with short-circuit evaluation
    return (pkt->priority > 0 && root->left) ? 
           process_packet(pkt, root->left) : 
           (root->right ? process_packet(pkt, root->right) : pkt->metadata);
}

int main() {
    // Initialize packet
    struct Packet pkt = {3, 5};
    
    // Build binary tree
    struct Node n1 = {2, NULL, NULL};
    struct Node n2 = {4, NULL, NULL};
    struct Node n3 = {3, &n1, &n2};
    struct Node n4 = {5, NULL, NULL};
    struct Node root = {1, &n3, &n4};
    
    // Process packet through tree
    int intermediate = process_packet(&pkt, &root);
    
    // Apply final transformations
    int queue_op = (intermediate << 1) & 7;  // Bitwise shift and mask
    int stack_op = (queue_op > 4) ? queue_op - 2 : queue_op + 3;  // Ternary operator
    
    volatile int final_metric = ((stack_op * 3) % 11) + (pkt.priority && intermediate ? 1 : 0);  // Short-circuit eval
    
    printf("Result: %d\n", final_metric);
    return 0;
}
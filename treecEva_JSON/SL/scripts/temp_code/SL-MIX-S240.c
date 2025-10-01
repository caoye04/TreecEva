#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 10

struct Node {
    int id;
    double value;
    struct Node* next;
};

struct DataContainer {
    struct Node* head;
    int count;
    char tag[32];
};

struct ComputationUnit {
    struct DataContainer containers[3];
    int active_index;
    double accumulator;
};

// Function to compute factorial
long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Function to initialize a node
struct Node* create_node(int id, double value) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->id = id;
    node->value = value;
    node->next = NULL;
    return node;
}

// Function to add a node to container
void add_node(struct DataContainer* container, int id, double value) {
    struct Node* node = create_node(id, value);
    node->next = container->head;
    container->head = node;
    container->count++;
}

// Function to compute weighted sum of container nodes
double compute_weighted_sum(struct DataContainer* container) {
    double sum = 0.0;
    struct Node* current = container->head;
    int index = 1;
    
    while (current != NULL) {
        sum += current->value * pow(-1, index) * index;
        current = current->next;
        index++;
    }
    return sum;
}

int main() {
    struct ComputationUnit unit;
    unit.active_index = 2;
    unit.accumulator = 0.0;
    
    // Initialize containers
    for (int i = 0; i < 3; i++) {
        unit.containers[i].head = NULL;
        unit.containers[i].count = 0;
        sprintf(unit.containers[i].tag, "Container_%d", i);
    }
    
    // Populate containers with data
    add_node(&unit.containers[0], 1, 3.14159);
    add_node(&unit.containers[0], 2, 2.71828);
    add_node(&unit.containers[0], 3, 1.41421);
    
    add_node(&unit.containers[1], 1, 10.0);
    add_node(&unit.containers[1], 2, 20.0);
    add_node(&unit.containers[1], 3, 30.0);
    add_node(&unit.containers[1], 4, 40.0);
    
    add_node(&unit.containers[2], 1, -5.5);
    add_node(&unit.containers[2], 2, 7.2);
    
    // Perform complex computation sequence
    double temp1 = compute_weighted_sum(&unit.containers[0]);
    double temp2 = compute_weighted_sum(&unit.containers[1]);
    double temp3 = compute_weighted_sum(&unit.containers[2]);
    
    // Mathematical transformations
    long long fact_result = factorial(5);
    double trig_result = sin(temp1) * cos(temp2) + tan(temp3);
    
    // Bitwise operations on intermediate results
    int bitwise_a = (int)(temp1 * 100) & 0xFF;
    int bitwise_b = (int)(temp2 * 10) | 0xF0;
    int bitwise_c = bitwise_a ^ bitwise_b;
    
    // Complex logical evaluation
    int condition_a = (temp1 > 0) && (temp2 < 100);
    int condition_b = (temp3 <= 0) || (fact_result > 100);
    int final_condition = condition_a ^ condition_b;
    
    // Multi-step calculation with nested operations
    double intermediate = pow(trig_result, 3) - sqrt(fabs(temp1 * temp2));
    long long combined_bits = ((long long)bitwise_c << 16) | ((long long)fact_result & 0xFFFF);
    
    // TARGET ASSIGNMENT
    int target_value = (int)(intermediate * 1000) + (final_condition ? (int)combined_bits : -(int)combined_bits);
    
    printf("Result: %d\n", target_value);
    return 0;
}
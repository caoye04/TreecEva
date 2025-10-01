#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 5

struct Node {
    int id;
    double value;
    struct Node* next;
};

struct DataContainer {
    struct Node nodes[MAX_NODES];
    int count;
    char tag[32];
};

int main() {
    struct DataContainer container;
    strcpy(container.tag, "COMPLEX_DATA");
    container.count = 0;
    
    // Initialize nodes with complex values
    for (int i = 0; i < MAX_NODES; i++) {
        container.nodes[i].id = i + 1;
        container.nodes[i].value = pow(-1, i) * (i + 1) * M_PI;
        container.nodes[i].next = (i < MAX_NODES - 1) ? &container.nodes[i+1] : NULL;
        container.count++;
    }
    
    // Perform complex calculations
    double accumulator = 0.0;
    struct Node* current = container.nodes;
    int index = 0;
    
    while (current != NULL && index < MAX_NODES) {
        double temp = current->value;
        if (index % 2 == 0) {
            temp = fabs(temp) * 2.5;
        } else {
            temp = -sqrt(fabs(temp)) * 3.0;
        }
        
        if (temp > 0) {
            accumulator += temp;
        } else {
            accumulator *= 0.5;
        }
        
        current = current->next;
        index++;
    }
    
    // Apply final transformation
    int tag_length = strlen(container.tag);
    double final_result = accumulator;
    
    if (tag_length > 10) {
        final_result = final_result * tag_length / 7.0;
    } else {
        final_result = final_result + tag_length;
    }
    
    // Bitwise adjustment
    int int_part = (int)final_result;
    int_part = (int_part << 2) ^ 0xF0;
    final_result = (double)int_part + (final_result - (int)final_result);
    
    printf("Result: %.6f\n", final_result);
    return 0;
}
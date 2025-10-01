#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 5

struct Node {
    int values[3];
    double weight;
    struct Node* next;
};

struct DataContainer {
    struct Node nodes[MAX_NODES];
    int active_count;
    char tag[16];
};

int main() {
    struct DataContainer container;
    strcpy(container.tag, "COMPLEX");
    container.active_count = 3;
    
    // Initialize nodes
    for(int i = 0; i < container.active_count; i++) {
        container.nodes[i].values[0] = (i + 1) * 10;
        container.nodes[i].values[1] = (i + 1) * 20;
        container.nodes[i].values[2] = (i + 1) * 30;
        container.nodes[i].weight = sqrt((i + 1) * 7.0);
        container.nodes[i].next = (i < container.active_count - 1) ? &container.nodes[i+1] : NULL;
    }
    
    // Complex calculation chain
    double accumulator = 0.0;
    int bit_pattern = 0xF0;
    int mask = 0x0F;
    
    struct Node* current = &container.nodes[0];
    int index = 0;
    
    while(current != NULL && index < container.active_count) {
        // Perform bitwise operations on node values
        int xor_result = current->values[0] ^ current->values[1];
        int and_result = xor_result & bit_pattern;
        int shifted = and_result >> 2;
        
        // Mathematical operations
        double sin_component = sin(current->weight);
        double cos_component = cos(current->weight / 2.0);
        double combined = sin_component * cos_component * 100.0;
        
        // Update accumulator with weighted combination
        accumulator += (shifted * combined) / (index + 1.0);
        
        // String-based conditional operation
        if (strlen(container.tag) > index) {
            accumulator *= 1.0 + (container.tag[index] % 7) / 100.0;
        }
        
        current = current->next;
        index++;
    }
    
    // Final complex transformation
    int integer_part = (int)accumulator;
    int fractional_part = (int)((accumulator - integer_part) * 1000);
    
    // Bitwise manipulation of final parts
    int masked_integer = integer_part & 0xFF;
    int rotated_fractional = ((fractional_part << 4) | (fractional_part >> 12)) & 0xFFFF;
    
    // Final calculation
    int result = (masked_integer ^ rotated_fractional) + (integer_part >> 3);
    
    printf("Result: %d\n", result);
    return 0;
}
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 10

typedef struct {
    int id;
    double value;
    int flags;
} DataNode;

typedef struct {
    DataNode nodes[MAX_NODES];
    int count;
    char label[32];
} DataContainer;

int main() {
    DataContainer container;
    strcpy(container.label, "TestContainer");
    container.count = 5;
    
    // Initialize nodes
    for(int i = 0; i < container.count; i++) {
        container.nodes[i].id = i + 1;
        container.nodes[i].value = pow(2.0, i) * M_PI;
        container.nodes[i].flags = (i & 1) ? (0xF0 >> i) : (0x0F << i);
    }
    
    double accumulator = 0.0;
    int mask = 0xAA;
    
    // Complex processing loop
    for(int i = 0; i < container.count; i++) {
        DataNode* node = &container.nodes[i];
        
        // Apply bitwise masking to flags
        node->flags &= mask;
        
        // Perform conditional mathematical operations
        if((node->flags & 0x03) == 0x03) {
            node->value = sqrt(fabs(node->value)) * log(fabs(node->value) + 1);
        } else if(node->flags & 0x01) {
            node->value = ceil(node->value) / floor(fabs(node->value) + 0.5);
        } else {
            node->value = fabs(node->value) - trunc(node->value);
        }
        
        // Update accumulator with transformed value
        accumulator += (node->id % 2) ? node->value : -node->value;
        
        // Rotate mask
        mask = ((mask << 1) | (mask >> 7)) & 0xFF;
    }
    
    // Final calculation step
    int final_flag = 0;
    for(int i = 0; i < container.count; i++) {
        final_flag ^= container.nodes[i].flags;
    }
    
    double final_result = accumulator;
    if(final_flag & 0x80) {
        final_result = final_result * sin(final_result) + cos(final_result/2);
    } else {
        final_result = final_result * cos(final_result) - sin(final_result/2);
    }
    
    // Apply final transformation
    final_result = round(final_result * 1000.0) / 1000.0;
    
    printf("Result: %.3f\n", final_result);
    return 0;
}
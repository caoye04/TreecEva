#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 32

struct ModeConfig {
    unsigned int filter_enable : 1;
    unsigned int dither_enable : 1;
    unsigned int reserved : 6;
};

union Register {
    struct ModeConfig config;
    unsigned char byte;
};

typedef struct HashNode {
    unsigned char key;
    int count;
    struct HashNode* next;
} HashNode;

HashNode* hash_table[HASH_SIZE];

unsigned int hash(unsigned char key) {
    return key % HASH_SIZE;
}

void increment_count(unsigned char key) {
    unsigned int index = hash(key);
    HashNode* current = hash_table[index];
    
    while (current != NULL) {
        if (current->key == key) {
            current->count++;
            return;
        }
        current = current->next;
    }
    
    HashNode* new_node = (HashNode*)malloc(sizeof(HashNode));
    new_node->key = key;
    new_node->count = 1;
    new_node->next = hash_table[index];
    hash_table[index] = new_node;
}

int main() {
    // Initialize hash table
    for (int i = 0; i < HASH_SIZE; i++) {
        hash_table[i] = NULL;
    }
    
    // Sequence of register configurations
    union Register reg;
    unsigned char configs[] = {0x03, 0x01, 0x02, 0x03, 0x00, 0x03, 0x01, 0x03};
    int num_configs = sizeof(configs) / sizeof(configs[0]);
    
    // Process each configuration
    for (int i = 0; i < num_configs; i++) {
        reg.byte = configs[i];
        increment_count(reg.byte);
    }
    
    // Count activations where both FILTER_ENABLE and DITHER_ENABLE are set
    int target_activations = 0;
    for (int i = 0; i < HASH_SIZE; i++) {
        HashNode* current = hash_table[i];
        while (current != NULL) {
            reg.byte = current->key;
            if (reg.config.filter_enable && reg.config.dither_enable) {
                target_activations += current->count;
            }
            current = current->next;
        }
    }
    
    // Clean up
    for (int i = 0; i < HASH_SIZE; i++) {
        HashNode* current = hash_table[i];
        while (current != NULL) {
            HashNode* temp = current;
            current = current->next;
            free(temp);
        }
    }
    
    printf("Result: %d\n", target_activations);
    return 0;
}
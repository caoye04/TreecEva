#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define HASH_MULTIPLIER 31
#define DATA_LENGTH 5

typedef struct Node {
    int value;
    struct Node* next;
} Node;

unsigned int simple_hash(const char* str) {
    unsigned int hash = 0;
    while (*str) {
        hash = hash * HASH_MULTIPLIER + (*str++);
    }
    return hash;
}

int main() {
    char rr_data[DATA_LENGTH][10] = {"0x3C", "0x42", "0x38", "0x46", "0x3E"};
    int hex_values[DATA_LENGTH];
    int checksum_accum = 0;
    
    // Parse hexadecimal values
    for (int i = 0; i < DATA_LENGTH; i++) {
        sscanf(rr_data[i], "%x", &hex_values[i]);
    }
    
    // Create linked list from values
    Node* head = NULL;
    Node* current = NULL;
    
    for (int i = 0; i < DATA_LENGTH; i++) {
        Node* new_node = (Node*)malloc(sizeof(Node));
        new_node->value = hex_values[i];
        new_node->next = NULL;
        
        if (head == NULL) {
            head = new_node;
            current = head;
        } else {
            current->next = new_node;
            current = new_node;
        }
    }
    
    // Process linked list values
    current = head;
    int position = 1;
    int checksum_result = 0;
    
    while (current != NULL) {
        int value = current->value;
        int transformed = (value > 50) ? (int)(log(value) * 10) : (int)(pow(2, value/10));
        
        if (position % 2 == 0) {
            checksum_result ^= (transformed << 2);
        } else {
            checksum_result |= (transformed & 0xFF);
        }
        
        checksum_accum += transformed;
        current = current->next;
        position++;
    }
    
    // Final checksum adjustment
    checksum_result = (checksum_result > 1000) ? checksum_result/2 : checksum_result * 3;
    
    // Clean up linked list
    current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
    
    printf("Result: %d\n", checksum_result);
    return 0;
}
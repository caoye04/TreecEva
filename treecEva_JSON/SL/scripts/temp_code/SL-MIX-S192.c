#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct PacketNode {
    int size;
    struct PacketNode* next;
} PacketNode;

int main() {
    PacketNode* head = NULL;
    PacketNode* current = NULL;
    
    // Simulate packet reception: 64, 128, 32, 256, 16
    int packets[] = {64, 128, 32, 256, 16};
    int num_packets = 5;
    
    // Build linked list
    for (int i = 0; i < num_packets; i++) {
        PacketNode* new_node = (PacketNode*)malloc(sizeof(PacketNode));
        new_node->size = packets[i];
        new_node->next = NULL;
        
        if (head == NULL) {
            head = new_node;
            current = head;
        } else {
            current->next = new_node;
            current = new_node;
        }
    }
    
    // Process packets
    int total_bytes = 0;
    PacketNode* temp = head;
    
    while (temp != NULL) {
        if (temp->size > 100) {
            break;  // Early return simulation
        }
        total_bytes += temp->size;
        temp = temp->next;
    }
    
    printf("Result: %d\n", total_bytes);
    
    // Free allocated memory
    while (head != NULL) {
        PacketNode* to_free = head;
        head = head->next;
        free(to_free);
    }
    
    return 0;
}
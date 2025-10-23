#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007

typedef struct PacketNode {
    int id;
    int size;
    int ack_time;
    struct PacketNode* next;
} PacketNode;

typedef struct Stack {
    int items[100];
    int top;
} Stack;

void push(Stack* s, int value) {
    s->items[++s->top] = value;
}

int pop(Stack* s) {
    return s->items[s->top--];
}

long long mod_exp(long long base, long long exp, long long modulus) {
    long long result = 1;
    base %= modulus;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % modulus;
        base = (base * base) % modulus;
        exp >>= 1;
    }
    return result;
}

int main() {
    // Initialize packet linked list
    PacketNode* head = NULL;
    PacketNode* current = NULL;
    
    // Simulated packet data
    int packets[][3] = {{1, 128, 5}, {2, 256, 3}, {3, 64, 7}, {4, 512, 2}};
    int num_packets = 4;
    
    // Build linked list
    for (int i = 0; i < num_packets; i++) {
        PacketNode* node = (PacketNode*)malloc(sizeof(PacketNode));
        node->id = packets[i][0];
        node->size = packets[i][1];
        node->ack_time = packets[i][2];
        node->next = NULL;
        
        if (!head) {
            head = node;
            current = node;
        } else {
            current->next = node;
            current = node;
        }
    }
    
    // Process packets with stack
    Stack ack_stack = {.top = -1};
    current = head;
    long long cumulative_checksum = 0;
    
    while (current != NULL) {
        // Compute modular exponentiation of size
        long long size_exp = mod_exp(current->size, 3, MOD);
        
        // Compute log scale of ack_time
        double log_ack = log2(current->ack_time + 1);
        int scaled_ack = (int)(log_ack * 1000);
        
        // Push scaled ack to stack
        push(&ack_stack, scaled_ack);
        
        // Update cumulative checksum
        cumulative_checksum = (cumulative_checksum + size_exp) % MOD;
        
        current = current->next;
    }
    
    // Calculate final efficiency score
    int ack_sum = 0;
    while (ack_stack.top >= 0) {
        ack_sum += pop(&ack_stack);
    }
    
    // Final efficiency combines checksum and ack processing
    union {
        long long ll;
        int parts[2];
    } converter;
    converter.ll = cumulative_checksum;
    
    int final_efficiency_score = (converter.parts[0] ^ converter.parts[1]) + ack_sum;
    
    // Clean up linked list
    current = head;
    while (current != NULL) {
        PacketNode* temp = current;
        current = current->next;
        free(temp);
    }
    
    printf("Result: %d\n", final_efficiency_score);
    return 0;
}
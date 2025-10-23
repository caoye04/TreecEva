#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 101

typedef struct HashNode {
    int key;
    int count;
    struct HashNode* next;
} HashNode;

typedef struct LinkedListNode {
    int anomaly_count;
    struct LinkedListNode* next;
} LinkedListNode;

HashNode* hash_table[HASH_SIZE];

void init_hash() {
    for (int i = 0; i < HASH_SIZE; i++) {
        hash_table[i] = NULL;
    }
}

int hash(int key) {
    return abs(key) % HASH_SIZE;
}

void insert(int key) {
    int index = hash(key);
    HashNode* node = hash_table[index];
    while (node != NULL) {
        if (node->key == key) {
            node->count++;
            return;
        }
        node = node->next;
    }
    HashNode* new_node = (HashNode*)malloc(sizeof(HashNode));
    new_node->key = key;
    new_node->count = 1;
    new_node->next = hash_table[index];
    hash_table[index] = new_node;
}

int get_anomaly_count() {
    int count = 0;
    for (int i = 0; i < HASH_SIZE; i++) {
        HashNode* node = hash_table[i];
        while (node != NULL) {
            if (node->count > 2) count++;
            node = node->next;
        }
    }
    return count;
}

void clear_hash() {
    for (int i = 0; i < HASH_SIZE; i++) {
        HashNode* node = hash_table[i];
        while (node != NULL) {
            HashNode* temp = node;
            node = node->next;
            free(temp);
        }
        hash_table[i] = NULL;
    }
}

int main() {
    int device_readings[3][10] = {
        {10, 20, 10, 30, 10, 40, 50, 60, 70, 80},
        {5, 15, 25, 5, 35, 5, 45, 55, 65, 75},
        {100, 200, 100, 300, 400, 500, 600, 700, 800, 900}
    };
    
    LinkedListNode* head = NULL;
    int final_count = 0;
    
    for (int i = 0; i < 3; i++) {
        init_hash();
        for (int j = 0; j < 10; j++) {
            insert(device_readings[i][j]);
        }
        int anomaly_count = get_anomaly_count();
        LinkedListNode* new_node = (LinkedListNode*)malloc(sizeof(LinkedListNode));
        new_node->anomaly_count = anomaly_count;
        new_node->next = head;
        head = new_node;
        clear_hash();
    }
    
    LinkedListNode* current = head;
    while (current != NULL) {
        final_count += current->anomaly_count;
        LinkedListNode* temp = current;
        current = current->next;
        free(temp);
    }
    
    printf("Result: %d\n", final_count);
    return 0;
}
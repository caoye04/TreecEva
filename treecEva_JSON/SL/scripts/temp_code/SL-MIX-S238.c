#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_TABLE_SIZE 101

typedef struct Node {
    int block_id;
    int ref_count;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct {
    Node* head;
    Node* tail;
    int size;
} Queue;

typedef struct {
    Node* table[HASH_TABLE_SIZE];
} HashTable;

Node* create_node(int id) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->block_id = id;
    n->ref_count = 1;
    n->next = NULL;
    n->prev = NULL;
    return n;
}

Queue* create_queue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->head = NULL;
    q->tail = NULL;
    q->size = 0;
    return q;
}

HashTable* create_hash_table() {
    HashTable* ht = (HashTable*)malloc(sizeof(HashTable));
    memset(ht->table, 0, sizeof(ht->table));
    return ht;
}

int hash(int key) {
    return key % HASH_TABLE_SIZE;
}

void move_to_front(Queue* q, Node* n) {
    if (n == q->head) return;
    if (n == q->tail) q->tail = n->prev;
    if (n->next) n->next->prev = n->prev;
    if (n->prev) n->prev->next = n->next;
    n->next = q->head;
    n->prev = NULL;
    if (q->head) q->head->prev = n;
    q->head = n;
    if (!q->tail) q->tail = n;
}

void enqueue(Queue* q, Node* n) {
    if (q->head) q->head->prev = n;
    n->next = q->head;
    n->prev = NULL;
    q->head = n;
    if (!q->tail) q->tail = n;
    q->size++;
}

Node* dequeue(Queue* q) {
    if (!q->tail) return NULL;
    Node* n = q->tail;
    if (q->head == q->tail) {
        q->head = q->tail = NULL;
    } else {
        q->tail = n->prev;
        q->tail->next = NULL;
    }
    q->size--;
    return n;
}

void insert_hash(HashTable* ht, Node* n) {
    int index = hash(n->block_id);
    n->next = ht->table[index];
    ht->table[index] = n;
}

Node* find_hash(HashTable* ht, int id) {
    int index = hash(id);
    Node* current = ht->table[index];
    while (current) {
        if (current->block_id == id) return current;
        current = current->next;
    }
    return NULL;
}

int main() {
    Queue* access_queue = create_queue();
    HashTable* block_map = create_hash_table();
    int evicted_count = 0;
    int access_sequence[] = {10, 20, 30, 10, 40, 20, 50, 60, 30, 70, 80, 90};
    int seq_len = sizeof(access_sequence)/sizeof(access_sequence[0]);
    
    for (int i = 0; i < seq_len; i++) {
        int block_id = access_sequence[i];
        Node* block_node = find_hash(block_map, block_id);
        
        if (block_node) {
            block_node->ref_count++;
            move_to_front(access_queue, block_node);
        } else {
            block_node = create_node(block_id);
            enqueue(access_queue, block_node);
            insert_hash(block_map, block_node);
        }
        
        if (access_queue->size > 5) {
            Node* to_evict = dequeue(access_queue);
            if (to_evict && to_evict->ref_count < 3) {
                int index = hash(to_evict->block_id);
                Node** head = &(block_map->table[index]);
                while (*head && *head != to_evict)
                    head = &((*head)->next);
                if (*head)
                    *head = to_evict->next;
                free(to_evict);
                evicted_count++;
            } else if (to_evict) {
                enqueue(access_queue, to_evict);
            }
        }
    }
    
    printf("Result: %d\n", evicted_count);
    return 0;
}
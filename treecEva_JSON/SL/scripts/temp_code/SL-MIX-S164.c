#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 128
#define SIGNAL_COUNT 10

struct signal_entry {
    int signal_id;
    int count;
    struct signal_entry* next;
};

struct signal_stats {
    int total_signals;
    int unique_signals;
    double mean_count;
    int max_count;
};

union bit_mask {
    unsigned int full_mask;
    struct {
        unsigned int lower : 16;
        unsigned int upper : 16;
    } parts;
};

int hash_function(int key) {
    return (key * 2654435761U) % HASH_SIZE;
}

void insert_signal(struct signal_entry* hash_table[], int signal) {
    int index = hash_function(signal);
    struct signal_entry* entry = hash_table[index];
    
    while (entry != NULL) {
        if (entry->signal_id == signal) {
            entry->count++;
            return;
        }
        entry = entry->next;
    }
    
    struct signal_entry* new_entry = (struct signal_entry*)malloc(sizeof(struct signal_entry));
    new_entry->signal_id = signal;
    new_entry->count = 1;
    new_entry->next = hash_table[index];
    hash_table[index] = new_entry;
}

struct signal_stats calculate_stats(struct signal_entry* hash_table[]) {
    struct signal_stats stats = {0, 0, 0.0, 0};
    int total_count = 0;
    
    for (int i = 0; i < HASH_SIZE; i++) {
        struct signal_entry* entry = hash_table[i];
        while (entry != NULL) {
            stats.unique_signals++;
            total_count += entry->count;
            if (entry->count > stats.max_count) {
                stats.max_count = entry->count;
            }
            entry = entry->next;
        }
    }
    
    stats.total_signals = total_count;
    stats.mean_count = stats.unique_signals > 0 ? (double)total_count / stats.unique_signals : 0.0;
    return stats;
}

int main() {
    struct signal_entry* hash_table[HASH_SIZE] = {NULL};
    int signals[SIGNAL_COUNT] = {12, 45, 12, 67, 45, 12, 89, 45, 12, 34};
    
    // Process signals
    for (int i = 0; i < SIGNAL_COUNT; i++) {
        insert_signal(hash_table, signals[i]);
    }
    
    // Calculate statistics
    struct signal_stats stats = calculate_stats(hash_table);
    
    // Apply bit manipulation for anomaly detection
    union bit_mask mask;
    mask.full_mask = 0x00FF00FF;
    
    // Anomaly score calculation
    int variance_component = (stats.max_count - (int)stats.mean_count) * 10;
    int hash_collision_indicator = (stats.unique_signals & mask.parts.lower) > 0 ? 1 : 0;
    int anomaly_score = (variance_component > 5) ? 
                       (variance_component + hash_collision_indicator) : 
                       (stats.unique_signals ^ mask.parts.upper);
    
    // Clean up
    for (int i = 0; i < HASH_SIZE; i++) {
        struct signal_entry* entry = hash_table[i];
        while (entry != NULL) {
            struct signal_entry* temp = entry;
            entry = entry->next;
            free(temp);
        }
    }
    
    printf("Result: %d\n", anomaly_score);
    return 0;
}
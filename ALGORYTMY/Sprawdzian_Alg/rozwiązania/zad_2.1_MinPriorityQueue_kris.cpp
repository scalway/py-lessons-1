
#include <iostream>

#include <vector>
#include <algorithm>

class MinPriorityQueue {
private:
    std::vector<int> heap;
    
    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[index] < heap[parent]) {
                std::swap(heap[index], heap[parent]);
                index = parent;
            } else break;
        }
    }

    void heapifyDown(int index) {
        int size = heap.size();
        while (true) {
            int smallest = index;
            int left = 2 * index + 1;
            int right = 2 * index + 2;

            if (left < size && heap[left] < heap[smallest]) smallest = left;
            if (right < size && heap[right] < heap[smallest]) smallest = right;

            if (smallest != index) {
                std::swap(heap[index], heap[smallest]);
                index = smallest;
            } else break;
        }
    }

    void heapifyUpRecursive(int index) {
        if (index == 0) return;  // Warunek bazowy - dotarliśmy do korzenia
        
        int parent = (index - 1) / 2;
        if (heap[index] < heap[parent]) {
            std::swap(heap[index], heap[parent]);
            heapifyUpRecursive(parent);  // Rekurencyjne wywołanie
        }
    }

    void heapifyDownRecursive(int index) {
        int size = heap.size();
        int smallest = index;
        int left = 2 * index + 1;
        int right = 2 * index + 2;

        if (left < size && heap[left] < heap[smallest]) smallest = left;
        if (right < size && heap[right] < heap[smallest]) smallest = right;

        if (smallest != index) {
            std::swap(heap[index], heap[smallest]);
            heapifyDownRecursive(smallest);  // Rekurencyjne wywołanie
        }
    }

public:
    bool isEmpty() {
        return heap.empty();
    }

    void enqueue(int x) {
        heap.push_back(x);
        heapifyUp(heap.size() - 1);
    }

    int dequeue() {
        // Zakładamy, że kolejka nie jest pusta
        int minVal = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        
        if (!isEmpty()) {
            heapifyDown(0);
        }
        return minVal;
    }
};


int main() {
    MinPriorityQueue pq;
    pq.enqueue(5);
    pq.enqueue(3);
    pq.enqueue(8);
    pq.enqueue(1);

    while (!pq.isEmpty()) {
        std::cout << pq.dequeue() << " ";
    }
    // Output powinien być: 1 3 5 8
    return 0;
}
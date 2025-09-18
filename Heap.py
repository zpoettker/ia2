# Heap.py
# Homework – Heap Implementation
# Functions: find_left, find_right, find_parent, get_value, heapify, build_heap

class Heap:
    def __init__(self, arr=None):
        """Constructor: initialize heap array, build if given."""
        if arr is None:
            self.heap = []
        else:
            self.heap = arr[:]
            self.build_heap()

    def __del__(self):
        """Destructor."""
        del self.heap

    def find_left(self, i):
        """Return the index of the left child of node i."""
        left = 2 * i + 1
        if left < len(self.heap):
            return left
        return None

    def find_right(self, i):
        """Return the index of the right child of node i."""
        right = 2 * i + 2
        if right < len(self.heap):
            return right
        return None

    def find_parent(self, i):
        """Return the index of the parent of node i."""
        if i == 0:
            return None
        return (i - 1) // 2

    def get_value(self, i):
        """Return the value at index i in the heap."""
        if 0 <= i < len(self.heap):
            return self.heap[i]
        return None

    def heapify(self, i):
        """Maintain max-heap property starting from index i."""
        left = self.find_left(i)
        right = self.find_right(i)
        largest = i

        if left is not None and self.heap[left] > self.heap[largest]:
            largest = left
        if right is not None and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self):
        """Build a max-heap from the current list."""
        n = len(self.heap)
        for i in range((n // 2) - 1, -1, -1):
            self.heapify(i)

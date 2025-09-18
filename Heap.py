
class Heap:

    # Constructor
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr[:]
            self.build_heap()

    # Destructor
    def __del__(self):
        del self.heap  

    def find_left(self, i):
        left = 2 * i + 1
        if left < len(self.heap):  
            return left
        return None

    
    def find_right(self, i):
        right = 2 * i + 2
        if right < len(self.heap): 
            return right
            
        return None

    def find_parent(self, i):
        if i == 0:
            
            return None
            
        return (i - 1) // 2

    def get_value(self, i):
        if 0 <= i < len(self.heap):
            return self.heap[i]   
            
        return None

    def heap(self, i):
        left = self.find_left(i)
        right = self.find_right(i)
        largest = i

        if left is not None and self.heap[left] > self.heap[largest]: 
            largest = left
            
        if right is not None and self.heap[right] > self.heap[largest]: 
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heap(largest)  # heap function

    def build_heap(self):
        n = len(self.heap) 
        for i in range((n // 2) - 1, -1, -1):
            self.heap(i)  # heap function

    def extract_max(self):
        if len(self.heap) == 0:
            return None
            
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap(0)  # heap function
        
        return root

    def insert(self, value):
        self.heap.append(value) 
        i = len(self.heap) - 1
        
        while i > 0 and self.heap[self.find_parent(i)] < self.heap[i]:
            parent = self.find_parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def heap_sort(self):
        result = []
        while len(self.heap) > 0:
            result.insert(0, self.extract_max())
            
        return result

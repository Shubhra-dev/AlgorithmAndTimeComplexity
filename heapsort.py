class MinHeap:
    def __init__(self):
        self.heap = []
    
    def add(self, num):
        self.heap.append(num)
        self.swim(len(self.heap) - 1)
    
    def delete(self):
        if not self.heap:
            return None
        
        min_num = self.heap[0]
        
        if len(self.heap) == 1:
            self.heap = []
        else:
            self.heap[0] = self.heap.pop()
            self.sink(0)
        
        return min_num
    
    def build(self, arr):
        self.heap = arr
        for i in range(len(self.heap) // 2, -1, -1):
            self.sink(i)
    
    def heapify(self):
        for i in range(len(self.heap) - 1, -1, -1):
            self.sink(i)
    
    def swim(self, i):
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2
    
    def sink(self, i):
        while 2 * i + 1 < len(self.heap):
            j = 2 * i + 1
            if j + 1 < len(self.heap) and self.heap[j + 1] < self.heap[j]:
                j += 1
            if self.heap[j] >= self.heap[i]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
    
    def sort(self):
        sorted_arr = []
        while self.heap:
            sorted_arr.append(self.delete())
        return sorted_arr
    
    #main Function

if __name__ == '__main__':
    heap = MinHeap()
    with open('a.txt', 'r') as file:
        arr = [int(num) for num in file.read().split()]
    heap.build(arr)
    
    while True:
        # Input
        action = input("Enter 'A' to add a number, 'B' to delete, or 'S' to sort: ")
        if action == 'A':
            num = int(input("Enter a number to add to the heap: "))
            heap.add(num)
            print("Heap after adding:", heap.heap)
        elif action == 'B':
            num = heap.delete()
            if num is None:
                print("Heap is empty.")
            else:
                print("Deleted number:", num)
                print("Heap after deleting:", heap.heap)
        elif action == 'S':
            sorted_arr = heap.sort()
            print("Sorted array:", sorted_arr)
            break
        else:
            print("Invalid action. Please enter 'A', 'B', or 'S'.")

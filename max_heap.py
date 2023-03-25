class MaxHeap:
    def __init__(self):
        self.data = []

    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __gt__(self, other):
            return self.key > other.key 
    
    def parent(self, i):
        return (i-1)//2
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def has_left(self, i):
        return self.left(i) < len(self.data)
    
    def has_right(self, i):
        return self.right(i) < len(self.data)
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def up_heap(self, index):
        parent = self.parent(index)
        if index > 0 and self.data[index] > self.data[parent]:
            self.swap(index, parent)
            self.up_heap(parent)

    def add(self, key, value):
        self.data.append(self.Item(key, value))
        self.up_heap(len(self.data) - 1)

    def print_mx(self):
        for i in range(0, (len(self.data)//2)-1):
            print(
                f'parent = {self.data[i].key}, left_child = {self.data[2*i+1].key} right child = {self.data[2*i+2].key}'
            )

    def maximum(self):
        return self.data[0].key, self.data[0].value
    
    def down_mxheap(self, index):
        if self.has_left(index):
            left = self.left(index)
            largest = left
            if self.has_right(index):
                right = self.right(index)
                if self.data[right] > self.data[left]:
                    largest = right    
            if self.data[largest] > self.data[index]:
                self.swap(largest, index)
                self.down_mxheap(largest)


    def remove_mx(self):
        self.swap(0, len(self.data)-1)
        item = self.data.pop()
        self.down_mxheap(0)
        return item.key, item.value
    



mx = MaxHeap()
mx.add(15, 'K')
mx.add(9, 'F')
mx.add(7, 'Q')
mx.add(20, 'B')
mx.add(16, 'X')
mx.add(4, 'C')
mx.add(6, 'Z')
mx.add(12, 'H')
mx.add(11, 'S')
mx.add(25, 'J')
mx.add(14, 'E')
mx.add(8, 'W')
mx.add(5, 'A')
print(mx.maximum())


for i in range(len(mx.data)):
    print(mx.remove_mx())




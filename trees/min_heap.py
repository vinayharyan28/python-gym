class MinHeap:
    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
        
        def __lt__(self, other):
            return self.key < other.key 
        
    def __init__(self):
        self.data = []

    def parent(self, i):
        return (i-1)//2
    
    def left(self, i):
        return 2*i+1
    
    def right(self, i):
        return 2*i+2
    
    def has_left(self, i):
        return self.left(i) < len(self.data)
    
    def has_right(self, i):
        return self.right(i) < len(self.data)
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def up_heap(self, position):
        parent = self.parent(position)
        while position > 0 and self.data[position] < self.data[self.parent(position)]:
            self.swap(parent, position)
            self.up_heap(parent)


    def add(self, key, value):
        self.data.append(self.Item(key, value))
        self.up_heap(len(self.data)-1)

    def is_empty(self):
        return len(self.data) == 0

    def minimum(self):
        if self.is_empty():
            raise 'data is empty'
        item = self.data[0]
        return item.key, item.value
    
    def dowun_heap(self, index):
        if self.has_left(index):
            left = self.left(index)
            smallest = left
            if self.has_right(index):
                right = self.right(index)
                if self.data[right] < self.data[left]:
                    smallest = right
            if self.data[smallest] < self.data[index]:
                self.swap(smallest, index)
                self.dowun_heap(smallest)

    def print_heap(self):
        for i in range(0, len(self.data)//2):
            print(
                f'parent = {self.data[i].key}, left_child = {self.data[2*i+1].key} right child = {self.data[2*i+2].key}'
            )


    def remove_heap(self):
        self.swap(0, len(self.data)-1)
        item = self.data.pop()
        self.dowun_heap(0)
        return item.key, item.value
    
        

if __name__ == '__main__':
    m = MinHeap()
    m.add(15, 'K')
    m.add(9, 'F')
    m.add(7, 'Q')
    m.add(20, 'B')
    m.add(16, 'X')
    m.add(4, 'C')
    m.add(6, 'Z')
    m.add(12, 'H')
    m.add(11, 'S')
    m.add(25, 'J')
    m.add(14, 'E')
    m.add(8, 'W')
    m.add(5, 'A')

    m.print_heap()
    print(m.remove_heap())

    print(m.minimum())
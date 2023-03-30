class QuadraticProbing:
    def __init__(self, size=7):
        self.table = [None] * size
        self.size = size

    def _hash(self, key):
        return key % self.size

    def insert_key(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            self.table[hashed_key] = key 
        else:
            for i in range(self.size):
                hashed_key = self._hash(key)
                if self.table[hashed_key + i * i] is None:
                    self.table[hashed_key + i * i] = key 
                    break


if __name__ == '__main__':
    c = QuadraticProbing()
    c.insert_key(22)
    c.insert_key(30)
    c.insert_key(50)
    print(c.table)

    
        
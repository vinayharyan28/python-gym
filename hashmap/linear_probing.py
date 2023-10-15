class LinearProbing:
    def __init__(self, max_size=8):
        self.max_size = max_size
        self.table = [None] * self.max_size
        self.lenght = 0
        self.load_factor = 0.66

    def __len__(self):
        return len(self.table)
    
    def _hash(self, key):
        return key % len(self.table)
    
    def _increment(self, key):
        return (key + 1) % len(self.table)
    
    def resize(self):
        self.lenght = 0
        self.max_size *= 2
        old_table = self.table
        self.table = [None] * self.max_size
        for t in old_table:
            if t is not None:
                self[t[0]] = t[1]
    
    def __setitem__(self, key, value):
        self.lenght += 1
        hash_code = self._hash(key)
        while self.table[hash_code] is not None:
            if self.table[hash_code][0] == key:
                self.lenght -= 1
                break
            hash_code = self._increment(key)
        t = (key, value)
        self.table[hash_code] = t
        if self.lenght/len(self.table) >= self.load_factor:
            self.resize()

    def find_item(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        
        if self.table[hashed_key][0] != key:
            original_hashed_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self._increment(key)
                if self.table[hashed_key] is None:
                    raise KeyError('key not present')
                if original_hashed_key == hashed_key:
                    raise KeyError('key not present')
        return hashed_key


    def __getitem__(self, key):
        index = self.find_item(key)
        return self.table[index][1]
    
    def __delitem__(self, key):
        index = self.find_item(key)
        self.table[index] = None


if __name__ == '__main__':
    lp = LinearProbing(5)
    lp[50] = 100
    lp[70] = 400
    lp[76] = 200
    lp[93] = 300

    del lp[50]
    print(lp.table)

    # print(lp[50])
    print(lp[70])
    # print(lp[93])
    # print(lp[76])
class SeprateChaining:
    def __init__(self, capacity):
        self.hash_table = [[] for i in range(capacity)]

    def hashing(self, key):
        return key % len(self.hash_table)
    
    def insert(self, key, value):
        self.hash_table[self.hashing(key)].append(value)

    def delete_key(self, key, value):
        if self.hash_table[self.hashing(key)] is None:
            return
        else:
            self.hash_table[self.hashing(key)].remove(value)


    def print_hash_table(self):
        for i in range(len(self.hash_table)):
            print(i, end=' ')
            for j in self.hash_table[i]:
                print('-----> ', j, end=' ')
            print()


s = SeprateChaining(5)
# s.print_hash_table()
s.insert(10, 'vinay')
s.insert(10, 'haryan')
s.insert(2, 'mumbai')
s.insert(22, 'lower parel')
s.insert(28, 'paral')
s.print_hash_table()
s.delete_key(10, 'haryan')

print(s.hash_table)
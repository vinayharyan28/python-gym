class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, insert_word):
        temp = self.root
        for char in insert_word:
            index = ord(char) - ord('a')
            if temp.children[index] is None:
                temp.children[index] = Node()
            temp = temp.children[index]
        temp.end_of_word = True

    def search(self, key):
        temp = self.root
        for char in key:
            index = ord(char) - ord('a')
            node = temp.children[index]
            if node is None:
                return False
            temp = node

        return temp is not None and temp.end_of_word


if __name__ == '__main__':
    words = ["the", "a", "there", "their", "any"]
    trie = Trie()

    for word in words:
        trie.insert(word)

    print(trie.search("their"))
    print(trie.search("thor"))
    print(trie.search("there"))
    print(trie.search("an"))
    print(trie.search("any"))



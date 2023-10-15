tree = [None] * 10


def root(key):
    if tree[0] is not None:
        print('the tree already had root')
    else:
        tree[0] = key


def set_left(key, parent):
    if tree[parent] is None:
        print("Can't set child at ", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 1] = key


def set_right(key, parent):
    if tree[parent] is None:
        print("Can't set child at ", (parent * 2) + 2, ", no parent found")

    else:
        tree[(parent * 2) + 2] = key


def print_tree():
    for i in range(10):
        if tree[i] is not None:
            print(tree[i], end=' ')
        else:
            print('-', end=' ')


root('A')
set_left('B', 0)
set_right('C', 0)
# set_left('D', 1)
print_tree()


class LinkedBinaryTree:
    class Node:
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position:
        """ An abstraction representing the location of a single element"""
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element_(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')
        return p.node

    def make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def root_(self):
        return self.make_position(self.root)

    def parent(self, p):
        node = self.validate(p)
        return self.make_position(node.parent)

    def left(self, p):
        node = self.validate(p)
        return self.make_position(node.left)

    def right(self, p):
        node = self.validate(p)
        return self.make_position(node.right)

    def num_children(self, p):
        node = self.validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def add_root(self, e):
        if self.root is not None:
            raise ValueError('Root exits')
        self.size += 1
        self.root = self.Node(e)
        return self.make_position(self.root)

    def add_left(self, p, e):
        node = self.validate(p)
        if node.left is not None:
            raise ValueError('Left child exists')
        self.size += 1
        node.left = self.Node(e, node)
        return self.make_position(node.left)

    def add_right(self, p, e):
        node = self.validate(p)
        if node.right is not None:
            raise ValueError('Right child exist')
        self.size += 1
        node.right = self.Node(e, node)
        return self.make_position(node.right)

    def replace(self, p, e):
        node = self.validate(p)
        old = node.element
        node.element = e
        return old

    def delete(self, p):
        node = self.validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self.root:
            self.root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node
        return node.element

    def is_root(self, p):
        """Return True if position p represents the root of the tree"""
        return self.root_() == p

    def is_leaf(self, p):
        """Return True if position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self.subtree_preorder(c):
                yield other

    def preorder(self):
        if not self.is_empty():
            for sp in self.subtree_preorder(self.root_()):
                yield sp

    def position(self):
        return self.preorder()

    def __iter__(self):
        for p in self.position():
            yield p.element_()

    def depth(self, p):
        """Return the number of levels separating position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height1(self):
        """Return the height of the tree"""
        return max(self.depth(p) for p in self.position() if self.is_leaf(p))

    def height2(self):
        """Return the height of the subtree rooted at position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self.height2(p)

    def attach(self, p, t1, t2):
        node = self.validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self.size += len(t1) + len(t2)
        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.is_empty():
            t2.root.parent = node
            node.right = t2.root
            t2.root = None
            t2.size = 0




linked_b = LinkedBinaryTree()
linked_b.add_root(1)
p = linked_b.make_position(linked_b.root)
l = linked_b.add_left(p, 2)

for p in linked_b.preorder():
    print(p.element_())

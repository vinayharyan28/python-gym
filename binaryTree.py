class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def preorder(self, root):
        if root is not None:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    @staticmethod
    def insert_tree(root, value):
        if root is None:
            root = TreeNode(value)
            return
        else:
            q = [root]
            while len(q):
                temp_node = q[0]
                q.pop(0)
                if temp_node.left is None:
                    temp_node.left = TreeNode(value)
                    break
                else:
                    q.append(temp_node.left)
                if temp_node.right is None:
                    temp_node.right = TreeNode(value)
                    break
                else:
                    q.append(temp_node.right)


    @staticmethod
    def deletion(root, value):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.data == value:
                return None
            else:
                return root
            
        q = [root]
        while len(q):
            temp_node = q.pop(0)
            
            if temp_node.data == value:
                result_node = temp_node
            if temp_node.left is not None:
                last = temp_node
                q.append(temp_node.left)
            if temp_node.right is not None:
                last = temp_node
                q.append(temp_node.right)
        if result_node is not None:
            result_node.data = temp_node.data
            if last.right is not None:
                last.right = None
            else:
                last.left = None

        return root


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
tt = Tree()

tt.insert_tree(t, 7)
tt.insert_tree(t, 8)
tt.preorder(t)
print('\n')
tt.deletion(t, 3)

tt.preorder(t)




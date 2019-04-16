class treeNode:
    def __init__(self, key = None, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class TreeClass:
    def __init__(self, preset = 0):
        self._populate_tree(preset)

    # Functions to implement for the partial exam
    def __str__(self):
        self._print_preorder_recur(self.root)
        print("")
        self._print_inorder_recur(self.root)
        print("")
        self._print_postorder_recur(self.root)
        print("")

    def __setitem__(self, key, data):
        tmpNode = self._find_node(self.root, key)
        if tmpNode == None:
            return
        else:
            tmpNode.data = data
    
    def __getitem__(self, key):
        tmpNode = self._find_node(self.root, key)
        if tmpNode == None:
            return None
        else:
            return tmpNode
    
    # Helper Functions
    def _populate_tree(self, preset):
        if preset == 1:
            self.root = treeNode(5, 5, treeNode(2, 2, treeNode(1, 1), treeNode(4, 4)), treeNode(8, 8, treeNode(7, 7), treeNode(9, 9)))
        elif preset == 2:
            self.root = treeNode("c", "c", treeNode("a", "a", None, treeNode("b", "b")), treeNode("e", "e", treeNode("d", "d"), treeNode("f","f")))
        elif preset == 3:
            self.root = treeNode(20, 20, treeNode(13, 13, treeNode(8, 8), treeNode(15, 15)), treeNode(27, 27, treeNode(21, 21), None))
        else:
            self.root = treeNode()

    def _print_preorder_recur(self, node):
        if node == None:
            return
        print(str(node.data), end = " ")
        self._print_preorder_recur(node.left)
        self._print_preorder_recur(node.right)

    def _print_inorder_recur(self, node):
        if node == None:
            return
        self._print_inorder_recur(node.left)
        print(str(node.data), end = " ")
        self._print_inorder_recur(node.right)
    
    def _print_postorder_recur(self, node):
        if node == None:
            return
        self._print_postorder_recur(node.left)
        self._print_postorder_recur(node.right)
        print(str(node.data), end = " ")

    def _find_node(self, node, key):
        # Checks if the tree is empty or if you have walked all the tree and still not found the node
        if node == None:
            return None
        # If the function has found the key, return the node    
        elif node.key == key:
            return node
        # if the node has left child
        elif node.left != None:
            return self._find_node(node.left, key)
        # if the node has no left child but has a right child
        elif node.left == None and node.right != None:
            return self._find_node(node.right, key)

class HashClass:
    def __init__(self, preset = 0):
        self._size = 16
        self.hashmap = [[] for _ in range(self._size)]

    # Functions to implement for the partial exam
    def __setitem__(self, key, data):
        pass
    
    def __getitem__(self, key):
        pass

    # Helper functions

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    h = HashClass()
    h = HashClass(1)

    t = TreeClass()
    t = TreeClass(1)
    print(t)

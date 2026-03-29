RED = True
BLACK = False

class LLRBNode:
    def __init__(self, key, colour=RED):
        self.key = key
        self.left = None
        self.right = None
        self.colour = colour

class LLRBBST(AbstractSearchInterface):

    def __init__(self):
        self.root = None

    def get(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.get(node.left, key)
        else:
            return self.get(node.right, key)

    def isRed(self, node):
        if node is None:
            return False
        return node.colour == RED

    def rotLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.colour = node.colour
        node.colour = RED
        return x

    def rotRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.colour = node.colour
        node.colour = RED
        return x

    def flipColour(self, node):
        node.colour = RED
        node.left.colour = BLACK
        node.right.colour = BLACK

    def put(self, node, key):
        if node is None:
            return LLRBNode(key, colour=RED)

        if key < node.key:
            node.left = self.put(node.left, key)
        elif key > node.key:
            node.right = self.put(node.right, key)
        else:
            return node

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotLeft(node)

        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotRight(node)

        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColour(node)

        return node

    def searchElement(self, element):
        return self.get(self.root, element)

    def insertElement(self, element):
        if self.searchElement(element):
            return False

        self.root = self.put(self.root, element)
        self.root.colour = BLACK

        return True
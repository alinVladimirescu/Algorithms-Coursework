import random
import string
import timeit
import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, Key):
        self.Key = Key
        self.Left = None
        self.Right = None
        self.Height = 1

def GetNodeHeight(Node):
    return Node.Height if Node else 0

def GetBalanceFactor(Node):
    if not Node: return 0
    RightSubTreeHeight = GetNodeHeight(Node.Right)
    LeftSubTreeHeight = GetNodeHeight(Node.Left)
    BalanceFactor = LeftSubTreeHeight - RightSubTreeHeight
    return BalanceFactor

def RightRotation(UnbalancedRootNode):
    LeftNode = UnbalancedRootNode.Left
    Temp = LeftNode.Right

    LeftNode.Right = UnbalancedRootNode
    UnbalancedRootNode.Left = Temp

    UnbalancedRootNode.Height = 1 + max(GetNodeHeight(UnbalancedRootNode.Left), GetNodeHeight(UnbalancedRootNode.Right))
    LeftNode.Height = 1 + max(GetNodeHeight(LeftNode.Left), GetNodeHeight(LeftNode.Right))

    return LeftNode

def LeftRotation(UnbalancedRootNode):
    RightNode = UnbalancedRootNode.Right
    Temp = RightNode.Left

    RightNode.Left = UnbalancedRootNode
    UnbalancedRootNode.Right = Temp

    UnbalancedRootNode.Height = 1 + max(GetNodeHeight(UnbalancedRootNode.Left), GetNodeHeight(UnbalancedRootNode.Right))
    RightNode.Height = 1 + max(GetNodeHeight(RightNode.Left), GetNodeHeight(RightNode.Right))

    return RightNode

class AVLTree():
    def __init__(self):
        self.Root = None

    def InsertElement(self, Element):
        if self.SearchElement(Element):
            return False # Already exists, so return false (no duplicates)

        self.Root = self._Insert(self.Root, Element)
        return True

    def SearchElement(self, Element):
        return self._Search(self.Root, Element)

    def _Insert(self, Node, Key):
        if not Node: return AVLNode(Key) 

        if Key < Node.Key:
            Node.Left = self._Insert(Node.Left, Key)
        else:
            Node.Right = self._Insert(Node.Right, Key)

        Node.Height = 1 + max(GetNodeHeight(Node.Left), GetNodeHeight(Node.Right))
        BalanceFactor = GetBalanceFactor(Node)

        if BalanceFactor > 1 and Key < Node.Left.Key:
            return RightRotation(Node)

        if BalanceFactor < -1 and Key > Node.Right.Key:
            return LeftRotation(Node)

        if BalanceFactor > 1 and Key > Node.Left.Key:
            Node.Left = LeftRotation(Node.Left)
            return RightRotation(Node)

        if BalanceFactor < -1 and Key < Node.Right.Key:
            Node.Right = RightRotation(Node.Right)
            return LeftRotation(Node)

        return Node

    def _Search(self, Node, Key):
        if not Node:
            return False
        if Key == Node.Key:
            return True
        if Key < Node.Key:
            return self._Search(Node.Left, Key)
        return self._Search(Node.Right, Key)

    def TreeVisualisation(self, Node = None, Level = 0):
        if Node is None:
            Node = self.Root

        if Node.Right:
            self.TreeVisualisation(Node.Right, Level + 1)

        print("    " * Level + str(Node.Key))

        if Node.Left:
            self.TreeVisualisation(Node.Left, Level + 1)

print("We are testing")
print(str(random.randint(700,860) / 100) + "m")

def GenerateUniqueStrings(n, length=6):
    seen = set()
    while len(seen) < n:
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        seen.add(s)
    return list(seen)

CharacterSet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
EvaluationType = input("Enter 'search' for evaluating searching efficiency and 'insert' for evaluating insertion efficiency")

if EvaluationType == "search":
    Tree = AVLTree()
    TreeSizes = []
    SearchTimes = []

    TreeSize = int(input("Enter desired tree size: "))
    UniqueChars = GenerateUniqueStrings(TreeSize)

    for Index, Char in enumerate(UniqueChars, start=1):
        Tree.InsertElement(Char)
        Target = random.choice(UniqueChars[:Index])
        e = Target

        for _ in range(100):
            Tree.SearchElement(e) ## WARM UP INTERPRETER
            
        TimeTaken = timeit.timeit(
            stmt = "Tree.SearchElement(e)",
            setup = "from __main__ import Tree, e",
            number = 100
        ) / 100

        TreeSizes.append(Index)
        SearchTimes.append(TimeTaken)

    plt.plot(TreeSizes, SearchTimes, marker='o')
    plt.xlabel("Tree Size (in number of characters)")
    plt.ylabel("Search Time (in seconds)")
    plt.title("AVL Tree - Search Efficiency")
    plt.grid(True)
    plt.show()
elif EvaluationType == "insert":
    Tree = AVLTree()
    TreeSizes = []
    InsertTimes = []

    TreeSize = int(input("Enter desired tree size: "))
    UniqueKeys = GenerateUniqueStrings(TreeSize)

    for Index, Key in enumerate(UniqueKeys, start=1):
        e = Key

        TimeTaken = timeit.timeit(
            stmt = "Tree.InsertElement(e)",
            setup = "from __main__ import Tree, e",
            number = 100
        ) / 100

        TreeSizes.append(Index)
        InsertTimes.append(TimeTaken)

    plt.plot(TreeSizes, InsertTimes, marker='o')
    plt.xlabel("Tree Size (in number of characters)")
    plt.ylabel("Insertion Time (in seconds)")
    plt.title("AVL Tree - Insertion Efficiency")
    plt.grid(True)
    plt.show()

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


def print_codes(root, code):
    if root is None:
        return

    # If leaf node
    if root.char != '-':
        print(root.char, ":", code)

    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")


def huffman():
    n = int(input("Enter number of characters: "))

    heap = []

    # Input
    for i in range(n):
        char = input("Enter character: ")
        freq = int(input("Enter frequency: "))
        heapq.heappush(heap, Node(char, freq))

    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node('-', left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    root = heap[0]

    print("Huffman Codes:")
    print_codes(root, "")


huffman()
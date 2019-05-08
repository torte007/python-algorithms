class BTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right



# Multiway tree class (a tree with multiple children)

class MTree:
    def __inti__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next

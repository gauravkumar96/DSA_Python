

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


newbt = TreeNode('Drinks')
leftchild = TreeNode('Hot')
leftchild1 = TreeNode('Cola')
leftchild2 = TreeNode('Fanta')
rightchild = TreeNode('Cold')
rightchild1 = TreeNode('Tea')
rightchild2 = TreeNode('Coffee')



newbt.leftchild = leftchild
newbt.rightchild = rightchild

rightchild.rightchild = leftchild1
rightchild.leftchild = leftchild2

leftchild.leftchild = rightchild1
leftchild.rightchild = rightchild2


def preorderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorderTraversal(rootnode.leftchild)
    preorderTraversal(rootnode.rightchild)


preorderTraversal(newbt)
        
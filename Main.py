  
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    if (root == None):
        root = BinaryTreeNode(new_value)
        return root
    else:
        if root.data > new_value:
            if root.left_child is None:
                new_node = BinaryTreeNode(new_value)
                root.left_child = new_node
            else:
                insert(root.left_child,new_value)

        else:
            if root.right_child is None:
                new_node = BinaryTreeNode(new_value)
                root.right_child = new_node
            else:
                insert(root.right_child,new_value)

def inorder(root) -> None:
    if root:
        inorder(root.left_child)
        print(root.data, end = " ")
        inorder(root.right_child)


def preorder(root) -> None:
    if root:
        print(root.data, end = " ")
        preorder(root.left_child)
        preorder(root.right_child)


def postorder(root) -> None:
    if root:
        postorder(root.left_child)
        postorder(root.right_child)
        print(root.data, end = " ")

input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)

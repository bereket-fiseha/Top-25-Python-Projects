from collections import deque

class TreeNode:
    data=None
    left=None
    right=None
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class BinaryTree:
     def __init__(self,root=None):
              self.root=root

     def insert(self,data):
         new_node=TreeNode(data)
         if not self.root:
            print("in")
            self.root=new_node
         else:
            que=deque()
            que.append(self.root)
            while len(que)>0:
                 t_node=que.popleft()
                 if t_node.left:
                      que.append(t_node.left)
                 else:
                    t_node.left=new_node
                    break
                 if t_node.right:
                      que.append(t_node.right)
                 else:
                    t_node.right=new_node 
                    break

     def in_order_traversal(self,root):
          
            if root.left:
              self.in_order_traversal(root.left)
            print(root.data)         
            if root.right:
              self.in_order_traversal(root.right)
     def remove(self,data):
         pass
     def build(self,arr:list):
         pass
                  

if __name__=="__main__":
     tree=BinaryTree()
     tree.insert(5)
     tree.insert(4)
     tree.insert(6)
     tree.insert(7)
     tree.insert(1)
     tree.pre_order_traversal(tree.root)    
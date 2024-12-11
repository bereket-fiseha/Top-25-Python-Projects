class Node:
   def __init__(self,val=None,next=None):
     self.val=val
     self.next=next

class LinkedList:
    def __init__(self,head:Node=None):
        self.head=head 
    def insert_front(self,data):
      self.head=Node(data,self.head)
     
     
    def append(self,data)->None:
         if not self.head:
             self.head=Node(data)
         else:
              itr=self.head
              while itr.next:
                itr=itr.next
              itr.next=Node(data) 
    def insert_at(self,data,index:int)->None:
       pass
    def remove_at(self,index:int)->None:
       pass
           
    def __str__(self)->str:
        itr=self.head
        res=""
        while itr:
           res+=f"{itr.val}-->"
           itr=itr.next
        return res   
if __name__=="__main__":
  ll=LinkedList()
  ll.append(5)
  ll.append(6)
  ll.insert_front(9)
  print(str(ll))

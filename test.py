class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
 def __init__(self):
     self.head = None

 def listprint(self):
     printval = self.head
     while printval is not None:
         print (printval.data)
         printval = printval.next

 def insert(self,data):
     new_node = Node(data)
     new_node.next = self.head
     self.head = new_node

list = LinkedList()
#list.head = Node("Mon")
#e2 = Node("Tue")
#e3 = Node("Wed")
#
## Link first Node to second node
#list.head.next = e2
#
## Link second Node to third node
#e2.next = e3

list.insert("Mon")
list.insert("Tue")
list.insert("Wed")
list.listprint()

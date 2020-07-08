class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def delete(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def count(self):
        current = self.head
        count = 0
        while (current):
            current = current.next
            count += 1
        return count

    def reverse(self):
        prev = None
        current = self.head
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


list = LinkedList()
list.insert_start("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list.head.next = e2
e2.next = e3
list.insert_end("Thu")
list.reverse()
list.printlist()
print(list.count())

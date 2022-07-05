class Node:

# Constructor to initialize the node object
  def __init__(self, name):
    self.name = name
    self.next = None

class LinkedList:

#this function is for initialize head
  def __init__(self):
    self.head = None

#this function is to sort the name
  def sortedInsert(self, new_node):
    
    if self.head is None:
      new_node.next = self.head
      self.head = new_node

    elif self.head.name >= new_node.name:
      new_node.next = self.head
      self.head = new_node

    else :
        current = self.head
        while(current.next is not None and
        current.next.name < new_node.name):
            current = current.next
      
        new_node.next = current.next
        current.next = new_node

#this function is for insert a new node at the beginning
  def push(self, name):
    new_node = Node(name)
    new_node.next = self.head
    self.head = new_node

#this function to print the LinkedList
  def printList(self):
    temp = self.head
    while(temp):
      print(temp.name)
      temp = temp.next

llist = LinkedList()
new_node = Node("vda")
llist.sortedInsert(new_node)
new_node = Node("priya")
llist.sortedInsert(new_node)
new_node = Node("divya")
llist.sortedInsert(new_node)
new_node = Node("vijet")
llist.sortedInsert(new_node)
new_node = Node("anusha")
llist.sortedInsert(new_node)
new_node = Node("akshatha")
llist.sortedInsert(new_node)
new_node = Node("sada")
llist.sortedInsert(new_node)
new_node = Node("praveen")
llist.sortedInsert(new_node)
new_node = Node("suhas")
llist.sortedInsert(new_node)
new_node = Node("atharava")
llist.sortedInsert(new_node)
llist.printList()


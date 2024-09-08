

## Prepend -> add a linked list at the begining of the linked list

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next 

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True

  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while temp.next:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp.value

  def prepend(self,value):
    new_node = Node(value)
    if self.length == 0:
      self.head == new_node
      self.tail == new_node
    else:
      new_node.next = self.head
      self.head = new_node
      self.length += 1
      return True

  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp.value

  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def set_value(self, index, value):
    temp = self.get(index)
    if temp:  # If a valid node is returned
      temp.value = value
      return True
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()

  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None


l1 = LinkedList(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
l1.print_list()
l1.pop()
l1.print_list()
l1.prepend(0)
l1.print_list()
l1.pop_first()
l1.print_list()
l1.get(2)
l1.set_value(2,10)
l1.print_list()
l1.insert(0,0)
l1.print_list()
l1.remove(0)
l1.print_list()
l1.reverse()
l1.print_list()
-----------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1




my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""

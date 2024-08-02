class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Sll:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        l = []    
        trav = self.__head
        while trav is not None:
            l.append(str(trav.data))
            trav = trav.next

        return "<---->".join(l)
    
    def insert(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node 
            self.__tail = new_node
        self.__size += 1

    def delete_random(self,index):
        if (index < 0) or (index >= self.__size):
            raise Exception("index out of range")
        elif (index == 0):
            return self.remove_first()
        elif (index == self.__size - 1):
            return self.remove_last()
        else:
            i = 0
            trav = self.__head
            while i != (index - 1):
                i += 1
                trav = trav.next
            temp = trav.next
            trav.next = trav.next.next
            del temp                    

    def size(self):
        return self.__size
    
    def is_empty(self):
        return self.size() == 0
    
    def rotate_right(self, k):
        if self.__head is None or k == 0:
            return
        length = self.__size
        k = k % length
        if k == 0:
            return
        for _ in range(k):
            current = self.__head
            while current.next.next:  
                current = current.next
            new__head = current.next
            current.next = None
            new__head.next = self.__head
            self.__head = new__head  

    def reverse(self):
        prev = None
        current = self.__head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev              
    
    def append_last(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.next = None
            self.__tail = new_node
            self.__size += 1

    
    def prepend(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__size += 1 

    def merge(self, other):
        if not self.__head:
            self.__head = other.head
            return
        current = self.__head
        while current.next:
            current = current.next
        current.next = other.head
        current = self.__head
        while current.next:
            current = current.next
            traversal = self.__head
            while traversal != current:
                traversal = traversal.next

    def interleave(self, other):
        p1 = self.__head
        p2 = other.head
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
            traversal = self.__head
            while traversal and traversal != p1 and traversal != p2:
                traversal = traversal.next                

    def middle_element(self):
        slow_pointer = self.__head
        fast_pointer = self.__head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data 
    
    def index_of(self, data):
        current = self.__head
        index = 0
        while current:
            inner_current = self.__head
            while inner_current != current:
                inner_current = inner_current.next
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1    

    def split_index(self, index):
        if index < 0:
            raise Exception("Index out of bounds")
        if index == 0:
            new_list = Sll()
            new_list.head = self.__head
            self.__head = None
            return new_list
        current = self.__head
        for _ in range(index - 1):
            if current is None:
                raise Exception("Index out of bounds")
            current = current.next
        if current is None:
            raise Exception("Index out of bounds")
        new_list = Sll()
        new_list.head = current.next
        current.next = None
        traversal = self.__head
        while traversal:
            traversal = traversal.next
        return new_list





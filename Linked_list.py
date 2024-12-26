class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self):
        if self.head == None :
            return 'list is empty'
        else :
            curr = self.head
            result = ''
            while(curr != None):
                result = result + str(curr.data) + ' --> '
                curr = curr.next
            return result[:-5]

    def insert_head(self,value):    
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def insert_after(self,pos,value):
        curr = self.head
        while(curr != None):
            if curr.data == pos:
                break
            curr = curr.next
        if curr != None:
            new_node = Node(value)
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Value Error - data not found'
        
    def append(self,value):
        new_node = Node(value)
        if self.head == None :
            self.head = new_node
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = new_node
        self.n += 1
    
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None :
            return 'list is empty'
        self.head = self.head.next
        self.n -= 1

    def remove(self,value):
        if self.head.data == value :
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr != None :
            curr.next = curr.next.next
            return
        return 'ValueError - value not found'

    def pop(self):
        if self.head == None :
            return 'list is empty'
        curr = self.head
        if curr.next == None :
            return self.delete_head()
        while(curr.next.next != None):
            curr = curr.next
        curr.next = None
        self.n -= 1

    def search(self,value):
        curr = self.head
        pos = 0
        while(curr != None):
            if curr.data == value:
                return pos 
            curr = curr.next
            pos += 1
        return 'ValueError - value not found'
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None :
            if pos == index :
                return curr.data
            curr = curr.next
            pos += 1
        return 'IndexError - index out of bounds'
    
    def __delitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError('IndexError-Index out of bounds')
        if index == 0:
            return self.delete_head()
        curr = self.head
        prev = None
        pos = 0
        while curr and pos < index:
            prev = curr
            curr = curr.next
            pos += 1
        
        if curr:
            prev.next = curr.next
            self.n -= 1

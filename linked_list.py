#!/Users/pwu/anaconda/bin/python3
""" shebang for linux /usr/bin/env python3
this file contains a python linked list implementation
"""


class node:
    """ this is the node class definition
    """
    def __init__(self, data):
        """initialize the node object
        """
        self.data = data
        self.next = None


class linkedList:
    """ this is the linked list
    """

    def __init__(self, node=None):
        """initilialize the head of this linked list
        """
        self.head = node 

    def addNodeHead(self, data):
        """adds new node to head of list
        """
        nn = node(data)
        if self.head is not None:
            nn.next = self.head
        self.head = nn
            
    def addNodeTail(self, data):
        """add node to tail of list
        """
        nn = node(data)
        if self.head is None:
            self.head = nn
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = nn

    def removeNodeHead(self):
        """remove node from head of list
        """
        if self.head is not None:
            self.head = self.head.next

    def removeNodeTail(self):
        """remove node from tail of list
        """
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                return
            prev = None
            n = self.head
            while n.next is not None:
                prev = n
                n = n.next
            prev.next = None
                
    def removeNodeAtIndex(this, idx):
        """remove node at index value
        """
        if this.head is not None:
            prev = None
            n = this.head
            tIdx = 0
            while n is not None and tIdx < idx:
                prev = n
                n = n.next
                tIdx += 1
            if n is None:
                print("error: index out of range")
            else:
                prev.next = n.next
            
    def printLinkedList(this):
        """ prints out the linked list
        """
        if this.head is not None:
            n = this.head
            print("start")
            while n is not None:
                print(n.data)
                n = n.next
            print("end")


def mergeSortedList(l1, l2):
    """ merge 2 sorted linked list into a new one
    """
    newHead = None
    if l1 is None and l2 is None: 
        return None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data < l2.data:
        newHead = l1
        l1 = l1.next
    else:
        newHead = l2
        l2 = l2.next
    mover = newHead
    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            mover.next = l1
            mover = l1
            l1 = l1.next
        else:
            mover.next = l2
            mover = l2
            l2 = l2.next
    while l1 is not None:
        mover.next = l1
        mover = l1
        l1 = l1.next
    while l2 is not None:
        mover.next = l2
        mover = l2
        l2 = l2.next
    return newHead
            

if __name__ == '__main__':
    ll = linkedList()
    print("add 5 at head")
    ll.addNodeHead(5)
    ll.printLinkedList()
    print("remove head")
    ll.removeNodeHead()
    ll.printLinkedList()
    print("add 6 at tail")
    ll.addNodeTail(6)
    ll.printLinkedList()
    print("remove tail")
    ll.removeNodeTail()
    ll.printLinkedList()
    print("add bunch values head and tail")
    ll.addNodeHead(4)
    ll.addNodeTail(7)
    ll.addNodeHead(3)
    ll.addNodeTail(8)
    ll.addNodeTail(9)
    ll.addNodeTail(10)
    ll.addNodeHead(0)
    ll.printLinkedList()
    print("removing index 1")
    ll.removeNodeAtIndex(1)
    ll.printLinkedList()
    print("remove out of index value")
    ll.removeNodeAtIndex(50)
    ll.printLinkedList()
    ll2 = linkedList()
    ll2.addNodeHead(21)
    ll2.addNodeHead(16)
    ll2.addNodeHead(13)
    ll2.addNodeHead(9)
    ll2.addNodeHead(8)
    ll2.addNodeHead(2)
    ll2.printLinkedList()
    print("merging 2 lists")
    ll3 = linkedList(mergeSortedList(ll.head, ll2.head))
    ll3.printLinkedList()
            





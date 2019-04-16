
class DataClass:
    # USE THIS IMPLEMENTATION OF DATACLASS UNCHANGED
    def __init__(self, x_type, x_information):
        self.x_type = x_type
        self.x_information = x_information
    def __str__(self):
        return "{" + str(self.x_type) + ": " + str(self.x_information) + "}"

class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

class DataList:
    class Node:
        def __init__(self, data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, value):
        new_Node = self.Node(value, self.head.next, self.head)
        self.head.next = new_Node
        return new_Node
    
    def add_to_back(self, value):
        new_Node = self.Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = new_Node
        self.tail.prev = new_Node
        return new_Node

    
    def __str__(self):
        return self.traverse(self.head)

    def traverse(self, node):
        retrn = ""
        if node.next.data != None:
            retrn += str(node.next.data) + " " + str(self.traverse(node.next))
        return retrn        

# Questions Part 1 of Exam2
def count_value(head, value):
    if head == None:
        return 0
    if head.data == value:
        return 1 + count_value(head.next, value)
    return count_value(head.next, value)

def contains_all(head1, head2):
    if head1 == None or head2 == None:
        return False
    if head1 == None and head2 == None:
        return True
    if head1.data == head2.data:
        return contains_all(head1.next, head2.next)
    if head1.data != head2.data:
        search = find_value(head1.data, head2.next)
        if search != True:
            return False
        return contains_all(head1.next, head2)

    return contains_all(head1.next, head2.next)

def find_value(value, head):
    if head == None:
        return False
    if head.data == value:
        return True
    if head.data != value:
        return find_value(value, head.next)

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("DataClass example:")
    dc = DataClass(2, "A string with some information for type 2")
    print(str(dc))
    dc = DataClass(3, "A string with information for type 3 DataClass")
    print(str(dc))
    dc = DataClass(2, "More information for a type 2 D.C.")
    print(str(dc))

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(4, SLL_Node(5)))))
    print(str(head))
    print("list: " + str(head))
    print("# of 1: " + str(count_value(head, 1)))
    print("# of 3: " + str(count_value(head, 3)))

    print("\nTesting Contains_all")
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(5))))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(1)))
    head3 = SLL_Node(5, SLL_Node(2, SLL_Node(3)))
    head4 = SLL_Node(6, SLL_Node(1, SLL_Node(3)))
    print("{" + str(head1) + "} contains all in {" + str(head2)+ "}: " +str(contains_all(head1,head2)))
    print("{" + str(head1) + "} contains all in {" + str(head3)+ "}: " +str(contains_all(head1,head3)))
    print("{" + str(head1) + "} contains all in {" + str(head4)+ "}: " +str(contains_all(head1,head4)))

    print("\nTesting Datalist")
    dl = DataList()
    dl.add_to_back(1)
    dl.add_to_back(2)
    dl.add_to_back(3)
    print("dl: " + str(dl))
    dl.add_to_front(4)
    dl.add_to_front(5)
    dl.add_to_front(6)
    print("dl: " + str(dl))
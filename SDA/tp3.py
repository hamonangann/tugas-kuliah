from __future__ import annotations

"""
List of these operations:
    - Append other node in front of this node
    - Remove other node in front of this node

Commands:
    INSERT_HEAD [VALUE]
    REMOVE_HEAD
    
    INSERT_TAIL [VALUE]
    REMOVE_TAIL
    
    INSERT_NODE_USING_POINTER [DIREKSI] [VALUE]
    REMOVE_NODE_USING_POINTER [DIREKSI]
    MOVE_POINTER [DIREKSI] [VALUE]


[HEAD (P)]<->[TAIL]

INSERT_HEAD A
    [A]
    [HEAD (P)]<->[TAIL]
    
    [HEAD (P)]<--[A]-->[TAIL]
    [HEAD (P)]<->[TAIL]

    [HEAD (P)]<->[A]-->[TAIL]
    [HEAD (P)]<--[TAIL]

    [HEAD (P)]<->[A]<->[TAIL]


REMOVE_HEAD
    [HEAD (P)]<->[A]<->[TAIL]
    
    [HEAD (P)]-->[TAIL]
    [HEAD (P)]<--[A]<->[TAIL]
    
    [HEAD (P)]<->[TAIL]
    [HEAD (P)]<--[A]-->[TAIL]

    [HEAD (P)]<->[TAIL]


INSERT_TAIL B
    [B]
    [HEAD (P)]<->[TAIL]

    [HEAD (P)]<--[B]-->[TAIL]
    [HEAD (P)]<->[TAIL]

    [HEAD (P)]<->[B]-->[TAIL]
    [HEAD (P)]<--[TAIL]

    [HEAD (P)]<->[B]<->[TAIL]


REMOVE_TAIL
    [HEAD (P)]<->[B]<->[TAIL]

    [HEAD (P)]<--[TAIL]
    [HEAD (P)]<->[B]-->[TAIL]
    
    [HEAD (P)]<->[TAIL]
    [HEAD (P)]<--[B]-->[TAIL]

    [B]
    [HEAD (P)]<->[TAIL]

INSERT_NODE_USING_POINTER RIGHT C
    [C]
    [HEAD (P)]<->[B]<->[TAIL]
    
    [HEAD (P)]<--[C]-->[B]<->[TAIL]
    [HEAD (P)]<->[B]<->[TAIL]
    
    [HEAD (P)]<->[C]-->[B]<->[TAIL]
    [HEAD (P)]<--[B]<->[TAIL]
    
    [HEAD (P)]<->[C]<->[B]<->[TAIL]
    
MOVE_POINTER KANAN 2
    [HEAD (P)]<->[C]<->[B]<->[TAIL]
    
    [HEAD]<->[C (P)]<->[B]<->[TAIL]
    
    [HEAD]<->[C]<->[B (P)]<->[TAIL]
    
INSERT_NODE_USING_POINTER LEFT D
    [D]
    [HEAD]<->[C]<->[B (P)]<->[TAIL]
    
    [HEAD]<->[C]<--[D]-->[B (P)]<->[TAIL]
    [HEAD]<->[C]<->[B (P)]<->[TAIL]
    
    [HEAD]<->[C]<->[D]-->[B (P)]<->[TAIL]
    [HEAD]<->[C]<--[B (P)]<->[TAIL]
    
    [HEAD]<->[C]<->[D]<->[B (P)]<->[TAIL]
    
    
"""


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(value="_HEAD")
        self.tail = Node(value="_TAIL")
        self.head.set_next(self.tail)
        self.tail.set_prev(self.head)
    
    def get_length_bruteforce(self):
        count = 0
        curr = self.head.next
        while curr != self.tail:
            count += 1
            curr = curr.next
        return count

    def print(self):
        nodes = []
        curr = self.head

        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        output = "<->".join(map(str, nodes))
        print(f"    {output}")
        print()


    # def insert_head(self, new_node: Node):
    #     old_head = self.head
    #     self.head = new_node

    #     old_head._prev = self.head
    #     self.head._next = old_head

    # def remove_head(self):
    #     self.head = self.head._next
    #     self.head._prev = None


    # def insert_tail(self, new_node: Node):
    #     old_tail = self.tail
    #     self.tail = new_node

    #     old_tail._next = self.tail
    #     self.tail._prev = old_tail

    # def remove_tail(self):
    #     self.tail = self.tail._prev
    #     self.tail._next = None

class Pointer:
    def __init__(self, node: Node):
        self.value = node.value
        self.node = node
        node.value = self

    def is_pointed_node_adjacent_to(self, other_node: Node):
        return other_node.prev is self.node or other_node.next is self.node

    def __repr__(self):
        return f"{self.value!r} (P)"

    def unpack(self):
        self.node.value = self.value


    def move_left(self, n: int = 1):
        """return new pointer after the movement, and boolean status of the operation (True: success, False: fail)"""
        if n == 0:
            return self, True
        if self.node.prev is None:
            return self, False

        self.unpack()
        ret = Pointer(self.node.prev)
        return ret.move_left(n - 1)

    def move_right(self, n: int = 1):
        if n == 0:
            return self, True
        if self.node.next is None:
            return self, False

        self.unpack()
        ret = Pointer(self.node.next)
        return ret.move_right(n - 1)


class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.prev: Node = prev
        self.next: Node = next
        self.value = value

    def __repr__(self):
        return f"[{self.value!r}]"

    def set_prev(self, node):
        self.prev = node

    def set_next(self, node):
        self.next = node

# prepend
# append
    def insert_after(self, new_next: Node):
        old_next = self.next
        #print(f"    old next-->{old_next}")
        #print()

        new_next.set_prev(self)
        #print(f"    {self}<--{new_next}")
        #print(f"    {self}<->{old_next}")
        #print()

        new_next.set_next(old_next)
        #print(f"    {self}<--{new_next}-->{old_next}")
        #print(f"    {self}<->{old_next}")
        #print()

        self.set_next(new_next)
        #print(f"    {self}<->{new_next}-->{old_next}")
        #print(f"    {self}<--{old_next}")
        #print()
        
        old_next.set_prev(new_next)
        #print(f"    {self}<->{new_next}<->{old_next}")
        #print()

    def insert_before(self, new_prev: Node):
        old_prev = self.prev
        #print(f"    old prev-->{old_prev}")
        #print()

        new_prev.set_next(self)
        #print(f"    {new_prev}-->{self}")
        #print(f"    {old_prev}<->{self}")
        #print()

        new_prev.set_prev(old_prev)
        #print(f"    {old_prev}<--{new_prev}-->{self}")
        #print(f"    {old_prev}<->{self}")
        #print()

        self.set_prev(new_prev)
        #print(f"    {old_prev}<--{new_prev}<->{self}")
        #print(f"    {old_prev}-->{self}")
        #print()

        old_prev.set_next(new_prev)
        #print(f"    {old_prev}<->{new_prev}<->{self}")

    def remove_before(self):
        self.prev.prev.remove_after()

    def remove_after(self):
        removed_next = self.next
        #print(f"    removed next-->{removed_next}")
        new_next = removed_next.next
        #print(f"    new next-->{new_next}")
        #print()

        #print(f"    {self}<->{removed_next}<->{new_next}")
        #print()

        self.set_next(new_next)
        #print(f"    {self}-->{new_next}")
        #print(f"    {self}<--{removed_next}<->{new_next}")
        #print()

        new_next.set_prev(self)
        #print(f"    {self}<->{new_next}")
        #print(f"    {self}<--{removed_next}-->{new_next}")
        #print()

        #print(f"    {self}<->{new_next}")
        #print()

def traverse_node(current: Node):
    while (current.next != None):
        # print_node(current)
        current = current.next

"""
Mungkin bisa dimasukin ke dalem class method aja
"""
def print_node(self, current: Node):
    if (current.prev != None):
        print("<-", end="")
    print(current.value, end="")
    if (current.next != None):
        print("->", end="")



"""
Commands:
    INSERT_HEAD [VALUE]
    REMOVE_HEAD
    
    INSERT_TAIL [VALUE]
    REMOVE_TAIL
    
    INSERT_NODE_USING_POINTER [DIREKSI] [VALUE]
    REMOVE_NODE_USING_POINTER [DIREKSI] [VALUE]
    MOVE_POINTER [DIREKSI] [VALUE]
"""


def main():
    doubly_linked_list = DoublyLinkedList()
    head = doubly_linked_list.head
    tail = doubly_linked_list.tail
    pointer = Pointer(doubly_linked_list.head)

    while True:
        errorOccured = False
        commands = input()
        if commands == "":
            continue
        command, *arg = commands.split()


        if command == "EXIT":
            break

        print(command)
        if command == "SIZE":
            print("   ", doubly_linked_list.get_length_bruteforce())
            print()
            continue
        if command == "IS_EMPTY":
            print("   ", head.next == tail)
            print()
            continue

        print("    Before: ")
        doubly_linked_list.print()

        if command == "INSERT_HEAD":
            if (len(arg) != 1):
                print("    Syntax error")
                print()
                continue
            head.insert_after(Node(arg[0]))
        elif command == "REMOVE_HEAD":
            if (len(arg) != 0):
                print("    Syntax error")
                print()
                continue
            if head.next == tail:
                print("    Unable to remove head or tail")
                print()
                continue
            if pointer.is_pointed_node_adjacent_to(head):
                pointer, success = pointer.move_left()
            head.remove_after()

        elif command == "INSERT_TAIL":
            if (len(arg) != 1):
                print("    Syntax error")
                print()
                continue
            tail.insert_before(Node(arg[0]))

        elif command == "REMOVE_TAIL":
            if (len(arg) != 0):
                print("    Syntax error")
                print()
                continue
            if tail.prev == head:
                print("    Unable to remove head or tail")
                print()
                continue

            if pointer.is_pointed_node_adjacent_to(tail):
                pointer, success = pointer.move_right()
            tail.remove_before()

        elif command == "INSERT_NODE_USING_POINTER":
            if (len(arg) != 2):
                print("    Syntax error")
                print()
                continue
            direction, value = arg

            if pointer.node == doubly_linked_list.tail and direction == "NEXT":
                print("    Insertion out of bound error")
                print()
                continue
            if pointer.node == doubly_linked_list.head and direction == "PREV":
                print("    Insertion out of bound error")
                print()
                continue

            if direction == "PREV":
                pointer.node.insert_before(Node(value))
            elif direction == "NEXT":
                pointer.node.insert_after(Node(value))
            else:
                print("Syntax error")
                print()
                continue

        elif command == "REMOVE_NODE_USING_POINTER":
            if (len(arg) != 1):
                print("    Syntax error")
                print()
                continue
            direction, *_ = arg
            if direction == "PREV":
                if pointer.node == doubly_linked_list.head:
                    print("    Head do not have previous node")
                    print()
                    continue
                if pointer.node.prev == doubly_linked_list.head:
                    print("    Unable to remove head or tail")
                    print()
                    continue
                pointer.node.remove_before()
            elif direction == "NEXT":
                if pointer.node == doubly_linked_list.tail:
                    print("    Tail do not have next node")
                    print()
                    continue
                if pointer.node.next == doubly_linked_list.tail:
                    print("    Unable to remove head or tail")
                    print()
                    continue
                pointer.node.remove_after()
            else:
                print("    Syntax error")

        elif command == "MOVE_POINTER":
            if (len(arg) != 2):
                print("    Syntax error")
                print()
                continue
            direction, n = arg
            try:
                n = int(n)
                if n <= 0:
                    raise Exception
            except Exception:
                print("    Syntax error")
                print()
                continue
            n = int(n)
            success = True
            if direction == "PREV":
                pointer, success = pointer.move_left(n)
            elif direction == "NEXT":
                pointer, success = pointer.move_right(n)
            else:
                print("    Syntax error")

            if not success:
                print("    Steps out of bound error")
                print()
                continue

        if not errorOccured:
            print("    After: ")
            doubly_linked_list.print()

if __name__ == "__main__":
    main()

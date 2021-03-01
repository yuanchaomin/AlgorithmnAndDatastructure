class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class MyLinkedList:
    def __init__(self, val=None):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr_index = 0
        curr_p = self.head.next

        if index > (self.size - 1):
            return -1

        while curr_p:
            if curr_index == index:
                return curr_p.val
            else:
                curr_index += 1
                curr_p = curr_p.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        if val is None:
            return
        else:
            NewHead = ListNode(val)
            OldHead = self.head.next
            self.head.next = NewHead
            NewHead.next = OldHead
            self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        if val is None:
            return
        else:
            TailNode = ListNode(val)
            Curr_p = self.head

            while Curr_p.next:
                Curr_p = Curr_p.next

            Curr_p.next = TailNode
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """

        curr_index = -1
        curr_p = self.head

        while curr_p.next:
            if curr_index == (index - 1):
                NewNode = ListNode(val)
                next_p = curr_p.next
                curr_p.next = NewNode
                NewNode.next = next_p

                curr_index += 2
                curr_p = curr_p.next.next

            else:
                curr_index += 1
                curr_p = curr_p.next

        if index == self.size:
            self.addAtTail(val)
            return

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr_index = 0
        curr_p = self.head.next

        if index > self.size - 1:
            return

        if index == 0:
            newHead_p = curr_p.next
            curr_p.next = None
            self.head.next = newHead_p

        while curr_p:
            if curr_index == (index - 1):
                #                 print("what is that {}".format(curr_p.next.next))
                #                 curr_index += 1

                if curr_p.next.next:
                    pre_p = curr_p
                    curr_p = pre_p.next
                    next_p = pre_p.next.next
                    curr_p.next = None
                    pre_p.next = next_p
                    curr_index += 2
                else:
                    curr_p.next = None
                    break
            else:
                curr_index += 1
                curr_p = curr_p.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIn|dex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
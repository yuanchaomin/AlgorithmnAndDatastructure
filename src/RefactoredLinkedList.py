# try to use the dummy node and compare those two implementation
# try to implement a search method in the LinkedList implementation
class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self,val=None):
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail

    def search(self, GivenValue:int):
        index = 0
        p = self.head
        preP = None
        while p.next:
            if p.val == GivenValue:
                return preP,p,index
            else:
                preP = p
                p = p.next
                index += 1
        return preP,p, index

    def getNodeByIndex(self, givenIndex:int) -> ListNode:
        index = -1
        p = self.head
        if givenIndex > self.size:
            raise ValueError("The GivenIndex should be less than the size of the LinkedList")
        elif self.head.next.val == -1:
            raise ValueError("Can not get any node from am empty LinkedList")
        while p.next:
            if index == givenIndex:
                return p
            p = p.next
            index += 1
        return None

    def getValueByIndex(self, index:int) -> int:
        return (self.getNodeByIndex(index).val)

    def get(self, index:int) -> int:
        return self.getValueByIndex(index)

    def addAtHead(self,val:int) -> None:
        if val is None:
            return
        if self.head.next.val == -1:
            self.head.next = ListNode(val)
            self.head.next.next = self.tail
        else:
            oldHead = self.head.next
            newHead = ListNode(val)
            self.head.next = newHead
            newHead.next = oldHead
        self.size +=1

    def addAtTail(self, val:int) -> None:
        if val is None:
            return
        p = self.head
        while p.next and p.next.val != -1:
            p = p.next
        p.next = ListNode(val)
        p.next.next = self.tail
        self.size += 1

    def deleteHead(self) -> None:
        p = self.head
        if self.head.next.val == -1:
            raise ValueError("Eempty LinkedList has no elements, thus can not perform delete operation")
        else:
            p.next = p.next.next

    def deleteTail(self) -> None:
        preP = None
        p = self.head
        if self.head.next.val == -1:
            raise ValueError("Eempty LinkedList has no elements, thus can not perform delete operation")
        while p.next:
            preP = p
            p = p.next
        preP.next = p.next

    def addAtIndex(self, index:int, val:int) -> None:

        if index < 0:
            raise ValueError("Index must be positive")
        elif index == 0:
            return self.addAtHead(val)
        elif index == self.size - 1:
            return self.addAtTail(val)
        elif (index > self.size -1):
            raise ValueError("Index cannot larger than length of LinkedList")
        else:
            foundedNode = self.getNodeByIndex(index)
            preNode = self.getNodeByIndex(index - 1)
            newNode = ListNode(val)
            preNode.next = newNode
            newNode.next = foundedNode
        return

    def deleteAtIndex(self, index:int) -> None:
        if index < 0:
            raise ValueError("Index must be positive")
        elif index == 0:
            return self.deleteHead()
        elif index == self.size - 1:
            return self.deleteTail()
        elif (index > self.size -1):
            raise ValueError("Index cannot larger than length of LinkedList")
        else:
            foundedNode = self.getNodeByIndex(index)
            preNode = self.getNodeByIndex(index - 1)
            preNode.next = foundedNode.next
        return

    def printAllValue(self) -> None:
        p = self.head
        while p.next :
            p = p.next
            if p.val != -1:
                print(p.val)












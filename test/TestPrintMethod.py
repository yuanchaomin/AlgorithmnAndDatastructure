from src.RefactoredLinkedList import LinkedList


if __name__  == "__main__":
    obj = LinkedList()
    for i in range(0,20):
        obj.addAtTail(i)
    #obj.addAtIndex(0,1)


    obj.printAllValue()


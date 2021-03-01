from src.RefactoredLinkedList import LinkedList


if __name__  == "__main__":
    obj = LinkedList()
    for i in range(1,11):
        obj.addAtHead(i)
    #obj.addAtIndex(0,1)


    obj.printAllValue()


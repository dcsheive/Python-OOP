class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SList:
    def __init__(self):
        self.head = None
        self.tail = None

    def PrintAllVals(self):
        runner = self.head
        while runner.next != None:
            print(runner.value)
            runner = runner.next
            if runner.next == None:
                print(runner.value)
                print()

    def AddBack(self, val):
        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node

    def AddFront(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node

    def InsertBefore(self, nextVal, val):
        new_node = SLNode(nextVal)
        runner = self.head
        while runner.next.value != val:
            runner = runner.next
        temp = runner.next
        runner.next = new_node
        new_node.next = temp

    def InsertAfter(self, preVal, val):
        new_node = SLNode(preVal)
        runner = self.head
        while runner.value != val:
            runner = runner.next
        temp = runner.next
        runner.next = new_node
        new_node.next = temp

    def RemoveNode(self, val):
        runner = self.head
        while runner.next.value != val:
            runner = runner.next
        runner.next = runner.next.next

    def ReverseList(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous  # None, first time round.
            previous = current  # Used in the next iteration.
            current = next  # Move to next node.
        self.head = previous




list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
list.head.next.next.next = SLNode('Ben')

# something close to this should be utilized for all of the above problems
list.PrintAllVals()
list.AddBack('Tony')
list.PrintAllVals()
list.AddFront('Michael')
list.PrintAllVals()
list.InsertBefore('Gordon', 'Debra')
list.PrintAllVals()
list.InsertAfter('Nancy', 'Ben')
list.PrintAllVals()
list.RemoveNode('Chad')
list.PrintAllVals()
list.ReverseList()
list.PrintAllVals()

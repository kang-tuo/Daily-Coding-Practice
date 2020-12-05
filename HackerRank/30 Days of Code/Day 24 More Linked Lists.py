class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        # Write your code here
        if head is not None and head.next is not None:
            if head.data == head.next.data:
                head.next = head.next.next
                self.removeDuplicates(head)
            else:
                self.removeDuplicates(head.next)
        return head


mylist = Solution()
T = [1, 1, 2, 2, 2, 2, 3]
head = None
for i in range(len(T)):
    data = T[i]
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)

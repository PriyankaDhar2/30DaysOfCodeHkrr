class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    def removeDuplicates(self, head):
        current = head

        # Check if the list is empty or has only one node
        if not current or not current.next:
            return head

        # Traverse the list
        while current.next:
            # Compare current node's data with the next node's data
            if current.data == current.next.data:
                # If they are equal, skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head

    # Function to print the linked list
    def printList(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
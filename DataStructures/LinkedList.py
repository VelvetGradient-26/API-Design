class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None
        self.length = 0

    # Insert at end
    def append(self, value):
        node = Node(value) 
        if self.head is None: 
            self.head = node
        else: 
            current = self.head
            while current.next is not None: 
                current = current.next
            current.next = node
        self.length += 1

    # Insert at beginning
    def prepend(self, value): 
        node = Node(value)

        if self.head is None: 
            self.head = node
        else: 
            node.next = self.head
            self.head = node

        self.length += 1

    # Insert at position
    def insert(self, value, pos): 
        pass

    # Delete node by value        
    def delete(self, value): 
        pass

    # Delete node by position
    def pop(self, index): 
        pass

    # get the value by position
    def get(self, index): 
        pass

    # Print the Linked List
    def __str__(self):
        result = ""

        current = self.head
        while current: 
            result += str(current.value) + " -> "
            current = current.next

        result += "None"

        return result

    # Print the Length of the Linked List
    def __len__(self): 
        return self.length

    # Check if a value exist in Linked List
    def __contains__(self, item):
        pass

if __name__ == "__main__": 
    ll = LinkedList()

    nums = [num for num in range(10, 110, 10)]
    print(nums)

    for num in nums: 
        ll.append(num)

    print(ll)

    
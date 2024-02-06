class Node:
    """
    Defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with data and next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for next_node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list
    """

    def __init__(self):
        """
        Initializes a singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

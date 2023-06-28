#!/usr/bin/python3
""" defines a class node."""


class Node:
    """Node is represented here."""

    def __init__(self, data, next_node=None):
        """This initiates the class.

        Args:
            data (int): data in the node
            next_node (:obj:): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ This retrieves the data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """retrieves the next_node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """REPRESENTS A LINED LIST."""

    def __init__(self):
        """initiates the linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """inserts and sorts in list.

        Args:
            value (Node): node to be added
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            head = self.__head
            while (head.next_node is not None and head.next_node.data < value):
                head = head.next_node
            new.next_node = head.next_node
            head.next_node = new

    def __str__(self):
        """the representative of the class."""
        display_list = []
        head = self.__head
        while head is not None:
            display_list.append(str(head.data))
            head = head.next_node
        return ("\n".join(display_list))

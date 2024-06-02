#!/usr/bin/python3
""" class that defines a node of a singly linked list """


class Node:
    """ Node class """
    def __init____(self, data, next_node=None):
        """instantiation"""
        self.data = data
        self.nextnode = next_node
    
    @property
    def data(self):
        """ getter """
        return self.__data
    
    @data.setter
    def data(self, value):
        """setter"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """ getter """
        return self.__nextnode
    
    @next_node.setter
    def next_node(self, value):
        """setter"""
        if value is not None and type(value) != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ SinglyLinkedList class """
    def __init__(self):
        """Initialize SSL class"""
        self.head = None

    def __str__(self):
        """To string method"""
        result = ""
        node = self.head
        while node:
            result += str(node.data) + '\n'
            node = node.next_node
        return result[:-1]

    def sorted_insert(self, value):
        """Inserts a new node at sorted position"""
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new_node.next_node = node.next_node
        node.next_node = new_node

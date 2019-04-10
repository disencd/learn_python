

class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        _temp_node = Node(data)
        if not self.head:
            self.head = _temp_node
        else:
            temp = self.head
            _temp_node.link = temp
            self.head = _temp_node

    def append_back(self, data):
        _temp_node = Node(data)
        if not self.head:
            self.head = _temp_node
        else:
            temp = self.head
            while temp.link:
                temp = temp.link
            temp.link = _temp_node

    def display_list(self):
        start = self.head

        if not start:
            print("List Empty")

        while start:
            print("{} -> ".format(start.data))
            start = start.link

    def reverse_list(self):
        print("Reverse List........")
        first = self.head
        sec = first.link

        first.link = None

        while sec:
            temp = sec.link
            sec.link = first
            first = sec
            sec = temp

        self.head = first

if __name__ == "__main__":
    l = LinkedList()
    l.insert_front(1)
    l.insert_front(2)
    l.append_back(3)
    l.insert_front(4)
    l.append_back(5)
    l.insert_front(6)
    l.display_list()
    l.reverse_list()
    l.display_list()

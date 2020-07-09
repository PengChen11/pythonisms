from collections.abc import Iterable

class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LL:
    def __init__(self, data_list=None):
        self.head = None
        self.length = 0
        if isinstance(data_list, Iterable):
            for data in reversed(data_list):
                self.prepend(data)
        else:
            self.prepend(data_list)


    def prepend (self, value):
        '''method to add a node infrond of everything else'''
        self.head = Node(value, self.head)
        self.length += 1


    def __iter__(self):

        def get_value():
            '''method to get the value of LL'''
            current = self.head
            while current:
                yield current.value
                current = current.next
        return get_value()


    def __len__(self):
        return self.length


    def __eq__(self,other_list):
        return list(self) == list(other_list)


    def __str__(self):

        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"


    def __getitem__(self, index):
        '''method to make the link list supports get item with index like working with a list. Support negetive index too'''

        if abs(index) > self.length or index==self.length:
            raise IndexError

        if index >= 0:
            for i, item in enumerate(self):
                if i == index:
                    return item

        if index < 0 :
            for i, item in enumerate(self):
                if i == self.length+index:
                    return item

